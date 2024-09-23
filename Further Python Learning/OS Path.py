#THE OS AND IO PATHS

#os path allows you to find, create, manage, delete, and maintain different folders

#io path allows you read from and write to files

#MODULES AND PACKAGES

#module is another name for a single .py file with python code

#package is a folder that can contain multiple python modules

#IMPORT

#import is used to load other python source code files into your current code page

#to access other folders import io path

import os

os.path.adventure() #allows us to use the function named adventure in our current code that is in the path module 

#os.path.isfile() specfies if a file exists or not and will return as a boolean

variablename = os.path.isfile("C:\\Users\owl.png")
print(variablename)

#assume the file owl doesnt exist, it will print out False

#os.path.isdir() specifies whether a directory exists or not and will return with boolean

variablename = os.path.isdir("C:\\Users") #assumption that the directory does exists and is on a drive called C
print(variablename)

#os.path.remove() will remove a file from the directory

os.path.remove("C:\\Users\owl.png") #removes the file named owl

#os.path.basename() will return the basename of the file (just the file and the extension ex. weather.doc would be a basename)
variablename = os.path.basename("/squirrel/elephant.png")
print(variablename) #prints out elephant.png

#os.path.dirname() gives us directory name where the folder or file is located
variablename = os.path.dirname("/squirrel/elephant.png")
print(variablename) #prints out squirrel

#sys.path() allows you to access a list of directories that are automatically created when starting a python file

import sys
sys.path 
#can also display error messages that would not otherwise show
