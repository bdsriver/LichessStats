import csv
import displayFunctions

#find score, as in 0 for loss, 0.5 for draw, 1 for win
def find_score(game):

    if game.opening[0:5] == game.winner:
        #player won
        return 1
    
    elif game.winner == "draw":
        return 0.5
    
    else:
        return 0


class Game:
    def __init__(self, opening, winner):
        self.winner = winner
        self.opening = opening


csv_file = "games.txt"

data_reader = open(csv_file, 'r')
reader = csv.reader(data_reader, delimiter = ',' )

games = []

#pull the list of games
for row in reader:
    #skip the first row
    if row[0] == "color":
        continue

    #player color: opening played, winner (respectively)
    games.append(Game( (row[0]+ ': ' + row[2]) ,row[1]))
    

data_reader.close()

#corresponding data has the same index
openings = []
records = []#in the format: w-l-d

#each opening can have 2 instances in the array, one for playing as each color
#add the opening and record the result if it is not in the array
#if it is already there only put the result

for g in games:
    if g.opening not in openings:
        openings.append(g.opening)

        #add appropriate record
        score = find_score(g)
        if score == 1:
            records.append([1,0,0])
        elif score == 0.5:
            records.append([0,0,1])
        else:
            records.append([0,1,0])
    
    else:
        #if the opening is already there:
        o_index = openings.index(g.opening)
        
        score = find_score(g)

        if score == 1: #add a win
            records[o_index][0] = records[o_index][0] + 1
        elif score == 0.5: #add a draw
            records[o_index][2] = records[o_index][2] + 1
        else: # add a loss
            records[o_index][1] = records[o_index][1] + 1

#can sort openings by color
#bring up a continuous menu that can show your best, worst, and most played openings
option = ''
while option != "e":
    print("What color do you want to see your opening data for?")
    print("w - white")
    print("b - black")
    print("e - exit")
    print()
    color = input()
    
    while color != 'w' and color != 'b' and color != 'e':
        
        if color != 'w' and color != 'b' and color != 'e':
            color = input("Please put w, b, or e")
    
    if color == "e":
        break
    
    if color == 'w':
            color = 'white'
        
    elif color == 'b':
            color = 'black'

    print("How would you like to sort your openings?")
    print("1 - best")
    print("2 - worst")
    print("3 - most played")
    print("4 - most wins")
    print("5 - most losses")
    print("e - exit")
    print()

    option = input()
    valid = any(option == x for x in ["1", "2", "3", "4", "5", "e"])
    while valid != True:
        if valid != True:
            option = input("Please put 1,2,3, or e")
        valid = any(option == x for x in ["1", "2", "3", "4", "5", "e"])
    
    if option == "e":
        break
    
    #best openings sorted by loss percentage
    if option == "1":
        displayFunctions.display_best(color, openings, records)
    elif option == "2":
        displayFunctions.display_worst(color, openings, records)
    elif option == "3":
        displayFunctions.display_most_played(color, openings, records)
    elif option == "4":
        displayFunctions.display_most_wins(color, openings, records)
    elif option == "5":
        displayFunctions.display_most_losses(color, openings, records)