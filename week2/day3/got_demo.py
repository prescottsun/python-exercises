from pprint import pprint
from characters import characters
from houses import houses


count_A = 0
for character in characters:
    if character['name'][0] == 'A':
        count_A += 1
    # if character['name'].startswith('A') == True:
pprint('There are %s characters whose names start with A' % (count_A))

count_Z = 0
for character in characters:
    if character['name'][0] == 'Z':
        count_Z += 1
pprint('There are %s characters whose names start with Z' % (count_Z))

dead_characters = 0
for character in characters:
    if character['died'] != '':
        dead_characters += 1
pprint('There are %s dead characters' % (dead_characters))

most_titles_count = 0
most_titles_name = ''
for character in characters:
    if len(character['titles']) > most_titles_count:
        most_titles_count = len(character['titles'])
        most_titles_name = character['name']
pprint('%s has the most titles.' % (most_titles_name))


Valyrian_count = 0
for character in characters:
    if 'Valyrian' in character['culture']:
        Valyrian_count += 1
pprint('%s characters are Valyrian' % (Valyrian_count))

for character in characters:
    if character['name'] == 'Hot Pie':
        pprint('%s plays %s' % (character['playedBy'], character['name']))

not_in_show = 0
for character in characters:
    if character['tvSeries']:
        not_in_show += 1
pprint('%s characters are not in the TV show' % (not_in_show))


Targaryens = []
for character in characters:
    if 'Targaryen' in character['name']:
        Targaryens.append(character['name'])
# pprint(Targaryens)

print(houses.values)

for character in characters:

    for house in houses:
        houses_histogram = dict(house[allegiance] = )

    

    # print(len(house['swornMembers']))
# pprint(houses_histogram)

# pprint(len(characters))

# # print out the key names individually
# for k in jon_snow:
#    pprint(k)

# # print out just the values
# for key in jon_snow:
#    pprint(jon_snow[key])

# # print both the key and the value
# for k in characters.jon_snow:
#    pprint("%s: %s" % (k, jon_snow[k]))