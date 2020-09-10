
import csv
import time


def get_item(item_id):
    if type(item_id) != str:
        item_id = str(item_id)
    with open('loot.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if row[1] == item_id:
                return row


def get_rankings(columns):
    rankings = {}
    for col in columns:
        rankings[col] = 0
    with open('loot.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            for col in columns:
                if row[col] == "Yes":
                    rankings[col] += 1
    list_rankings = []
    for key, val in rankings.items():
        list_rankings.append((key, val))
    return list_rankings

def show_optimal_targets(item):
    item_data = get_item(item)
    drops_from = []
    for i in range(5, len(item_data)):
        if item_data[i] == "Yes":
            drops_from.append(i)
    unit_names = get_item("ITEM_IDS")
    ranks = get_rankings(drops_from)
    ranks = sorted(ranks, key=lambda k: k[1])
    for pair in ranks:
        print("{} - {} drops".format(unit_names[pair[0]], pair[1]))


if __name__ == "__main__":
    show_optimal_targets(1427)





