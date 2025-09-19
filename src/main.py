
"""This is the starting module"""

import os
import shutil


def main():
    """Main function that executes the entire application"""

    if not os.path.exists("./static"):
        raise FileNotFoundError("The ./static path does not exists")

    if os.path.exists("./public"):
        shutil.rmtree("./public")

    os.mkdir("./public")

    src = "./static"
    dest = "./public"

    copy_static(src, dest)


def copy_static(src, dest):
    """ recursively copies static files into public directory"""

    current_src = src
    current_dest = dest
    content = os.listdir(current_src)

    for item in content:

        if os.path.isfile(f"{current_src}/{item}"):
            shutil.copy(f"{current_src}/{item}", f"{current_dest}/{item}")
        else:
            os.mkdir(f"{current_dest}/{item}")
            copy_static(f"{current_src}/{item}", f"{current_dest}/{item}")

main()
