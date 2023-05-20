# __main__.py
import sys, os, getopt

sys.path.append(os.path.abspath(__file__ + "../../../"))

import genreqs
from genreqs import parse

def main():
    """
        --- Generate requirements for you project ---
    """

    argv = sys.argv[1:]
    pip_list = []

    try:
        options, args = getopt.getopt(
            argv, "p:",
            ["path ="]
        )

        for name, value in options:
            if name.strip()  == '-p' or name.strip() == '--path':
                print(name, value)
                pip_list = parse.minimal_task(value)
    except Exception as e:
        print("Something wrong happened", str(e))

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
            print(f"GenReqs version {genreqs.__version__}")
    
    if pip_list:
        parse.get_only_master_packages(pip_list)

if __name__ == "__main__":
    main()