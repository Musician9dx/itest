import pickle as pk
import os


class object_handler():

    def __init__(self):
        pass

    def save_object(self, obj, path, replace=True):

        if replace:

            if os.path.isfile(path):
                os.remove(path)

            file = open(path, "+wb")

            pk.dump(obj=obj, file=file)

        else:

            if os.path.isfile(path):
                print("File Already Exists")

                return "Can't Create a File If File Already Exists"
            file = open(path, "wb")

            pk.dump(obj, file)

    def load_object(self, path):

        try:

            file = open(path, "rb")

            obj = pk.load(file)

            return obj

        except:

            print("File Doesn't exist")

            return "File Doesn't Exist"



