from resume_parser import resumeparse

import os
from os import chdir, getcwd, listdir, path
import codecs
import re
import csv


def check_path(folder_path):
    ''' (str) -> str
    Verifies if the provided absolute path does exist.
    '''
    # abs_path = raw_input(prompt)
    isdir = os.path.isdir(folder_path)
    while isdir != True:
        print("\nThe specified path does not exist.\n")
    return  folder_path

# print "\n"

directory = check_path("/Users/favor/Downloads/moved/triamtex")

list=[]
for root,dirs,files in os.walk(directory):
    # print(files)
    for filename in files:
        if filename.endswith('.txt'):
            text = os.path.join(directory,filename)
            list.append(text)

# m=len(list)

# print(list)
i=0
all_data = []
while i<=len(list):
# for i in range(len(list)):

    # with while loop
    path=list[i-1]
    head, tail = os.path.split(path)

    # with for loop
    # path=list[i]
    # head, tail = os.path.split(list[i])

    # this will remove all special characters
    # applicant_name = re.findall(r"[\w']+", tail)
    applicant_name = tail.replace('\\', ' ').replace('.', ' ').split()
    applicantname = applicant_name[-2]

    # data = {'values': 678, 'values2': 167, 'values6': 998}
    data = resumeparse.read_file(path)
    data['filename'] = applicantname
    print(data)
    all_data.append(data)
    i+=1


# write list of dictionary to csv
keys = all_data[0].keys()
with open('people.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_data)




    

    