def output(sorter, indexes, color_openings, color_records):
     #if there are not 10 openings, only put that many
    stop_amount = 10
    if len(sorter) < 10:
        stop_amount = len(sorter)
    #output
    print()
    for n in range(stop_amount - 1):
        arr_ind = indexes.index(sorter[n])
        print(f'{color_openings[arr_ind][7:]}: {color_records[arr_ind][0]}-{color_records[arr_ind][1]}-{color_records[arr_ind][2]}')
        indexes[arr_ind] = "added" #we dont want to search the same thing twice
    print()

def display_worst(color, openings, records):
    indexes = []
    color_openings = []
    color_records = []
    #find the loss % for each
    for r in range(len(records) - 1):
        #only get the correct color openings
        if color == openings[r][0:5]:
            total = records[r][0] + records[r][1] + records[r][2]
            losses = records[r][1]
            indexes.append(losses/total)
            color_openings.append(openings[r])
            color_records.append(records[r])
    #make a copy with the sorted values so you can find its index
    sorter = indexes.copy()
    sorter.sort(reverse=True)

    output(sorter, indexes, color_openings, color_records)


def display_best(color, openings, records):
    indexes = []
    color_openings = []
    color_records = []
    #find the loss % for each
    for r in range(len(records) - 1):
        #only get the correct color openings
        if color == openings[r][0:5]:
            total = records[r][0] + records[r][1] + records[r][2]
            losses = records[r][1]
            indexes.append(losses/total)
            color_openings.append(openings[r])
            color_records.append(records[r])
    #make a copy with the sorted values so you can find its index
    sorter = indexes.copy()
    sorter.sort()

    output(sorter, indexes, color_openings, color_records)

def display_most_wins(color, openings, records):
    indexes = []
    color_openings = []
    color_records = []
    #find the loss % for each
    for r in range(len(records) - 1):
        #only get the correct color openings
        if color == openings[r][0:5]:
            wins = records[r][0]
            indexes.append(wins)
            color_openings.append(openings[r])
            color_records.append(records[r])
    #make a copy with the sorted values so you can find its index
    sorter = indexes.copy()
    sorter.sort(reverse=True)

    output(sorter, indexes, color_openings, color_records)

def display_most_losses(color, openings, records):
    indexes = []
    color_openings = []
    color_records = []
    #find the loss % for each
    for r in range(len(records) - 1):
        #only get the correct color openings
        if color == openings[r][0:5]:
            total = records[r][0] + records[r][1] + records[r][2]
            losses = records[r][1]
            indexes.append(losses)
            color_openings.append(openings[r])
            color_records.append(records[r])
    #make a copy with the sorted values so you can find its index
    sorter = indexes.copy()
    sorter.sort(reverse=True)

    output(sorter, indexes, color_openings, color_records)

def display_most_played(color, openings, records):
    indexes = []
    color_openings = []
    color_records = []
    #find the loss % for each
    for r in range(len(records) - 1):
        #only get the correct color openings
        if color == openings[r][0:5]:
            total = records[r][0] + records[r][1] + records[r][2]
            indexes.append(total)
            color_openings.append(openings[r])
            color_records.append(records[r])
    #make a copy with the sorted values so you can find its index
    sorter = indexes.copy()
    sorter.sort(reverse=True)

    output(sorter, indexes, color_openings, color_records)