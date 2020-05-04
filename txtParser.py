import csv
import json
import re
from pathlib import Path


filedate = "20181015"



def readfile(file, str=""):
    stack = []
    with open(file, 'r') as r:
        for lines in r:
            str = json.loads(lines)
            stack.append(str)

    return stack


def extract_values(obj, key):
    # """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        # """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results


#for all cursor in jasondata, get all the nodes in the responses of current cursor
def ignore_cursor_getall_nodes_responses(json_data, filename):
    j = 0
    arr = []
    # print(len(json_data))
    print(len(json_data[0]['response']))
    print(len(json_data[1]['response']))
    print(len(json_data[2]['response']))
    print(len(json_data))
    file = re.split(r'[_.]', filename)[1]

    for i in range(len(json_data)):  # 4
        json_data = json_data[i]['response'] #gets all the nodes in the responses does it for each cursor

        for node in json_data:
            node['TimeStamp'] = int(file) #

        # print(json_data)

        # for j in range(len(json_data[i]['response'])):
        #
        #     arr.append(json_data[i]['response'][j])
        return json_data  # returns array for array with all nodes


def id_checker(id, array2):
    if id in array2:
        return True
    else:
        return False


def check_for_duplicate(array_nodes_one, array_nodes_two): #all nodes are list in passed in
    # if len(array_nodes_one) < len(array_nodes_two):
    #     print("hello")
    array_of_id_two = []
    stack =[]
    #
    for nodes in array_nodes_one:
        for nodes_two in array_nodes_two:

            if nodes['id'] == nodes_two['id']:
                #remove check the time same
                if nodes['TimeStamp'] > nodes_two['TimeStamp']:
                    #append to stack
                    stack.append(nodes)
                    print(nodes['id'])
                    print(nodes['TimeStamp'])
                elif nodes['TimeStamp'] < nodes_two['TimeStamp']:
                    print(nodes['id'])
                    print(nodes['TimeStamp'])
                    stack.append(nodes_two)

            else:
                print("hello")

                stack.append(nodes)
                stack.append(nodes_two)
    return stack

    # id_1 = {one['id'] for one in array_nodes_one}
    # id_2 = {two['id'] for two in array_nodes_two}
    # print(id_1)
    # print(id_2)
    # matched_keys = set(id_1) & set(id_2)
    #
    #
    # if len(array_nodes_two + array_nodes_one) == len(matched_keys):
    #     print("True")
    # else:
    #     print("false")
    # # result = {key: (id_1[key], id_2[key]) for key in matched_keys}
    # # print(result)
    # print(matched_keys)
    # return matched_keys


# def check_for_dup(final_node_list):
#
#     for items in final_node_list:
#
#     # return len(final_node_list) != len(set(final_node_list))
#         # true
#     # for node in final_node_list:
#     #     if node['id']



    # for i in range(len(array_nodes_two)): #iterate through all ndoes
    #     array_of_id_two.append(array_nodes_two[i]['id'])
    #
    #
    # # print(array_of_id_two)
    #
    # for j in range(len(array_nodes_one)):
    #     array_node_id = array_nodes_one[j]['id']
    #     Time = array_nodes_one[j]['TimeStamp']
    #     indexOf(array_nodes_two[1]['id'])
    #     if id_checker(array_node_id, array_of_id_two):
    #         #check for timestpame
    #
    #         return array_node_id, array_nodes_one[j], Time, i , j


# def replace_with_current_id(array_nodes_one, array_nodes_two):
#     id_one, array_nodes_current, date, index_i_two, index_j_one  = check_for_duplicate(array_nodes_one, array_nodes_two)
#
#     # array_node_id = array_nodes_two[index_j_one]['id']
#     array_node_id = array_nodes_one[index_j_one]['id']
#     Time = array_nodes_two[i]['TimeStamp']
#     if date_node_one >



def main():
    a_filename = "data/6971761113_20181015141058.txt"
    b_filename = "data/6971761113_20181015151911.txt"
    json_data_one = readfile(a_filename) #array of cursor dictionaries
    # print(json_data_one)
    json_data_two = readfile(b_filename)
    # print(json_data_two)
    array_nodes_one = ignore_cursor_getall_nodes_responses(json_data_one, a_filename) #gets a list of all nodes in a list

    print("\n\n\n\n\n\n")
    array_nodes_two = ignore_cursor_getall_nodes_responses(json_data_two, b_filename)


    final_stack = check_for_duplicate(array_nodes_one, array_nodes_two)
    with open("newjson.json", 'w') as newjson:

        json.dump(final_stack, newjson)
        # # print(check_for_dup(final_stack))

    newjson.close()



    with open ("newtxt.txt", 'w') as newtxt:
        newtxt.write(str(final_stack))
    # # print(check_for_dup(final_stack))

    newtxt.close()
    # print(is_check)


main()

# print(array_nodes_one[0]['editableUntil'])
# authors = extract_values(json_data[0], 'username')


# id = extract_values(json_data, 'dislikes')


# cursor = json_data['cursor']
#
# # print(cursor)
# # print(id)
# cursor = extract_values(json_data, 'editable')


# for key in json_data.keys():
#     print(key)

# {"editableUntil": "2018-10-22T18:01:22",
#  "dislikes": 0,
#  "numReports": 0,
#  "likes": 0,
#  "message": "<p>You can read? aw shucks.</p>",
#  "id": "4146297139",
#  "createdAt": "2018-10-15T18:01:22",
#  "author":
#      {
#          "username": "carriebarber",
#          "about": "",
#          "name": "Carrie Barber",
#          "disable3rdPartyTrackers": false,
#          "isPowerContributor": false,
#          "joinedAt": "2013-07-05T15:34:46",
#          "profileUrl": "https://disqus.com/by/carriebarber/",
#          "url": "",
#          "location": "",
#          "isPrivate": true,
#          "signedUrl": "",
#          "isPrimary": true,
#          "isAnonymous": false,
#          "id": "60816887",
#          "avatar":
#              {
#                  "small":
#                      {
#                          "permalink": "https://disqus.com/api/users/avatars/carriebarber.jpg",
#                          "cache": "https://c.disquscdn.com/uploads/users/6081/6887/avatar32.jpg?1485236270"
#                      },
#                  "isCustom": true,
#                  "permalink": "https://disqus.com/api/users/avatars/carriebarber.jpg",
#                  "cache": "https://c.disquscdn.com/uploads/users/6081/6887/avatar92.jpg?1485236270",
#                  "large":
#                      {
#                          "permalink": "https://disqus.com/api/users/avatars/carriebarber.jpg",
#                          "cache": "https://c.disquscdn.com/uploads/users/6081/6887/avatar92.jpg?1485236270"
#                      }
#              }
#      },
#  "media": [],
#  "isSpam": false,
#  "isDeletedByAuthor": false,
#  "isDeleted": false,
#  "parent": 4146150478,
#  "isApproved": true,
#  "isFlagged": false,
#  "raw_message": "You can read? aw shucks.",
#  "isHighlighited": false,
#  "canVote": false,
#  "thread": "6971761113",
#  "forum": "thehill-v4",
#  "points": 0,
#  "moderationLabels": [],
#  "isEdited": false,
#  "sb": false
#  }
