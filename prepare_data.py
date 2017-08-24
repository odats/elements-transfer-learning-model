import os
import os.path
from shutil import copyfile, rmtree
import uuid
from PIL import Image

def prepare_data(folder_from, folder_to):
    print("start")
    
    # clear folder
    rmtree(folder_to)
    
    files = []
    for dirpath, dirnames, filenames in os.walk(folder_from):
        for filename in [f for f in filenames if (f.endswith(".jpg") or f.endswith(".png"))]:
            # get path to file
            file_path = os.path.join(dirpath, filename)
            files.append(file_path)
            
            # get class
            start = file_path.index("/", 0) + 1
            end = file_path.index("/", start)
            class_name = file_path[start:end]
            
            # create class folder 
            if not os.path.exists(folder_to + "/" + class_name):
                os.makedirs(folder_to + "/" + class_name)
            
            # copy file
            file_name = uuid.uuid4().hex + ".jpg"
            
            if(filename.endswith(".jpg")):
                copyfile(file_path, folder_to + "/" + class_name + "/" + file_name)
            elif (filename.endswith(".png")):
                Image.open(file_path).save(folder_to + "/" + class_name + "/" + file_name)            
    
    print("processed files: ", len(files))

prepare_data("data_tree", "geometry_data")
