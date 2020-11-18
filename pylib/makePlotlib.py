import pandas as pd
import matplotlib.pyplot as plt
import collections

def makeHistogram(Data):
    key_list = list(Data.keys())
    xName = key_list[0]
    yName = key_list[1]
    df = pd.DataFrame(Data,columns=[xName,yName])
    df.plot(x = xName, y= yName, kind = 'bar')

    plt.xlabel(key_list[0])
    plt.ylabel(key_list[1])
    # plt.title('Histogram of IQ')
    plt.show()

    
def formatDictDataforHist(newUserXAxisDataDict, userFilterDict, userXAxis):
    ### sort dict for histogrm
    newUserXAxisDataDict_sorted = dict(collections.OrderedDict(sorted(newUserXAxisDataDict.items())))
    ### split dict into two lists
    userXAxisKeys = list(newUserXAxisDataDict_sorted.keys())
    userXAxisValues = list(newUserXAxisDataDict_sorted.values())

    xAxisStr = userXAxis.title()
    for userXValue in userFilterDict.values():
        xAxisStr = xAxisStr + ',' + userXValue
    # print(xAxisStr)

    Data = {xAxisStr:userXAxisKeys, 'Number of Jobs':userXAxisValues}
    print(f'\t Date for histogram: {Data}')

    return Data
