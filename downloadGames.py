import berserk
client = berserk.Client()

username = input("lichess username: ")
games = client.games.export_by_player(username, opening=True)
games = list(games)

writer = open('games.txt', 'w', encoding='utf-8')
writer.write('color, winner, opening\n')
for game in games:
    if game['variant'] != 'standard':
        continue
    if game['status'] == 'noStart':
        continue
    
    if game['players']['white']['user']['name'] == username:
        writer.write('white,')
    else:
        writer.write('black,')
    
    if 'winner' in game:
        writer.write(game['winner'])
    else:
        writer.write('draw')
    writer.write(',')

    writer.write(game['opening']['name'])
    writer.write('\n')


writer.close()