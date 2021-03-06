# backup to zip

import zipfile, os
def backupToZip(folder):
# Backup the entire contents of the folder in to a zip file

    folder = os.path.abspath(folder)  # Making sure folder is absolute

# Figure out the filename this program should use based on what file exist already
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

# Create the zip file
    print(f'Creating {zipFilename}..........')
    backupZip = zipfile.ZipFile(zipFilename,'w')

# Walk the entire folder tree and compress the files in each folder 
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}.......')
# Add the current folder to the Zip files 
        backupZip.write(foldername)

# Add all files in this folder to the Zip files 
    for filename in filenames:
        newBase = os.path.basename(folder) + '_'
        if filename.startswith(newBase) and filename.endswith('.zip'):
            continue        # don't back up the backup Zip files
        backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done')

backupToZip('C:\\Users\\Georgee\\delicious')