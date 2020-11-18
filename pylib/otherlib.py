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
