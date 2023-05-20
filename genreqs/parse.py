import sys, os, re
from math import log, ceil
sys.path.append(os.path.abspath(__file__ + "../../../"))

"""Template robot with Python."""
import os, subprocess

def minimal_task(path = "")->list:

    freeze = subprocess.check_output(f"{path}pip freeze")
    freeze_list = freeze.decode("utf-8")

    if not freeze_list: return 0
    else:
        freeze_list = freeze_list.splitlines()
    result = freeze_list if type(freeze_list) == list else list(str(freeze_list))
    return result

def create_requirements_txt(pip_list):
    with open("requirements.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(pip_list))


def get_only_master_packages(pip_list, path = "")->list:
    master_packages = []
    package_names = [x.split("==")[0] for x in pip_list]
    i = 0
    
    # Check for dependancies
    for package in package_names:
        p_show = subprocess.check_output(f"{path}pip show {package}")
        try:
            p_show = p_show.decode("utf-8")
        except UnicodeDecodeError:
            p_show = p_show.decode("latin-1")

        p_show = p_show.splitlines()
        required_by = p_show[-1].split(":")[1].strip()
        split_dependancies = required_by.split(",")

        if split_dependancies[0] == "":
            # Package is not required by anyone"
            master_packages.append(pip_list[i])

        i += 1
        countdown(len(pip_list), i)

    return master_packages

def countdown(total, count):
    percent = (count * 100) / total
    bar = log(percent, 100) * 100
    bar =  bar if bar > 0 else 1
    
    bar_mul = "===" * ceil(bar/10)
    os.system('cls||clear')
    msg = '\33[94m'+"GenReqs: " + '\33[0m' + '\33[6m' + "Processing task..." +'\33[0m' + "\n\n"
    msg += '\33[33m'+"Please wait while we gather your required packages" +'\33[0m' + "\n"
    if bar < 100:
        '\33[31m'
        msg += '\33[31m' + str(bar_mul) + "=> " + str(format(bar, ".2f")) + "%"+'\33[0m'
    else:
        msg += '\33[32m' + str(bar_mul) + "=> " + str(format(bar, ".2f")) + "%"+'\33[0m'
    sys.stdout.write(msg)
    sys.stdout.flush()
