
new_dict = ([(333, [('ය', '.')]), (96, [('විය', '.')]), (88, [('.', 'මේ')]), (32, [('තිබේ', '.'), ('රජු', 'ගේ')]), (31, [('.', 'එහෙත්')]), (27, [('.', 'ඒ')]), (25, [('යි', '.'), ('ලදී', '.')]), (20, [('ගියේ', 'ය'), ('වේ', '.')])])

# print(new_dict[7])
# print(len(new_dict[7]))
# for tupel_item in new_dict:
#     for item in tupel_item:
#         print(item)


for tupel_item in new_dict:
    key = tupel_item[0]
    val = tupel_item[1]
    print(key)
    for item in val:
        print(item)