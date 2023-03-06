import shutil
import datetime 
import os
import sys

distination_directry='Dat '+datetime.datetime.now().strftime("(%d-%m-%y)")

from_dec="D:/Data"
to_dec="G:/backup/Data "+datetime.datetime.now().strftime("(%d-%m-%y)")
drive_dir="H:/My Drive/TALLY_BACKUP/Data "+datetime.datetime.now().strftime("(%d-%m-%y)")

drive_file=os.path.exists(drive_dir)
file_exists=os.path.exists(to_dec)

driver_drive=os.path.exists('H:/My Drive')
local_drive=os.path.exists("G:/backup")
if driver_drive and local_drive:
    if file_exists:
        shutil.rmtree(to_dec)
        sys.stdout.write(to_dec+"Folder already found soo Removed\n")
        shutil.copytree(from_dec,to_dec,copy_function = shutil.copy)
        sys.stdout.write("saved locally successfully\n")
    else:
        sys.stdout.write("File not found in local drive so copying...\n")
        shutil.copytree(from_dec,to_dec,copy_function = shutil.copy)
        sys.stdout.write("copied in local successfully\n")   
    if drive_file:
        shutil.rmtree(drive_dir)
        sys.stdout.write(drive_dir+"Folder already found soo Removed\n")
        shutil.copytree(from_dec,drive_dir,copy_function=shutil.copy)
        sys.stdout.write("copied in drive successfully\n")   
    else:       
        sys.stdout.write("File not found in drive so copying...\n")
        shutil.copytree(from_dec,drive_dir,copy_function=shutil.copy)
        sys.stdout.write("Created in Drive successfully\n")
else:
    sys.stdout.write("No such directory, please contact ADMIN")
#q=shutil.make_archive(distination_directry,"zip",root_dir=from_dec,base_dir="G:/backup")
#print(q)
sys.stdout.write("saved to both directory\n")
input("press any enter key to close\n")