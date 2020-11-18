from dictlib import us_state_abbrev, abbrev_us_state, columnNameList
from city_to_state import city_to_state_dict

def cleanRegionDataForHist(userXAxisDataDict):

    newUserXAxisDataDict = {}
    stateAbbrev = ''
    for regionValue in userXAxisDataDict:
        # find the correct region_abbrev
        if len(regionValue) != 2:
            # e.x. if 'California' is the regionValue
            if regionValue in us_state_abbrev:
                stateAbbrev = us_state_abbrev[regionValue]
            # if 'California, CA' is the regionValue
            elif any(abbrev in regionValue for abbrev in abbrev_us_state):
                for abbrev in abbrev_us_state:
                    # if 'CA' in 'California, CA' 
                    if abbrev in regionValue:
                        stateAbbrev = abbrev
            # if 'Menlo Park' is the regionValue
            elif regionValue in city_to_state_dict:
                state = city_to_state_dict[regionValue]
                stateAbbrev = us_state_abbrev[state]
            else:
                stateAbbrev = 'Unknown'
        elif regionValue.upper() in abbrev_us_state:
            stateAbbrev = regionValue.upper()
        else:
            stateAbbrev = 'Unknown'

        # add corresponding state_abbrev together
        if stateAbbrev in newUserXAxisDataDict:
            newUserXAxisDataDict[stateAbbrev] = newUserXAxisDataDict[stateAbbrev] + userXAxisDataDict[regionValue]
        else:
            newUserXAxisDataDict[stateAbbrev] = userXAxisDataDict[regionValue]

    return newUserXAxisDataDict

