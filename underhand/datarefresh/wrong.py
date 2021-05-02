can = open('datarefresh/source.txt', 'r')
shut = open('datarefresh/write.txt', 'w')
result = []
ident = 1
for stuff in can:
    if 'title' in stuff:
        result.append(stuff[10:-3])
    if '"optiontext":' in stuff:
        result.append(stuff[15:-3])
    if 'cultistequalsprisoner' in stuff:
        result.append(stuff[25])
    if "hasforesight" in stuff:
        result.append(stuff[16])
    if "candiscard" in stuff:
        result.append(stuff[14])
    if "numcards" in stuff:
        result.append(stuff[13])
    if "relic" in stuff:
        result.append(stuff[9])
    if "money" in stuff:
        result.append(stuff[9])
    if "cultist" in stuff:
        result.append(stuff[11])
    if "food" in stuff:
        result.append(stuff[8])
    if "prisoner" in stuff:
        result.append(stuff[12])
    if '''"suspicion":''' in stuff:
        result.append(stuff[13])
    if "iswin" in stuff:
        result.append(stuff[9:-2])
    if "islose" in stuff:
        result.append(stuff[10])
    if "cardartdone" in stuff:
        print(result)
        break
can.close()
shut.close()