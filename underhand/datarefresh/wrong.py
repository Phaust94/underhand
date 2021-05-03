import json
with open('datarefresh/source.txt', 'r') as source:
    can = json.load(source)
shut = open('datarefresh/write.txt', 'w')
result = []

for card_id, card in can.items():
    result.append(card_id)
    result.append(card["title"])
    result.append(card["option1"]["optiontext"])
    result.append(card["option1"]["cultistequalsprisoner"])
    result.append(int(card["option1"]["foresight"]["hasforesight"]) + int(card["option1"]["foresight"]["candiscard"]))
    result.append(int(card["option1"]["shuffle"]["numcards"]) + 1)
    result.append(card["option1"]["requirements"]["relic"])
    result.append(card["option1"]["requirements"]["money"])
    result.append(card["option1"]["requirements"]["cultist"])
    result.append(card["option1"]["requirements"]["food"])
    result.append(card["option1"]["requirements"]["prisoner"])
    result.append(card["option1"]["requirements"]["suspicion"])
    result.append(card["option1"]["rewards"]["relic"])
    result.append(card["option1"]["rewards"]["money"])
    result.append(card["option1"]["rewards"]["cultist"])
    result.append(card["option1"]["rewards"]["food"])
    result.append(card["option1"]["rewards"]["prisoner"])
    result.append(card["option1"]["rewards"]["suspicion"])
    result.append(card["option1"]["iswin"])
    result.append(card["option1"]["islose"])
    result.append(card["option2"]["optiontext"])
    result.append(card["option2"]["cultistequalsprisoner"])
    result.append(int(card["option2"]["foresight"]["hasforesight"]) + int(card["option2"]["foresight"]["candiscard"]))
    result.append(int(card["option2"]["shuffle"]["numcards"]) + 1)
    result.append(card["option2"]["requirements"]["relic"])
    result.append(card["option2"]["requirements"]["money"])
    result.append(card["option2"]["requirements"]["cultist"])
    result.append(card["option2"]["requirements"]["food"])
    result.append(card["option2"]["requirements"]["prisoner"])
    result.append(card["option2"]["requirements"]["suspicion"])
    result.append(card["option2"]["rewards"]["relic"])
    result.append(card["option2"]["rewards"]["money"])
    result.append(card["option2"]["rewards"]["cultist"])
    result.append(card["option2"]["rewards"]["food"])
    result.append(card["option2"]["rewards"]["prisoner"])
    result.append(card["option2"]["rewards"]["suspicion"])
    result.append(card["option2"]["iswin"])
    result.append(card["option2"]["islose"])
    result.append(card["option3"]["optiontext"])
    result.append(card["option3"]["cultistequalsprisoner"])
    result.append(int(card["option3"]["foresight"]["hasforesight"]) + int(card["option3"]["foresight"]["candiscard"]))
    result.append(int(card["option3"]["shuffle"]["numcards"]) + 1)
    result.append(card["option3"]["requirements"]["relic"])
    result.append(card["option3"]["requirements"]["money"])
    result.append(card["option3"]["requirements"]["cultist"])
    result.append(card["option3"]["requirements"]["food"])
    result.append(card["option3"]["requirements"]["prisoner"])
    result.append(card["option3"]["requirements"]["suspicion"])
    result.append(card["option3"]["rewards"]["relic"])
    result.append(card["option3"]["rewards"]["money"])
    result.append(card["option3"]["rewards"]["cultist"])
    result.append(card["option3"]["rewards"]["food"])
    result.append(card["option3"]["rewards"]["prisoner"])
    result.append(card["option3"]["rewards"]["suspicion"])
    result.append(card["option3"]["iswin"])
    result.append(card["option3"]["islose"])

    middleman = str(result[1])
    middleman.replace(' ', '_')
    middleman.upper()
    result[1] = middleman
    if result[19] == 0:
        result[19] = False
    if result[19] == 1:
        result[19] = True
    if result[37] == 0:
        result[37] = False
    if result[37] == 1:
        result[37] = True

    shut.write(f'''
{result[1]} = EventCard(
    {result[0]},
    {result[5]},
    'card',
    [
        CardOption(
            {result[2]},
            resources_required=ResourceList.from_resources(
                ResourceAmount(Resource.Relic, {result[6]}),
                ResourceAmount(Resource.Money, {result[7]}),
                ResourceAmount(Resource.Cultist, {result[8]}),
                ResourceAmount(Resource.Food, {result[9]}),
                ResourceAmount(Resource.Prisoner, {result[10]}),
                ResourceAmount(Resource.Suspicion, {result[11]}),
                ResourceAmount(Resource.Cultist | Resource.Prisoner, {result[3]}),
            ),
            resources_received=ResourceList.from_resources(
                ResourceAmount(Resource.Relic, {result[12]}),
                ResourceAmount(Resource.Money, {result[13]}),
                ResourceAmount(Resource.Cultist, {result[14]}),
                ResourceAmount(Resource.Food, {result[15]}),
                ResourceAmount(Resource.Prisoner, {result[16]}),
                ResourceAmount(Resource.Suspicion, {result[17]}),
                
            )
            foresight={result[5]}
            win_game={result[18]}
            lose_game={result[19]}
        ),
        CardOption(
            {result[38]},
            resources_required=ResourceList.from_resources(
                ResourceAmount(Resource.Relic, {result[42]}),
                ResourceAmount(Resource.Money, {result[43]}),
                ResourceAmount(Resource.Cultist, {result[44]}),
                ResourceAmount(Resource.Food, {result[45]}),
                ResourceAmount(Resource.Prisoner, {result[46]}),
                ResourceAmount(Resource.Suspicion, {result[47]}),
            ),
            resources_received=ResourceList.from_resources(
                ResourceAmount(Resource.Relic, {result[48]}),
                ResourceAmount(Resource.Money, {result[49]}),
                ResourceAmount(Resource.Cultist, {result[50]}),
                ResourceAmount(Resource.Food, {result[51]}),
                ResourceAmount(Resource.Prisoner, {result[52]}),
                ResourceAmount(Resource.Suspicion, {result[53]}),
                ResourceAmount(Resource.Cultist | Resource.Prisoner, {result[21]}),
            )
            foresight={result[22]}
            win_game={result[36]}
            lose_game={result[37]}
        ),
        CardOption("Decline to Trade"),
    ]
)''')
    break

print(result)
shut.close()
