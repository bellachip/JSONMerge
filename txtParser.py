import pandas
import json
import re

# the file to be converted to
# json format
a_filename = 'data\\6971761113_20181015141058.txt'
b_filename = 'btest.txt'

# dictionary where the lines from
# text will be stored
dict1 = {}
command = ""
description = ""
c_line = ""
# creating dictionary
# f = open("newfile.txt", "w")
with open(a_filename) as fh:
    for line in fh:
    #     # reads each line and trims of extra the spaces
    #     # and gives only the valid words
    #
    #     x = re.search(".*,$", line)
    #     y = re.search("^{", line)
    #     z = re.search("^}", line)
    #     r = re.search("^}.*,$", line)

        print(line)

#         if r:
#             continue
#             # c_line = line[:len(line)-2]
#             # print(c_line)
#
#         if y or z:
#             # c_line=line[]
#             # print(c_line)
#             continue
#
#         if x and not z:
#             c_line = line[:len(line) - 2]
#
#             f.write(c_line + "\n")
#
#             print(c_line)
#
#             # command, description = c_line.strip().split(None, 1)
#             # print(c_line)
#
# f.close()
#
#
