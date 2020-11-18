import json 


def readInputPriority(priNumber, allOptionDict):
    allOptionKeyList = list(allOptionDict.keys())
    print(f"Choose your priority-{priNumber} in finding a job")
    print(f'\t which {allOptionKeyList}')
    var = input(f"Input your priority-{priNumber}: ") 
    if var in allOptionKeyList:
        print(f"Choose which {var} you want to find a job")
        print(f'\t {allOptionDict[var]}')
        varChoice = input(f"Input your choice of {var}: ") 
        if varChoice in allOptionDict[var]:
            print(f"Priority: {var}({varChoice})")
            return var, varChoice
        else:
            print('Invalid value!')
            return -1
    else:
        print('Invalid value!')
        return -1

def readXAxisFilter():
    print('Filter for x-axis:')
    print('\t (1) Industry: category, title')
    print('\t (2) Location: country, region, locality')
    print('\t (3) Time: year, month, week')
    print('Please input your filter in priority (order):')
    print("\t e.g. {\"country\":\"USA\", \"title\":\"Data Science\"}")
    var = input(f"Input your filter: ") 
    filterDict = json.loads(var)
    print('Please input the x-axis of the histogram under your filters:')
    print("\t e.g. region")
    xAxis = input(f"Input your histogram x-axis: ") 

    return filterDict, xAxis
