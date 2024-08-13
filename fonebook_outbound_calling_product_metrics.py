import csv
from optparse import OptionParser
import os 
import pandas as pd

def process(fb_output):
        with open(fb_output,'r') as fb_out:
                fo = csv.DictReader(fb_out)

                cnt = 0 
                true_score_1 = 0
                true_score_2 = 0
                ra_score_1 = 0
                ra_score_2 = 0

                for row in fo:
                        cnt += 1
                        #we care about verified=true and contactability is high either 1 or 2 track both.
                        if row['verified'] == 'true' and row['contactabilityRank'] == '1':
                                true_score_1 += 1
                        elif row['verified'] == 'true' and row['contactabilityRank'] == '2':
                                true_score_2 += 1
                        elif row['verified'] == '' and row['contactabilityRank'] == '1':
                                ra_score_1 += 1
                        elif row['verified'] == '' and row['contactabilityRank'] == '2':
                                ra_score_2 += 1

                stat_true_and_high_score = (true_score_1 + true_score_2)/cnt * 100
                stat_ra_and_high_score = (ra_score_1 +ra_score_2)/cnt * 100

                print(str(round(stat_true_and_high_score,2)) + "% out of the total output file is verified true with a score of 1 or 2")

                all_high_scores = stat_true_and_high_score + stat_ra_and_high_score
                print(str(round(all_high_scores,2)) + "% out of the total output file has a high contactabiity score of 1 or 2 (reverse-appends included)")

                #avg score calculations
                df=pd.read_csv(fb_output)
                p=df['contactabilityRank'].describe()
                print(p)


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

