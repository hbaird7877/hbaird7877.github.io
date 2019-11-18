

import csv

with open('nfl_teams.csv', mode='a') as csv_file:
    fieldnames = ['id', 'team', 'wins', 'losses']
    nfl_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    nfl_writer.writerow({'id': 4,'team': 'Giants', 'wins': 6, 'losses': 4})
    nfl_writer.writerow({'id': 5,'team':'Lions','wins': 8,'losses': 2})