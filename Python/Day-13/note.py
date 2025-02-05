import csv

data=[
	['alice',20,'hyd'],
	['bob',23,'ben'],
	['carlo',21,'mum']
]

with open("dataCSV.csv","a") as file:
	writer=csv.writer(file)
	writer.writerows(data)

