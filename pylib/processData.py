import csv

from dictlib import us_state_abbrev, abbrev_us_state, columnNameList

def recordRegion(row, par):
    parValue = row[columnNameList.index(par)]
    if len(parValue) != 2:
        try:
            state = us_state_abbrev[parValue]
        except KeyError:
            return -1
    else:
        state = parValue
    state = state.upper()

    return state


# process based on priority
def main():
#Input:
    # UserInput example: userPriChoiceDict = {'title': 'Data Scientist', 'country': 'USA', 'region': 'CA'}
    # File handler example: fileList = ['/home/peilong/Documents/dataFrame/dataProject/datalab/temp_datalab_records_job_listings_4.csv', '/home/peilong/Documents/dataFrame/dataProject/datalab/temp_datalab_records_job_listings_5.csv', '/home/peilong/Documents/dataFrame/dataProject/datalab/temp_datalab_records_job_listings_7.csv', '/home/peilong/Documents/dataFrame/dataProject/datalab/temp_datalab_records_job_listings_6.csv']

#Output:
    # Plot Maker Input example: Data = {'Data Scientist, USA': ['AK','AL','AR','AZ','CA','CO','CT','DC','DE','FL','GA','HI','IA','ID','IL','IN','KS','KY','LA','MA','MD','ME','MI','MN','MO','MS','MT','NC','ND','NE','NH','NJ','NM','NV','NY','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VA','VT','WA','WI','WV','WY'],'Number of job':[78112,454163,287754,896481,5841354,1124741,458416,174988,123715,2259177,1297760,110014,310762,200847,1554790,736053,277829,409769,406856,1276979,952217,119656,899514,779235,556498,251131,83152,1086100,80801,156510,162360,1053763,189041,382632,1771785,1282502,335615,467366,1722800,104092,567580,63652,767854,3355422,358381,1695499,52227,3033877,594778,151314,77381]  }


    userPriChoiceDict = {'title': 'Service Technician', 'country': 'USA'}
    # , 'region': 'NC'}

    usStateJobDict = {}
    # with open('../testDataAndCode/temp_datalab_records_job_listings_test.csv') as csv_file:
    with open('/home/peilong/Documents/dataFrame/dataProject/datalab/temp_datalab_records_job_listings_7.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                n = 0
                for pri, priChoice in userPriChoiceDict.items():
                    # print (pri, priChoice)
                    if priChoice in row[columnNameList.index(pri)]:
                        n += 1
                # print('condition meet ', n)
                if n == len(userPriChoiceDict):
                    # hard coded region
                    # print(f'meet {n} requirement')
                    state = recordRegion(row, 'region')
                    if state in abbrev_us_state:
                        if state in usStateJobDict:
                            usStateJobDict[state] += 1
                        else:
                            usStateJobDict[state] = 1

                line_count += 1
        print(f'Processed {line_count} lines.')
        print(usStateJobDict)


if __name__ == "__main__":
    main()
