# __main__.py
import sys, os, getopt, logging

sys.path.append(os.path.abspath(__file__ + "../../../"))

import genreqs
from genreqs import parse

def main():
    """
        --- Generate requirements for you project ---
    """
    argv = sys.argv[1:]
    pip_list = []
    path = ""

    try:
        options, args = getopt.getopt(
            argv, "p:",
            ["path ="]
        )

        for name, value in options:
            if name.strip()  == '-p' or name.strip() == '--path':
                path = value
                pip_list = parse.minimal_task(value)
    except Exception as e:
        logging.warning(f"Something wrong happened {str(e)}")

    if len(sys.argv) == 1:
        #print("Need help ? Add -h or --help to your command")
        pip_list = parse.minimal_task()

    else:
        if "-h" in sys.argv or '--help' in sys.argv:
            help = """
Usage:
    genreqs [options]

    Options:
        -h, --help              Show help
        -V, --version           Show version and exit
        -p, --path              Generate requirements.txt from python folder / virtual environment
"""
        if '-V' in sys.argv or '--version' in sys.argv:
            logging.info(f"GenReqs version {genreqs.__version__}")
    
    if pip_list:
        master_packages = parse.get_only_master_packages(pip_list, path)
        parse.create_requirements_txt(master_packages)
        working_dir = os.getcwd()
        separator = "\\" if os.getcwd().find("\\") != -1 else "/"
        msg = '\33[32m' + "\nTask completed! "+'\33[0m' + "\nPlease find your requirements.txt at "
        req_path = working_dir + separator + "requirements.txt"

        clikable = f"\x1b]8;;{req_path}\a{req_path}\x1b]8;;\a"
        
        sys.stdout.write(msg + clikable)
        sys.stdout.flush()
    else:
        logging.info("No python package has been installed on this environment")

if __name__ == "__main__":
    main()