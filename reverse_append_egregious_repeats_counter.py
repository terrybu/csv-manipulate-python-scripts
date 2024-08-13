import csv
from optparse import OptionParser
import os 

def process(fb_output):
        with open(fb_output,'r') as fb_out:
                fo = csv.DictReader(fb_out)

                dict_rev_append_repeat = {}

                for row in fo:
                        #we care about verified=true and contactability is high either 1 or 2 track both.
                        if row['verified'] == '':
                                if row['phoneNumber'] in dict_rev_append_repeat and row['phoneNumber'] != '':
                                        dict_rev_append_repeat[row['phoneNumber']] += 1
                                else:
                                        dict_rev_append_repeat[row['phoneNumber']] = 1


                copy = dict_rev_append_repeat.copy()
                for k,v in dict_rev_append_repeat.items():
                        if v <= 1:
                                del copy[k]

                sorted_copy = sorted(copy.items(), key=lambda x: x[1], reverse=True)
                print(sorted_copy)

                for item in sorted_copy:
                        print("Reverse-Appended phone number " + item[0] + " appears " + str(item[1]) + " times in the output file.")


def main():     
        parser = OptionParser()
        parser.add_option( "-i", "--input", dest="fb_output_filename", default=None, action="store", type="string", help="Fonebook input file  to process.")

        (options, args) = parser.parse_args()
        if len(args) > 0:
                parser.error( "Unknown arguments passed to function: " + str(args) + "." + "\n Please use --help after the command and press enter for help") 
                
        if not options.fb_output_filename:
                parser.error( "Input fb_output_filename must be specified.")
                return -1


        if os.path.exists( options.fb_output_filename):
                process(options.fb_output_filename)


if __name__ == "__main__":
    main()

