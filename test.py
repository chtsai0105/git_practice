import shutil

fasttree_bins = ("FastTree", "fasttree")

for fasttree in fasttree_bins:
    fasttree = shutil.which(fasttree)
    if fasttree:
        print(f"Found FastTree at {fasttree}")
        break

print(fasttree)
