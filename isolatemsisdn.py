import csv
from tqdm import tqdm

customerid_array = [] 

with open('filtered.csv', newline='') as filtered_csv:
	reader = csv.DictReader(filtered_csv)
	print("Accessing filtered csv to get just the customerID extracted into an array")
	for row in reader:
		customerid_array.append(row['customerId'])

#print(customerid_array)
print(len(customerid_array))

with open('tiaa-cleaned-input.csv', newline='') as tiaa_file:
	reader2 = csv.DictReader(tiaa_file)
	headers = reader2.fieldnames
	with open('isolated_msisdn_out.csv', 'w', newline='') as write_file:
		writer = csv.DictWriter(write_file, fieldnames=headers)
		writer.writeheader()
		for customerId in tqdm(customerid_array):
			#iterate over every customerid (because this came back with false, 0 0)
			#find that customerID in reader2, the input file
			#find the phone number, write it out
			#print(customerId)
			for row in reader2:
				#print(row)
				if row['customerId'] == customerId:
					#bingo
					#writer.writerow(row)
					print(customerId)
					continue




