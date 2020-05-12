import sys
import os
import shutil
from queue import Queue  # put(value) to push, get() to remove

projectName = "project"
projectDirName = "example-one"
sappApiVersion = "1.10.1.0"


def pushFullDir(dirname):
    return os.path.join(os.getcwd(), dirname)


def isTestFile(fileName):
    modifiedFile = fileName.split(".")
    for item in modifiedFile:
        if item == "test":
            return True
    return False


def build():
    bfs = Queue()
    bfs.put(pushFullDir(projectDirName))

    while(bfs.qsize() > 0):
        cwd = os.chdir(bfs.get())
        directories = os.listdir(cwd)
        for item in directories:
            if os.path.isdir(item):
                bfs.put(pushFullDir(item))
            elif isTestFile(item) == False:
                print(item)


if __name__ == "__main__":
    build()
