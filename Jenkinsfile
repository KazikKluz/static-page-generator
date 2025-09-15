pipeline {
    triggers {
        pollSCM('H/1 * * * *')
    }

    agent {
        kubernetes {
yaml """
            apiVersion: v1
            kind: Pod
            spec:
              containers:
                - name: jnlp
                  image: jenkins/inbound-agent:3309.v27b_9314fd1a_4-6

                - name: python
                  image: python:3.13
                  command: ["cat"]
                  tty: true
            """
        }
    }

    stages {
         stage('Checkout') {
            steps {
                git(
                    url: 'https://github.com/KazikKluz/static-page-generator.git',
                    branch: 'main',
                    credentialsId: 'github-credentials'
                )
            }
        }

        stage('Install Dependencies'){
            steps {
                container('python') {
                    dir('.') {
                        sh 'pip install -r requirements.txt'
                    }
                }
            }
        }

        stage('Test & Coverage') {
            steps {
                container('python') {
		            dir('.') {
                        sh './test.sh'
	                }
                }
            }
        }

        stage('SonarCloud check') {
            steps {
                container('python') {
                    withCredentials([string(credentialsId: 'SONAR_TOKEN', variable: 'SONAR_TOKEN')]) {
                        sh '''
			    export SONAR_SCANNER_VERSION=7.0.2.4839
			    export SONAR_SCANNER_HOME=$HOME/.sonar/sonar-scanner-$SONAR_SCANNER_VERSION-linux-x64
			    curl --create-dirs -sSLo $HOME/.sonar/sonar-scanner.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-$SONAR_SCANNER_VERSION-linux-x64.zip
			    unzip -o $HOME/.sonar/sonar-scanner.zip -d $HOME/.sonar/
		            export PATH=$SONAR_SCANNER_HOME/bin:$PATH
			    export SONAR_SCANNER_OPTS="-server"

			    sonar-scanner \\
 				-Dsonar.organization=kazikkluz \\
  				-Dsonar.projectKey=KazikKluz_static-page-generator \\
  				-Dsonar.sources=./src \\
  				-Dsonar.host.url=https://sonarcloud.io \\
                -Dsonar.token=${SONAR_TOKEN} \\
                -Dsonar.python.coverage.reportPaths=coverage.xml \\
                        '''
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 1, unit: 'HOURS'){
                    waitForQualityGate abortPipeline: true
                }
            }
        }

    }

    post {
        always {
            archiveArtifacts artifacts: 'coverage.xml', allowEmptyArchive: true
        }
        success {
          slackSend  color: "good", message: "The pipeline has succeeded. ${currentBuild.fullDisplayName}"
        }

        failure {
          slackSend  color: "danger", message: "The pipeline has failed. ${currentBuild.fullDisplayName}"
        }
    }
}
