import os
from os import chdir, getcwd, listdir, path
import codecs
# import pyPdf
from PyPDF2 import PdfFileReader, PdfFileWriter
import datetime
from time import gmtime, strftime

# check path
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

directory = check_path("/Users/favor/Downloads/moved_copy/sample_pdf")
# saved = check_path("/Users/favor/Downloads/moved/saved")


# sore files in a list
list=[]
for root,dirs,files in os.walk(directory):
    # print(files)
    for filename in files:
        if filename.endswith('.pdf'):
            new_file_name = os.path.join(directory,filename)
            list.append(new_file_name)

m=len(list)

# print(list)
i=0
while i<=len(list):

    path=list[i-1]
    
    # print(path)
    head,tail=os.path.split(path)
    
    # separator 
    var="\\"

    # create new filename
    tail=tail.replace(".pdf",".txt")
    new_filename=head+var+tail
    
    # terminate loop
    i+=1

    # read file with file reader
    fileReader = PdfFileReader(open(path,'rb'),strict=False)
    countpage = fileReader.getNumPages()
    count = 0
    text = []

    # Iterate pages
    while count < countpage:
        pageObj = fileReader.getPage(count)
        count +=1
        extracted_text = pageObj.extractText()
        text.append(extracted_text)

    # convert list to string
    content = ""
    for each in text:
        content += each
    
    # Alternative1 to convert list to string
    # content = ' '.join(map(str,text))

    # Alternative2 to convert list to string
    # content = ' '.join([str[item] for item in text])

    # write text to new file with extension as text
    f = open(new_filename,'w')
    f.write(content)
    f.close
    # terminate loop
    i+=1



# write dictionary to csv python
# with open('test6.csv', 'w') as f:
#     for key in data.keys():
#         f.write("%s, %s\n" % (key, data[key]))