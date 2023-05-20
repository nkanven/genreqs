import sys, os
sys.path.append(os.path.abspath(__file__ + "../../../"))

"""Template robot with Python."""
import os, subprocess

def minimal_task(path = "")->list:

    freeze = subprocess.check_output(f"{path}pip freeze")
    freeze_list = freeze.decode("utf-8")

    if not freeze_list: return 0
    else:
        freeze_list = freeze_list.splitlines()
    
    return freeze_list if type(freeze_list) == list else list(str(freeze_list))

def get_only_master_packages(pip_list)->list:
    master_packages = []
    #package_names = [x.split("==")[0] for x in pip_list]

    #print(package_names)
    def remove_dependancies():
        print("dd")