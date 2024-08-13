import csv
from tqdm import tqdm

count=0

with open('region-invalid-cleanup/second_set.csv', newline='') as filtered_csv:
	fonebook_reader = csv.DictReader(filtered_csv)
	with open('tiaa-region-invalids-cleanup-final-second-set.csv', 'w', newline='') as write_file:
		headers = fonebook_reader.fieldnames
		writer = csv.DictWriter(write_file, fieldnames=headers)
		writer.writeheader()
		for row in tqdm(fonebook_reader):
				region = row['region']
				#print(region)
				#count+=1
				write_row = row.copy()
				if region == 'NEW YORK':
					write_row['region'] = 'NY'
				elif region == 'NEW JERSEY':
					write_row['region'] = 'NJ'
				elif region == 'NORTH CAROLINA':
					write_row['region'] = 'NC'
				elif region == 'RHODE ISLAND':
					write_row['region'] = 'RI'
				elif region == 'SOUTH CAROLINA':
					write_row['region'] = 'SC'
				elif region == 'DISTRICT COLUMBIA':
					write_row['region'] = 'DC'
				elif region == 'UNKNOWN STATE/PROVINCE':
					write_row['region'] = '' 				
				elif region == 'PUERTO RICO':
					write_row['region'] = 'PR'
				elif region == 'ARMED FORCES EUROPE, THE MIDDLE EAST, AND CANADA':
					write_row['region'] = 'AE'			
				elif region == 'ARMED FORCES PACIFIC':
					write_row['region'] = 'AP'
				elif region == 'ARMED FORCES AMERICAS (EXCEPT CANADA)':
					write_row['region'] = 'AA'	
				elif region == 'WEST VIRGINIA':
					write_row['region'] = 'WV'
				elif region == 'AMERICAN SAMOA':
					write_row['region'] = 'AS'
				elif region == 'GUAM':
					write_row['region'] = 'GU'
				elif region == 'NEW HAMPSHIRE': 
					write_row['region'] = 'NH'
				elif region == 'NEW MEXICO':
					write_row['region'] = 'NM'
				elif region == 'NORTH DAKOTA':
					write_row['region'] = 'ND'
				elif region == 'VIRGIN ISLANDS':
					write_row['region'] = 'VI'
				elif region == 'SOUTH DAKOTA':
					write_row['region'] = 'SD'
				writer.writerow(write_row)

#print(count)