
"""This is the starting module"""

import os
import shutil


SRC = "./static"
DEST = "./public"


def main():
    """Main function that executes the entire application"""

    if not os.path.exists(SRC):
        raise FileNotFoundError("The ./static path does not exists")

    if os.path.exists(DEST):
        shutil.rmtree(DEST)

    os.mkdir(DEST)

    copy_static(SRC, DEST)


def copy_static(source, destination):
    """ recursively copies static files into public directory"""

    current_src = source
    current_dest = destination
    content = os.listdir(current_src)

    for item in content:

        if os.path.isfile(f"{current_src}/{item}"):
            shutil.copy(f"{current_src}/{item}", f"{current_dest}/{item}")
        else:
            os.mkdir(f"{current_dest}/{item}")
            copy_static(f"{current_src}/{item}", f"{current_dest}/{item}")


main()
