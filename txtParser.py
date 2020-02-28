import csv
import json
import re
from pathlib import Path

stack = []
filedate = "20181015"

a_filename = "data/6971761113_20181015141058.txt"
b_filename = "data/6971761113_20181015144051.txt"

def readfile(file, str=""):
    with open(file, 'r') as r:
        for lines in r:
            str = json.loads(lines)


            print(str)
            stack.append(str)

    # print(data)
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


def ignore_cursor_getall_nodes_responses(json_data):
    j = 0
    arr = []
    # print(len(json_data))
    print(len(json_data[0]['response']))
    print(len(json_data[1]['response']))
    print(len(json_data[2]['response']))
    file = re.split(r'[_.]', a_filename)[1]
    print(json_data)
    for i in range(len(json_data)):  # 4
        print(len(json_data[i]))
        for j in range(len(json_data[i]['response'])):

            arr.append(json_data[i]['response'][j])

        return arr  # returns array for array with all nodes


def id_checker(id, array2):
    if id in array2:
        return True
    else:
        return False


def check_for_duplicate(array_nodes_one, array_nodes_two):
    # if len(array_nodes_one) < len(array_nodes_two):
    #     print("hello")
    array_of_id_two = []

    for i in range(len(array_nodes_two)):
        array_of_id_two.append(array_nodes_two[i]['id'])

    # print(array_of_id_two)

    for i in range(len(array_nodes_one)):
        array_node_id = array_nodes_one[i]['id']
        if id_checker(array_node_id, array_of_id_two):
            return array_node_id, array_nodes_one[i]


def replace_with_current_id(array_nodes_one, array_nodes_two, date):
    id_one, array_nodes_one = check_for_duplicate(array_nodes_one, array_nodes_two)
    print(id_one)
    print(array_nodes_one)


def main():
    json_data_one = readfile("data/6971761113_20181015141058.txt")
    json_data_two = readfile("data/6971761113_20181015144051.txt")
    array_nodes_one = ignore_cursor_getall_nodes_responses(json_data_one)
    array_nodes_two = ignore_cursor_getall_nodes_responses(json_data_two)
    is_check = check_for_duplicate(array_nodes_one, array_nodes_two)
    print(is_check)


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
