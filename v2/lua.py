import sys
import os
import shutil

projectName = "project"
sappApiVersion = "1.10.1.0"
projectDirName = "example-one"
sharedDir = "shared"
sourceDir = "src"
entryFile = "main.lua"

# --DO NOT MODIFY ANYTHING UNDER THIS LINE UNLESS YOU KNOW WHAT YOU ARE DOING!!!

# -- Data Structures


class ListStructure:
    def __init__(self, startingElem=None):
        self.list = []
        self.length = 0
        if startingElem != None:
            self.list.append(startingElem)
            self.length += 1

    def push(self):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def getLength(self):
        return self.length


class Queue(ListStructure):
    def __init__(self, startingElem=None):
        super().__init__(startingElem)

    def push(self, newElem):
        self.list.append(newElem)
        self.length += 1

    def pop(self):
        if self.length > 0:
            self.length -= 1
            return self.list.pop(0)
        else:
            return None

    def enqueue(self, newElem):
        self.push(newElem)

    def dequeue(self):
        return self.pop()

    def peek(self):
        if self.length <= 0:
            return None
        return self.list[0]

    def search(self, elemToFind):
        for elem in self.list:
            if elemToFind == elem:
                return True
        return False


class Stack(ListStructure):
    def __init__(self, startingElem=None):
        super().__init__(startingElem)

    def push(self, newElem):
        self.list.append(newElem)
        self.length += 1

    def pop(self):
        if self.length > 0:
            self.length -= 1
            return self.list.pop()
        else:
            return None

    def search(self, elemToFind):
        for elem in self.list:
            if elem == elemToFind:
                return True
        return False

    def peek(self):
        if self.length <= 0:
            return None
        return self.list[self.length-1]

# -- Program


def buildDir(dirname):
    return os.path.join(os.getcwd(), dirname)


def isValidFile(fileName):
    modifiedFile = fileName.split(".")
    for item in modifiedFile:
        if item == "test":
            return False
        if item == "lua":
            return True
    return False


def constructFileWithDir(dirname):
    bfs = Queue()
    bfs.enqueue(dirname)
    output = ""
    while(bfs.getLength() > 0):
        nextItem = bfs.dequeue()
        if os.path.isdir(nextItem) and nextItem != sharedDir:
            cwd = os.chdir(nextItem)
            directories = os.listdir(cwd)
            for item in directories:
                bfs.enqueue(buildDir(item))
        elif isValidFile(os.path.basename(nextItem)):
            file = open(nextItem, "r")
            output += file.read()
            output += "\n\n"
            file.close()
        else:
            continue
    return output


def build():
    projectDir = os.getcwd()
    output = constructFileWithDir(os.path.join(
        os.getcwd(), projectDirName, sharedDir))
    os.chdir(projectDir)
    output += constructFileWithDir(os.path.join(os.getcwd(),
                                                projectDirName, sourceDir))
    os.chdir(projectDir)
    output += constructFileWithDir(os.path.join(os.getcwd(),
                                                projectDirName, entryFile))
    file = open(projectName + ".lua", "w")
    file.write(output)
    file.close()


if __name__ == "__main__":
    build()
