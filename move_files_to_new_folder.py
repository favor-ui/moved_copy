# import shutil
# import os

# source = "/parent/subdir"
# destination = "/parent/"
# files_list = os.listdir(source)
# for files in files_list:
#     shutil.move(files, destination)



# import os
# import glob
# import shutil
 
# source = '/Users/favor/Downloads/moved/naija'
# destination = '/Users/favor/Downloads/moved/desti'
# #
# # gather all files
# allfiles = glob.glob(os.path.join(source, '*.pdf'), recursive=True)
# print("Files to move", allfiles)

# # iterate on all files to move them to destination folder
# for file_path in allfiles:
#     dst_path = os.path.join(destination, os.path.basename(file_path))
#     shutil.move(file_path, dst_path)
#     print(f"Moved {file_path} -> {dst_path}")


# worked
import shutil
import os

# source = 'path to folder'

def recursive_copy(path):

    for f in sorted(os.listdir(os.path.join(os.getcwd(), path))):
        file = os.path.join(path, f)
        if os.path.isfile(file):
            temp = os.path.split(path)
            f_name = '_'.join(temp)
            file_name = f_name + '_' + f
            # file_name = f_name
            shutil.move(file, file_name)
        else:
            recursive_copy(file)

source = '/Users/favor/Downloads/moved_copy/sample_text'
recursive_copy(source)



