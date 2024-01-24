# This program will duplicate taunts (placed in the "input" folder) or other motion files so that they apply to all characters.
# However, it can also copy any folder of your choice for all characters.
# Files will be copied in the following directory for all characters: fighter\<char name>\motion\body\<slot>\
# Folders will be copied in the following directory for all characters: fighter\<char name>\

import os, subprocess, shutil, msvcrt

def main():
    # quit if input is empty
    inputContents = os.listdir(".\\input")
    outputContents = os.listdir(".\\output")
    if len(inputContents) <= 0:
        print("No file(s) in input folder!")
        programEnd()
    
    # prompt user to either quit or override when output already exists
    if "My_Mod" in outputContents:
        a = input("Output found in output folder. Would you like to overwrite it? (Y/N): ")
        if a.lower() != "y":
            programEnd()
        else:
            shutil.rmtree(".\\output\\My_Mod")

    copyCharFolders()
    for inputNum in range(len(inputContents)):
        print("Copying " + getInputFilename(inputNum) + "...")
        if os.path.isfile(getInputFilepath(inputNum)):   
            copyInputFile(inputNum)
        elif os.path.isdir(getInputFilepath(inputNum)):
            copyInputFolder(inputNum)
        print(getInputFilename(inputNum) + " copied successfully!")
    programEnd()


# copy empty character folders to output
def copyCharFolders():
    args = "robocopy .\\lib\\default_empty_taunt_folders .\\output\\My_Mod /e /xf * >nul"
    subprocess.run(args, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) # parameters hide output text


# copy file from input to animations folder of all slots for all characters.
def copyInputFile(inputNum):
    inputFilepath = getInputFilepath(inputNum)
    characterFolders = os.listdir(".\\output\\My_Mod\\fighter")
    for char in characterFolders:
        for i in range(0, 8):
            altNumberPath = ".\\output\\My_Mod\\fighter\\" + char + "\\motion\\body\\c0" + str(i) + "\\"
            args = "xcopy " + inputFilepath + " " + altNumberPath + " /s"
            subprocess.call(args, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) # parameters hide output text.


# Copy folder from input directly to character folders.
def copyInputFolder(inputNum):
    inputFilepath = getInputFilepath(inputNum)
    directory = os.listdir(".\\output\\My_Mod\\fighter")
    for char in directory:
        charPath = ".\\output\\My_Mod\\fighter\\" + char + "\\"
        args = "xcopy " + inputFilepath + " " + charPath + " /s"
        subprocess.call(args, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) # parameters hide output text.


# Return the Filename of the current input file.
def getInputFilename(inputNum):
    return os.listdir(".\\input")[inputNum]


# return the Filepath of the current input file.
def getInputFilepath(inputNum):
    f = os.path.join(".\\input", os.listdir(".\\input")[inputNum])
    return f


def programEnd():
    print("Press any key to close.")
    msvcrt.getch()
    quit()


main()