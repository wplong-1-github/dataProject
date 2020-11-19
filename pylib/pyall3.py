import csv
import pandas as pd
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
import datetime

def main():
    # file = '/home/peilong/Documents/dataFrame/dataProject/datalab/temp_datalab_records_social_facebook.csv'
    file = '/home/peilong/Documents/dataFrame/dataProject/datalab/temp_datalab_records_linkedin_company.csv'

    dictFBlike = {}
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        like_index = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'\t Column names are {", ".join(row)}')
                like_index = row.index('followers_count')
                line_count += 1
            else:
                dataset = row[0]
                if dataset == '58362':
                    # time_str = row[1].split()[0]
                    time_str = row[1]
                    time_obj = datetime.datetime.strptime(time_str, '%Y-%m-%d')
                    if time_obj.date().year == 2017:
                        print(time_str)
                        dictFBlike[time_obj.strftime('%Y-%m-%d')] = row[like_index]
                line_count += 1

        print(f'\t Processed {line_count} lines.')
    print(dictFBlike)

    with open('LinkedIn_follow_ms.csv', mode='w') as ms_follow_file:
        ms_follow_file_writer = csv.writer(ms_follow_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for key, value in dictFBlike.items():
            ms_follow_file_writer.writerow([key, value])


    
if __name__ == "__main__":
    main()
