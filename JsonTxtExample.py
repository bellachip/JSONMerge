import csv
import json
import re


file = "data/6971761113_20181015141058.txt"
# def get_data(file):
#     with open(file, 'r') as reader:
#         raw = reader.read()
#     return raw
#
# raw = get_data(file)


# dictionary where the lines from
# text will be stored
dict1 = {}
command = ""
description = ""
c_line = ""
# creating dictionary
# f = open("newfile.txt", "w")
with open(file, 'r') as f:
    contents = f.read()
with open('newfile.txt', 'w') as w:
    w.write(contents.replace(',', '\n').replace('{', '{\n').replace('}', '\n}\n').replace('[', '').replace(']',''))

f.close()
w.close()



with open('newfile.txt', 'r') as f:
    raw = f.read().splitlines()





# A stack to hold the parsed objects
stack = [{}]

reader = csv.reader(raw, delimiter=':', skipinitialspace=True)

for row in reader:

    if len(row) == 0:


        continue

    if row[0] == '}' and len(stack) !=0:
    #     # The end of the current object
        stack.pop()
    #     continue
    val = row[-1]
    if val == '{':
        # A new subobject
        # d = []
        stack[-1][row[0]] = d = {}
        stack.append(d)
    else:
        # A line of plain data
        stack[-1][row[0]] = val

#
# Convert to JSON
out = json.dumps(stack[0], indent=4)
print(out)