import csv
from tqdm import tqdm

#Dictionary
#key=phonenumber
#value=array of customerIDs that the phone number was reverse-appended and duplicated for

#at the end, we can flatten the dictionary to keeping only arrays with length > 1

duplicates_dict = {}

with open('fonebookout_tiaa.csv', newline='') as filtered_csv:
	reader = csv.DictReader(filtered_csv)
	print("Finding all reverse-appended phone numbers and creating a dictionary")
	for row in reader:
		phoneNumber = row['phoneNumber']
		if phoneNumber != '' and phoneNumber != None:
			if not phoneNumber in duplicates_dict:
				#phone number was never registered as a key in dict
				new_pf_array = []
				new_pf_array.append(row['customerId'])
				duplicates_dict[phoneNumber] = new_pf_array
			else:
				duplicates_dict[phoneNumber].append(row['customerId'])

headers = ['phoneNumber', 'customerIds']

with open('duplicate_phonenumbers_out_v2_real.csv', 'w', newline='') as write_file:
	writer = csv.DictWriter(write_file, fieldnames=headers, extrasaction='ignore')
	writer.writeheader()
	#print(duplicates_dict)
	for k,v in duplicates_dict.items():
		if len(v) > 1:
			row={}
			row['phoneNumber'] = k
			row['customerIds'] = v
			writer.writerow(row)






