import os, sys

# Open a file
path = "D:\Videos"
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print (file)