getdata = {'ගන': ['ගන', 'ගත', 'ගහ', 'ගණ', 'කන', 'කහ', 'කණ', 'හන', 'හත', 'ශතන', 'වන', 'ගී', 'ගත', 'ගෙ', 'ගණ', 'ඌන', 'හන', 'එන', 'ඕන', 'ඝන', 'ගඳ'], 'සැටයි': ['යැමයි', 'යාමයි', 'පාමසිසැටි', 'තැටි', 'සිටි', 'සෙයි', 'ගැටය', 'සැලි', 'ජැටි', 'මැයි', 'සායි', 'සැළය', 'යැයි', 'දැයි'], 'නයම': ['කයට', 'ගසට', 'ණයටනය', 'නම', 'නාම', 'එයම', 'නිම', 'නයන', 'තම', 'එය', 'නෑ', 'යූ', 'නො', 'ණය']}

fulllist = ['p', 'මේ', 'කවියත්', 'ගන', 'ඇති', 'සැටයි', 'p', 'p', 'නයම', 'ඉස', 'බුදු', 'සමය']
print(fulllist)

# for n, i in enumerate(fulllist):
#     if i == 'ගන':
#         fulllist[n] = 'සැටයිකවියත්'
#
# print(fulllist)
# for item in fulllist:
#     for key in getdata:
#         if item == getdata:
#             item = getdata[key][0]
#
# print(fulllist)


for n, i in enumerate(fulllist):
    for key in getdata:
        if i==key:
            fulllist[n] = getdata[key][0]

print(fulllist)