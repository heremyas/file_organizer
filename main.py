# OBJECTIVES
# list files in a directory
# check files (folder or not)
# check extension name
# create directories based on their ext name
# move files to corresponding directory

from os import listdir, path, mkdir
import shutil

TARGET_DIR = "path/of/target/directory"

# list files and directories in a folder 
def listFiles(target_dir):
    files = listdir(target_dir)
    if("File Organizer.bat" in files):
        files.remove("File Organizer.bat")
        return files
    else:
        return files

# check files (folder or not)
def checkFile(target_dir):
    folders = []
    files = []
    files_list = listFiles(target_dir)

    for i in files_list:
        try:
            listFiles(path.join(target_dir, i))
            folders.append(i)
        except:
            files.append(i)
    
    return {"folders": folders, "files": files}

# check extension name (make them unique)
def checkExt(target_dir):
    ext_list = []
    files_list = checkFile(target_dir)["files"]
    for i in files_list:
        ext_list.append(i.split('.')[-1])

    filtered_ext = list(dict.fromkeys(ext_list))
    return filtered_ext

# create directory
def createDirectories(target_dir):
    for i in checkExt(target_dir):
        try:
            mkdir(path.join(target_dir, i))
            print(f"Folder {i} Created")
        except:
            print(f"Folder {i} exist")

# modve files to target directory
def moveFilesToDir(target_dir):
    file_list = checkFile(target_dir)['files']
    if file_list:
        try:
            for i in range(len(file_list)):
                ext_name = file_list[i].split('.')[-1]
                source = path.join(target_dir, file_list[i])
                target = path.join(target_dir, ext_name)
                shutil.move(source, target)
                print(f"File {file_list[i]} moved to {ext_name}")
        except Exception as e:
            print("Error moving files:", e)
        print("File Organization Successful!")
    else:
        print("Files organized")

def main(target_dir):
    createDirectories(target_dir)
    moveFilesToDir(target_dir)
    if (input("Press Enter to Exit... ") == ""):
        quit()

if __name__ == '__main__':
    main(TARGET_DIR)
