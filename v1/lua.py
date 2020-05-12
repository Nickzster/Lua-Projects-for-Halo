outputFile = 'gta_halo.lua'
apiVersion = 'api_version = "1.10.1.0"'


import sys
import os
import os.path
import shutil

def init(projectName):
    try:
        if(os.path.exists("./" + projectName)):
           exit()
        print('Creating project directory...')
        os.getcwd()
        os.mkdir("./" + projectName)
        os.chdir(projectName)
        print('Creating config...')
        config = open("config.lua", "w")
        config.write(apiVersion)
        config.close()
        print('Creating callbacks...')
        print('Creating functions...')
        os.mkdir('definitions')
        os.mkdir('callbacks')
        os.mkdir('functions')
        os.chdir('definitions')
        definitions = open('definitions.lua', "w")
        definitions.write("--Callback Definition File.\n--Define your callbacks here.\n\nfunction OnScriptLoad()\nend")
        definitions.close()
        gc = open('garbage_collection.lua', "w")
        gc.write("--Cleanup File.\n--Write your cleanup functions in here.\n\nfunction OnScriptUnload()\nend")
        gc.close()
        variables = open('variables.lua', "w")
        variables.write('--Define your global variables in here.\n--Any of your lua functions or callbacks will be able to reference them.')
        variables.close()
        os.chdir('../functions')
        functions = open('functions.lua', "w")
        functions.write("--Utility Functions.\n--You can implement utility functions in here, or in separate file(s) within this directory.")
        functions.close()
        os.chdir('../callbacks')
        callbacks = open('callbacks.lua', "w")
        callbacks.write("--Implement your callbacks in here.\n--You can also implement them in separate files, within the callback directory.")
        callbacks.close()
    except SystemExit:
        print("Project directory exists. Terminating init process.")
    except:
        print("Project init failed. Check to see if it already exists!")

def writeFiles(os, file):
    listOfDirectories = os.listdir(os.getcwd())
    listOfDirectories.sort()
    for filename in listOfDirectories:
        contents = open(filename, "r")
        file.write(contents.read())
        file.write("\n\n")
        contents.close()
        

def build(projectName):
    try:
        os.getcwd()
        os.chdir(projectName)
        output = open(projectName + ".lua", "w")
        print("Writing definitions...")
        os.chdir('./definitions')
        writeFiles(os, output)
        print("Writing functions...")
        os.chdir('../functions')
        writeFiles(os, output)
        print("Writing callbacks...")
        os.chdir("../callbacks")
        writeFiles(os, output)
        output.close()
        print('File ' + projectName + ".lua successfully built.")
    except:
        print("Could not build project.")


if __name__ == "__main__": 
    try:
        if(sys.argv[1] == 'init'):
            init(sys.argv[2])
        if(sys.argv[1] == 'build'):
            build(sys.argv[2])
        if(sys.argv[1] == 'help'):
            print("=====\npython3 lua.py init <name>\nInitalizes a new project with the directory of <name>\n=====")
            print("python3 lua.py build\nBuilds a main.lua file containing all of the files within the <name> directory.\n=====")
    except IndexError:
        print("You have entered too few arguments.")
    except:
        print("Something went wrong!")