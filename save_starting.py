
fulllist = []
def getlist(singlelist):
    fullbook = ""
    for listitem in singlelist:
        for item in listitem:
            if item == "P":
                item = '<p>'
                print(item)
                fullbook = fullbook + item + " "
            elif item == 'NP':
                item = '</P>'
                fullbook = fullbook + item + " "
            elif item == 'S':
                item = '<h6>'
                fullbook = fullbook + item + " "
            elif item == 'NS':
                item = '</h6>'
                fullbook = fullbook + item + " "
            else:
                fullbook = fullbook + item + " "
    print(fullbook)

lines = [   ['P','මේ' ,'කවියත්' ,'ගන' ,'ඇති', 'සැටයි','NP'],
            ['P', 'පණ්ඩුවාස', 'රජු' ,'ගේ', 'ඇවෑ', 'මෙන්', 'ඔහු', 'පුත්' ,'අභය','කුමාරයා', 'රජ', 'බව'],
            ['ලංකාවේ', 'නියම', 'ඉතිහාසය', 'ආරම්භ', 'වන්නේ', 'ලංකාවාසීන්', 'බුදු', 'සමය', 'වැළදගත්'],
            ['ලද්දේ', 'දැයි', 'මෙහි', 'දී', 'ප‍්‍රශ්නයක්', 'නැහීය', 'හැකි', 'ය','.', 'ධර්මාශෝක', 'රජු', 'ගේ', 'බලය', 'ඉන්දියා', 'අර්ධද්වීපයේ','NP'],
            ['S','රජු' ,'සමගම්' ,'වැසියන්' ,'ගෙන්' ,'විශාල' ,'පිරිසක්' ,'ද' ,'බිද්ධාගම' ,'වැළද' ,'ගත්තෝ', 'ය','NS']
        ]

getlist(lines)