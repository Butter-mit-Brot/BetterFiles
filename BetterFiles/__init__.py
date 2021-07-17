import os
import json
import shutil
import zipfile

########## universal ################

def createF(name, text, overwrite=False):
    def select(file):
        if os.path.isfile(name):

            if os.stat(name).st_size != 0:
                if overwrite is False:
                    return 'a'
                else:
                    pass
            return 'w'

        return 'x'
    f = open(name, select(name))
    f.write(text + '\n')
    f.close()

def readF(name):
    f = open(name, 'r')
    x = f.read()
    f.close()
    return x

############ JSON ###############

def createJSON(name, dict, indent: int):
    f = open(name, "w", encoding="utf-8")
    json.dump(dict, f, ensure_ascii=False, indent=indent)
    f.close()

def readJSON(name):
    f = open(name)
    data = json.load(f)
    return data

######## HTML #############

def createHTML(name,Title, text):


    tx = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{Title}</title>
</head>
<body>
    <p>{text}</p>
</body>
</html>
        """

    H = open(name, "w")
    H.write(tx)
    H.close()

######### standard os functions ##########

def move(original, to):
    shutil.move(original, to)

def delete(file):
    os.remove(file)

def copy(original, to):
    shutil.copy(original, to)

def rename(file, to):
    os.rename(file, to)


######### zip files ##########

def extractZIP(file):
    zip = zipfile.ZipFile(file, 'r')
    path = os.getcwd()
    zip.extractall(path=path)
    zip.close()

def makeZIP(name,*args):
    li = []
    for i in args:
        li.append(i)
    with zipfile.ZipFile(name, 'w') as new_zip:
        for name in args:
            new_zip.write(name)




