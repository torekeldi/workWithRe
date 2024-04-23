import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts = list(rows)
    headers = contacts.pop(0)

contacts_name = []
for data in contacts:
    name_str = ' '.join(data[0:3])
    name_list = name_str.split()
    data[0] = name_list[0]
    data[1] = name_list[1]
    try:
        data[2] = name_list[2]
    except:
        data[2] = ''
    contacts_name.append(data)

names = list(set([x[0]+x[1] for x in contacts_name]))
same_names = []
for name in names:
    same_name = []
    for data in contacts_name:
        if data[0]+data[1] == name:
            same_name.append(data)
    same_names.append(same_name)

unique_names = []
for data in same_names:
    # print(data[0][0])
    unique_name = ['', '', '', '', '', '', '']
    if len(data) > 1:
        unique_name[0] = max([data[0][0], data[1][0]])
        unique_name[1] = max([data[0][1], data[1][1]])
        unique_name[2] = max([data[0][2], data[1][2]])
        unique_name[3] = max([data[0][3], data[1][3]])
        unique_name[4] = max([data[0][4], data[1][4]])
        unique_name[5] = max([data[0][5], data[1][5]])
        unique_name[6] = max([data[0][6], data[1][6]])
    else:
        unique_name[0] = data[0][0]
        unique_name[1] = data[0][1]
        unique_name[2] = data[0][2]
        unique_name[3] = data[0][3]
        unique_name[4] = data[0][4]
        unique_name[5] = data[0][5]
        unique_name[6] = data[0][6]
    unique_names.append(unique_name)

pattern = r"((\+7|8))\s*\(*(\d{1,3})[\)|-]*\s*(\d{1,3})-*(\d{1,2})-*(\d{1,2})\s*\(*(доб. )*(\d*)\)*"
for idx, data in enumerate(unique_names):
    result = re.search(pattern, data[5])
    if result.group(7):
        re_sub = re.sub(pattern, r"+7(\3)\4-\5-\6 доб.\8", data[5])
    else:
        re_sub = re.sub(pattern, r"+7(\3)\4-\5-\6", data[5])
    unique_names[idx][5] = re_sub

unique_names.insert(0, headers)
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(unique_names)
