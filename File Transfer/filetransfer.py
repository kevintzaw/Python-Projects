import shutil
import os
import schedule
import time

#set where the source of the files are
source = '/Users/kevinzaw/Documents/GitHub/Python Projects/File Transfer/Folder A/'

#set the destinatin path to folderB
destination = '/Users/kevinzaw/Documents/GitHub/Python Projects/File Transfer/Folder B/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
