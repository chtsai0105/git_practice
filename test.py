import shutil

fasttree_bins = ("FastTree", "fasttree")

for fasttree in fasttree_bins:
    fasttree = shutil.which(fasttree)
    if fasttree:
        print(f"Found FastTree at {fasttree}")
        break

if not fasttree:
    raise RuntimeError(
        'FastTree not found. Please install it through "conda install bioconda::fasttree"'
    )
