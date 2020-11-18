import csv
import pandas as pd
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join

def readFile(fileDir):
    onlyfiles = [f for f in listdir(fileDir) if isfile(join(fileDir, f))]
    newFileList = [fileDir + f for f in onlyfiles]
    # print(newFileList)
    return newFileList

def makeHistogram(Data):
    key_list = list(Data.keys())
    xName = key_list[0]
    yName = key_list[1]
    df = pd.DataFrame(Data,columns=[xName,yName])
    df.plot(x = xName, y= yName, kind = 'bar')
    plt.show()

def readInputPriority(priNumber, priOption):
    print(f"Choose your {priNumber} priority in finding a job")
    print(f'\t Options: which {priOption}')
    var = input("Input: ") 
    if var in priOption:
        print("Priority: " + var)
        return var
    else:
        print('Invalid value!')
        return -1

def processDataBaseOnPriority(priList):
    print ('nouse')

def printCSV():
    columnNameList = ['dataset_id', 'listing_id', 'domain', 'as_of_date', 'title', 'url', 'brand', 'category', 'locality', 'region', 'country', 'number_of_openings', 'date_added', 'date_updated', 'posted_date', 'location_string', 'description', 'entity_id', 'city_lat', 'city_lng', 'cusip', 'isin']
    with open('temp_datalab_records_job_listings_test.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                for i,column in enumerate(row):
                    print('{0: <20}'.format(columnNameList[i]), column)
                line_count += 1
        print(f'Processed {line_count} lines.')

def main():

# ['dataset_id', 'listing_id', 'domain', 'as_of_date', 'title', 'url', 'brand', 'category', 'locality', 'region', 'country', 'number_of_openings', 'date_added', 'date_updated', 'posted_date', 'location_string', 'description', 'entity_id', 'city_lat', 'city_lng', 'cusip', 'isin']

    # user input
    priList = []
    firstPriOption = ['title','category','locality','region','country','date_added']


    firstPri = readInputPriority('1st', firstPriOption)
    priList.append(firstPri)

    # # file handler
    # fileDir = '/home/peilong/Documents/dataFrame/dataProject/datalab/'
    # readFile(fileDir)


    # printCSV()

if __name__ == "__main__":
    main()
