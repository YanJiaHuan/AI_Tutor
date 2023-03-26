import os
import shutil

def clear_directory(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)


# Replace 'path1/path2' with the path to the directory you want to clear
path1 = "../data"
# path2 = "../export"
# path3 = "./pdf_files"
clear_directory(path1)
# clear_directory(path2)
# clear_directory(path3)