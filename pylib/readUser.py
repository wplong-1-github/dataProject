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


def main():

    # user input
    userPriChoiceDict = {}
    # priPriOption = ['title','category','locality','region','country','date_added']
    allOptionDict = {'country':['USA','Israel'], 'region':['AK','AL','AR','AZ','CA','CO','CT','DC','DE','FL','GA','HI','IA','ID','IL','IN','KS','KY','LA','MA','MD','ME','MI','MN','MO','MS','MT','NC','ND','NE','NH','NJ','NM','NV','NY','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VA','VT','WA','WI','WV','WY'], 'title':['Data Scientist','Software Engineer']}

    allOptionKeyList = list(allOptionDict.keys())
    for i in range(len(allOptionKeyList)):
        pri, priChoice = readInputPriority(i+1, allOptionDict)
        userPriChoiceDict[pri] = priChoice
        print(f'User choice: {userPriChoiceDict}')
        # then make plot
        # 

if __name__ == "__main__":
    main()
