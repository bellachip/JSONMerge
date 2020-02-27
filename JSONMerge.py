import pandas
import json
import re

# the file to be converted to
# json format
a_filename = 'data\\6971761113_20181015144051.txt'
b_filename = 'btest.txt'

# dictionary where the lines from
# text will be stored
dict1 = {}
command = ""
description = ""
c_line = ""
# creating dictionary
f = open("newfile.txt", "w")
with open(a_filename) as fh:
    for line in fh:
        # reads each line and trims of extra the spaces
        # and gives only the valid words

        x = re.search(".*,$", line)
        y = re.search("^{", line)
        z = re.search("^}", line)
        r = re.search("^}.*,$", line)
        if r:
            continue
            # c_line = line[:len(line)-2]
            # print(c_line)

        if y or z:
            # c_line=line[]
            # print(c_line)
            continue

        if x and not z:
            c_line = line[:len(line) - 2]

            f.write(c_line + "\n")

            # command, description = c_line.strip().split(None, 1)
            # print(c_line)
f.close()


# def line_to_dict(split_Line):
#     # Assumes that the first ':' in a line
#     # is always the key:value separator
#
#     line_dict = {}
#     for part in split_Line:
#         key, value = part.split(":", maxsplit=1)
#         line_dict[key] = value
#
#     return line_dict

def convert():
    f = open("newfile.txt", "r")
    content = f.read()
    splitcontent = content.splitlines()  # array that spearates each row of data

    print(splitcontent)
    print("\n")

    # Split each line by pipe
    lines = [line.split('":') for line in splitcontent]  # array of an array of splited by key and value

    print(lines)
    print("\n")
    #
    # # Convert each line to dict

    # lines = [line_to_dict(l) for l in lines]
    i = 0
    sp = []
    # [l[0].strip('"') for l in lines]

    for l in lines:  # for each array in lines array
        sp = l
        word = sp[0].strip('"')  # strip the awkward comma on the first element of the row

        print(word)
        sp[0] = word
        print(sp[0])
        if re.search("true", sp[1]):
            sp[1] = True
        if re.search("false", sp[1]):
            sp[1] = False
        if re.search(r"\"\[.+\]\"", sp[1]):
            print("true")
            sp[1].strip('"')

    key = dict(line for line in lines)
    print(key)

    print(json.dumps(key, indent=2, sort_keys=True))

    # print(sp[0].strip('"'))

    print("\n")

    # Output JSON
    # with open("ajson.json", 'w') as fout:
    #     json.dump(lines, fout, indent=4)


convert()

# elif z:
#     c_line = line[:1]
#     print()
# command, description = line.strip().split(None, 1)

# dict1[command] = description.strip()

# creating json file
# the JSON file is named as test1
# out_file = open("ajson.json", "w")
# json.dump(dict1, out_file, indent=4, sort_keys=False)
# out_file.close()
