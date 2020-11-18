import csv

from dictlib import us_state_abbrev, abbrev_us_state, columnNameList

# not used
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


# process based on user filter
def processData(userFilterDict, userXAxis, file):
########################################
#Input:
    # UserInput example: userPriChoiceDict = {'title': 'Data Scientist', 'country': 'USA', 'region': 'CA'}
    # File handler example: fileList = ['/home/peilong/Documents/dataFrame/dataProject/datalab/temp_datalab_records_job_listings_4.csv', '/home/peilong/Documents/dataFrame/dataProject/datalab/temp_datalab_records_job_listings_5.csv', '/home/peilong/Documents/dataFrame/dataProject/datalab/temp_datalab_records_job_listings_7.csv', '/home/peilong/Documents/dataFrame/dataProject/datalab/temp_datalab_records_job_listings_6.csv']

#Output:
    # Plot Maker Input example: Data = {'Data Scientist, USA': ['AK','AL','AR','AZ','CA','CO','CT','DC','DE','FL','GA','HI','IA','ID','IL','IN','KS','KY','LA','MA','MD','ME','MI','MN','MO','MS','MT','NC','ND','NE','NH','NJ','NM','NV','NY','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VA','VT','WA','WI','WV','WY'],'Number of job':[78112,454163,287754,896481,5841354,1124741,458416,174988,123715,2259177,1297760,110014,310762,200847,1554790,736053,277829,409769,406856,1276979,952217,119656,899514,779235,556498,251131,83152,1086100,80801,156510,162360,1053763,189041,382632,1771785,1282502,335615,467366,1722800,104092,567580,63652,767854,3355422,358381,1695499,52227,3033877,594778,151314,77381]  }
########################################

    userXAxisDict = {}
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'\t Column names are {", ".join(row)}')
                line_count += 1
            else:
                n = 0
                for filter, filterValue in userFilterDict.items():
                    if filterValue in row[columnNameList.index(filter)]:
                        n += 1
                # select user x-Axis without cleaning
                if n == len(userFilterDict):
                    # read user x-Axis value
                    xAxisValue = row[columnNameList.index(userXAxis)]
                    if xAxisValue in userXAxisDict:
                        userXAxisDict[xAxisValue] += 1
                    else:
                        userXAxisDict[xAxisValue] = 1

                line_count += 1
        print(f'\t Processed {line_count} lines.')

    return userXAxisDict
