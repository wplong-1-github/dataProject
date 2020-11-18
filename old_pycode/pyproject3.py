import csv
import datetime


def main():
    usStateJobDict = {"TX": 0}
    with open('us_state_job_file_2017.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            print(f'Column names are {", ".join(row)}')
            state = row[0]
            if state in usStateJobDict:
                usStateJobDict[state] += int(row[1])
            else:
                usStateJobDict[state] = int(row[1])
            line_count += 1
        print(f'Processed {line_count} lines.')
        print(usStateJobDict)

    with open('us_state_job_file_2017_all.csv', mode='w') as usjob_file:
        usjob_writer = csv.writer(usjob_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for key in sorted(usStateJobDict):
            usjob_writer.writerow([key, usStateJobDict[key]])

if __name__ == "__main__":
    main()

