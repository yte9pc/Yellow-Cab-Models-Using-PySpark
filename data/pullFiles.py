# Purpose of this python script is to pull the data need from https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

import requests

url = 'https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2019-01.csv'
directory = url.replace(file_name, '')

# Downloads 2019 yellow cab data
for month in range(1, 13):
    file = directory + file_name.replace('-01', '-'+"{:02d}".format(month))
    print("Started Downloading", file)
    r = requests.get(file, allow_redirects=True)
    open(file.split('/')[-1], 'wb').write(r.content)
    print("Finished Downloading", file)

# Downloads taxi zone look up data
taxis_zone = 'https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv
print("Started Downloading", taxis_zone)
r = requests.get(taxis_zone, allow_redirects=True)
open(taxis_zone.split('/')[-1], 'wb').write(r.content)
print("Finished Downloading", taxis_zone)


# Downloads data dictionary
data_dictionary = 'https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf'
print("Started Downloading", data_dictionary)
r = requests.get(data_dictionary, allow_redirects=True)
open(data_dictionary.split('/')[-1], 'wb').write(r.content)
print("Finished Downloading", data_dictionary)
