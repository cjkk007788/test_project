import os

def read_folder(path):
    output = os.listdir(path)

    for item in output:
        if os.path.isdir(item):
            read_folder(path+"/"+item)
        else :
            print(item)


            
read_folder(".")          