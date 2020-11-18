import csv
import datetime


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

abbrev_us_state = dict(map(reversed, us_state_abbrev.items()))

def main():
    usStateJobDict = {"TX": 0}
    with open('datalab/temp_datalab_records_job_listings_4.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                print('region index is', row.index('region'))
                print('country index is', row.index('country'))
                print('number_of_openings index is', row.index('number_of_openings'))
                print('posted_date', row.index('posted_date'))
                print('region, country, posted_date')
                
                line_count += 1
            else:
                # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                if row[10] == 'USA':
                    # if date is marked and if posted date exist
                    if (row[9] != '') and (row[14] != ''):
                        if len(row[9]) != 2:
                            try:
                                state = us_state_abbrev[row[9]]
                            except KeyError:
                                line_count += 1
                                continue
                        else:
                            state = row[9]
                        state = state.upper()
                        if state in abbrev_us_state:
                            if state in usStateJobDict:
                                usStateJobDict[state] += 1
                            else:
                                usStateJobDict[state] = 1
                        # else:
                        #     print(row)
                    # else:
                    #     print(row)
                line_count += 1
        print(f'Processed {line_count} lines.')

        print(usStateJobDict)
    with open('us_state_job_file_4.csv', mode='w') as usjob_file:
        usjob_writer = csv.writer(usjob_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for key in sorted(usStateJobDict):
            usjob_writer.writerow([key, usStateJobDict[key]])

if __name__ == "__main__":
    main()

