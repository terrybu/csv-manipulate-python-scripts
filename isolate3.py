import csv
from tqdm import tqdm

dictionary = {}

with open('tiaa-input_rows_returned_invalid_verified_false.csv', newline='') as filtered_csv:
	reader_just_invalid_inputs = csv.DictReader(filtered_csv)
	for row in reader_just_invalid_inputs:
		invalid_ph = row['phoneNumber']
		invalid_customerId = row['customerId']
		dictionary[invalid_customerId] = invalid_ph

with open('fonebookouttiaa.csv', newline='') as tiaa_fonebook:
	fonebook_reader = csv.DictReader(tiaa_fonebook)
	headers = fonebook_reader.fieldnames
	with open('finished_merge_real_prod_file.csv', 'w', newline='') as write_file:
		writer = csv.DictWriter(write_file, fieldnames=headers)
		writer.writeheader()
		for row in tqdm(fonebook_reader):
			if row['customerId'] in dictionary.keys() and row['phoneNumber'] == '' and row['verified'] == 'false' and row['nameScore'] == '0' and row['addressScore'] == '0':
				write_row = row.copy()
				cust_id = row['customerId'] 
				cust_invalid_ph = dictionary[cust_id]
				write_row['phoneNumber'] = cust_invalid_ph
				writer.writerow(write_row)
			else:
				writer.writerow(row)



