import csv
import pandas as pd
from optparse import OptionParser
import os 

#TODO: 
#argparse the input file -I
#argparse the output file -O
#compare the two 
#spit out the result 
#no writer is needed? maybe in the future

def process(fb_input,fb_output):
        with open(fb_input,'r') as fb_in, open(fb_output,'r') as fb_out:
                fi = csv.DictReader(fb_in)
                fo = csv.DictReader(fb_out)

                set_custids_fi = set()
                set_custids_fo = set()

                for row in fi:
                # create a set of customerIds
                        set_custids_fi.add(row['customerId'])

                for row in fo:
                # create a set of customerIds
                        set_custids_fo.add(row['customerId'])

        #if it's not empty, something wrong
        if set_custids_fi == set_custids_fo:
                print("Input file set of customerIds = Output file set of customerIds. Success.")
        else:
                print("input file set of customerIds does not match output file set of customerIds.")
                print("size of set for input file")
                print(len(set_custids_fi))

                print("size of set for output file")
                print(len(set_custids_fo))

                difference = set_custids_fi.difference(set_custids_fo)
                print("difference between the two sets")
                print(difference)


                print("size difference between the two sets")
                print(len(difference))

def main():     
        parser = OptionParser()
        parser.add_option( "-i", "--input", dest="fb_input_filename", default=None, action="store", type="string", help="Fonebook input file  to process.")
        parser.add_option( "-o", "--output", dest="fb_output_filename", default=None, action="store", type="string", help="Fonebook output file  to process.")

        (options, args) = parser.parse_args()
        if len(args) > 0:
                parser.error( "Unknown arguments passed to function: " + str(args) + "." + "\n Please use --help after the command and press enter for help") 
                
        if not options.fb_input_filename:
                parser.error( "Input fb_input_filename must be specified.")
                return -1
        if not options.fb_output_filename:
                parser.error( "Output fb_output_filename must be specified.")
                return -1

        if os.path.exists( options.fb_input_filename) and os.path.exists( options.fb_output_filename) :
                process(options.fb_input_filename,options.fb_output_filename)


if __name__ == "__main__":
    main()

