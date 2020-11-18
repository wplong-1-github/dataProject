import csv
import pandas as pd
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join

# import collections

from dictlib import us_state_abbrev, abbrev_us_state, columnNameList
from readUserlib import readInputPriority, readXAxisFilter
from fileHandlerlib import fileNameHandler
from processDatalib import recordRegion, processData
from makePlotlib import makeHistogram, formatDictDataforHist
from cleanDatalib import cleanRegionDataForHist


########################################
# Input:
#     UserInput example: userPriChoiceDict = {'title': 'Data Scientist', 'country': 'USA', 'region': 'CA'}
#     File handler example: fileList = ['/home/peilong/Documents/dataFrame/dataProject/datalab/temp_datalab_records_job_listings_4.csv', '/home/peilong/Documents/dataFrame/dataProject/datalab/temp_datalab_records_job_listings_5.csv', '/home/peilong/Documents/dataFrame/dataProject/datalab/temp_datalab_records_job_listings_7.csv', '/home/peilong/Documents/dataFrame/dataProject/datalab/temp_datalab_records_job_listings_6.csv']

# Output:
#     Plot Maker Input example: Data = {'Data Scientist, USA': ['AK','AL','AR','AZ','CA','CO','CT','DC','DE','FL','GA','HI','IA','ID','IL','IN','KS','KY','LA','MA','MD','ME','MI','MN','MO','MS','MT','NC','ND','NE','NH','NJ','NM','NV','NY','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VA','VT','WA','WI','WV','WY'],'Number of job':[78112,454163,287754,896481,5841354,1124741,458416,174988,123715,2259177,1297760,110014,310762,200847,1554790,736053,277829,409769,406856,1276979,952217,119656,899514,779235,556498,251131,83152,1086100,80801,156510,162360,1053763,189041,382632,1771785,1282502,335615,467366,1722800,104092,567580,63652,767854,3355422,358381,1695499,52227,3033877,594778,151314,77381]  }
########################################


def main():

########################################
    # # user input
    # userPriChoiceDict = {}
    # # priPriOption = ['title','category','locality','region','country','date_added']
    # allOptionDict = {'country':['USA','Israel'], 'region':['AK','AL','AR','AZ','CA','CO','CT','DC','DE','FL','GA','HI','IA','ID','IL','IN','KS','KY','LA','MA','MD','ME','MI','MN','MO','MS','MT','NC','ND','NE','NH','NJ','NM','NV','NY','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VA','VT','WA','WI','WV','WY'], 'title':['Data Scientist','Software Engineer']}
########################################

    
    ## get user input
    userFilterDict, userXAxis = readXAxisFilter()
    print(f'\t Filter in priority: {userFilterDict}. x-axis of histogram: {userXAxis}')

    # fileDir = '/home/peilong/Documents/dataFrame/dataProject/datalab/'
    # fileList = fileNameHandler(fileDir)
    file = '/home/peilong/Documents/dataFrame/dataProject/datalab/temp_datalab_records_job_listings_7.csv'
    
    ## get files
    # file = '/home/peilong/Documents/dataFrame/dataProject/testDataAndCode/temp_datalab_records_job_listings_test.csv'
    print(f'\t File location {file}')

    ## process data and get filtered data
    userXAxisDataDict = processData(userFilterDict, userXAxis, file)
    print(userXAxisDataDict)

    ## clean data
    newUserXAxisDataDict = cleanRegionDataForHist(userXAxisDataDict)

    ## format newUserXAxisDataDict for histogram
    Data = formatDictDataforHist(newUserXAxisDataDict, userFilterDict, userXAxis)

    ## use filtered data to make histogram
    makeHistogram(Data)
    
    
if __name__ == "__main__":
    main()
