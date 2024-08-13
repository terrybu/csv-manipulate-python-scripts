import csv
from tqdm import tqdm

with open('fonebookouttiaa.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	headers = reader.fieldnames
	with open('fonebookouttiaa_onlyinvalids_out.csv', 'w', newline='') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=headers)
		writer.writeheader()
		for row in tqdm(reader):
			#print(row['verified'], row['nameScore'],row['addressScore'])
			if row['verified'] == 'false' and row['nameScore'] == '0' and row['addressScore'] == '0':
				writer.writerow(row)
