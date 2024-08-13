from csv import writer
from csv import reader
import uuid

# Open the input_file in read mode and output_file in write mode
with open('fb_disenroll_WLT4k7f5lN00h7mH6PRD_202207011535.csv', 'r') as read_obj,open('output_prod.csv', 'w') as write_obj:
    # Create a csv.reader object from the input file object
    csv_reader = reader(read_obj)
    # Create a csv.writer object from the output file object
    csv_writer = writer(write_obj)
    # Read each row of the input csv file as list
    for row in csv_reader:
        # Append the default text in the row / list
        default_text = str(uuid.uuid4())
        row.append(default_text)
        # Add the updated row / list to the output file
        csv_writer.writerow(row)