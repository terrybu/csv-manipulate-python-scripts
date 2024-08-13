import csv
from tqdm import tqdm


cnt = 0 
offending_nums = set()
max_associations = 0 
saved_max_num = 0

with open('tiaa-duplicate-mapping.csv', newline='') as filtered_csv:
	reader = csv.DictReader(filtered_csv)
	for row in tqdm(reader):
		custids = row['customerIds'].split(',')
		print(custids)
		if len(custids) > 10:
			max_associations = max(max_associations,len(custids))
			if len(custids) == max_associations:
				saved_max_num = row['phoneNumber']
			cnt += 1
			offending_nums.add(row['phoneNumber'])

print(cnt)

print(offending_nums)


print(max_associations)

print("saved max num")
print(saved_max_num)