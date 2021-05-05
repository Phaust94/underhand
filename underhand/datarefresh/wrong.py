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
    middleman = middleman.replace(' ', '_')
    middleman = middleman.upper()
    result[1] = middleman
    if result[19] == 0:
        result[19] = False
    if result[19] == 1:
        result[19] = True
    if result[37] == 0:
        result[37] = False
    if result[37] == 1:
        result[37] = True
    if result[5] == 0:
        result[5] = 'NoForesight'
    if result[5] == 1:
        result[5] = 'Foresight'
    if result[5] == 2:
        result[5] = 'ForesightWithDiscard'
    if result[22] == 0:
        result[22] = 'NoForesight'
    if result[22] == 1:
        result[22] = 'Foresight'
    if result[22] == 2:
        result[22] = 'ForesightWithDiscard'
    if result[40] == 0:
        result[40] = 'NoForesight'
    if result[40] == 1:
        result[40] = 'Foresight'
    if result[40] == 2:
        result[40] = 'ForesightWithDiscard'
    if result[18] == '':
        result[18] = 'NoWin'
    if result[18] == 'God of Beginnings':
        result[18] = 'GodOfBeginnings'
    if result[18] == 'Rhybaax':
        result[18] = 'Rhybaax'
    if result[18] == "Jhai'lungr":
        result[18] = 'JhaiLungr'
    if result[18] == 'Kekujira':
        result[18] = 'Kekujira'
    if result[18] == 'Yacare':
        result[18] = 'Yacare'
    if result[18] == "Uhl'uht'c":
        result[18] = 'UhlUhtC'
    if result[36] == '':
        result[36] = 'NoWin'
    if result[36] == 'God of Beginnings':
        result[36] = 'GodOfBeginnings'
    if result[36] == 'Rhybaax':
        result[36] = 'Rhybaax'
    if result[36] == "Jhai'lungr":
        result[36] = 'JhaiLungr'
    if result[36] == 'Kekujira':
        result[36] = 'Kekujira'
    if result[36] == 'Yacare':
        result[36] = 'Yacare'
    if result[36] == "Uhl'uht'c":
        result[36] = 'UhlUhtC'
    if result[54] == '':
        result[54] = 'NoWin'
    if result[54] == 'God of Beginnings':
        result[54] = 'GodOfBeginnings'
    if result[54] == 'Rhybaax':
        result[54] = 'Rhybaax'
    if result[54] == "Jhai'lungr":
        result[54] = 'JhaiLungr'
    if result[54] == 'Kekujira':
        result[54] = 'Kekujira'
    if result[54] == 'Yacare':
        result[54] = 'Yacare'
    if result[54] == "Uhl'uht'c":
        result[54] = 'UhlUhtC'

    shut.write(f'''
{result[1]} = EventCard(
    {result[0]},
    {result[5]},
    CardTier.Regular,
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
            foresight=Foresight.{result[5]}
            Win.{result[18]}
            lose_game={result[19]}
        ),
        CardOption(
            {result[20]},
            resources_required=ResourceList.from_resources(
                ResourceAmount(Resource.Relic, {result[24]}),
                ResourceAmount(Resource.Money, {result[25]}),
                ResourceAmount(Resource.Cultist, {result[26]}),
                ResourceAmount(Resource.Food, {result[27]}),
                ResourceAmount(Resource.Prisoner, {result[28]}),
                ResourceAmount(Resource.Suspicion, {result[29]}),
                ResourceAmount(Resource.Cultist | Resource.Prisoner, {result[21]}),
            ),
            resources_received=ResourceList.from_resources(
                ResourceAmount(Resource.Relic, {result[30]}),
                ResourceAmount(Resource.Money, {result[31]}),
                ResourceAmount(Resource.Cultist, {result[32]}),
                ResourceAmount(Resource.Food, {result[33]}),
                ResourceAmount(Resource.Prisoner, {result[34]}),
                ResourceAmount(Resource.Suspicion, {result[35]}),
            )
            foresight=Foresight.{result[22]}
            win_game=Win.{result[36]}
            lose_game={result[37]}
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
                ResourceAmount(Resource.Cultist | Resource.Prisoner, {result[39]}),
            ),
            resources_received=ResourceList.from_resources(
                ResourceAmount(Resource.Relic, {result[48]}),
                ResourceAmount(Resource.Money, {result[49]}),
                ResourceAmount(Resource.Cultist, {result[50]}),
                ResourceAmount(Resource.Food, {result[51]}),
                ResourceAmount(Resource.Prisoner, {result[52]}),
                ResourceAmount(Resource.Suspicion, {result[53]}),
            )
            foresight=Foresight.{result[40]}
            win_game=Win.{result[54]}
            lose_game={result[55]}
        ),
    ]
)''')
    break

print(result)
shut.close()
