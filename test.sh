#!/bin/bash
set -e
coverage run -m unittest discover -s tests -p "*.py" --verbose
coverage xml -o coverage.xml  # Outputs Cobertura XML



#python3 -m unittest discover -s src/tests
