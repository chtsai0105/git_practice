import subprocess
import shutil
from sys import argv


def locate_fasttree():
    fasttree_bins = ("Fasttree", "fasttree")

    for fasttree in fasttree_bins:
        fasttree = shutil.which(fasttree)
        if fasttree:
            return fasttree
    raise RuntimeError('FastTree not found. Please install it through "conda install bioconda::fasttree"')


def main(args):
    args = args or argv[1]
    results = subprocess.run([locate_fasttree(), "-gamma", args], capture_output=True, check=True, text=True)
    print(results)
