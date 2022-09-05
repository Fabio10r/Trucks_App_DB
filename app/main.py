import requests as requests
import json
import re
import psycopg2
import pandas as pd

#Define our connection string to postgres DB
conn_string = "host='db' dbname='craftable' user='postgres' password='0563'"

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string, port=5432)
cursor = conn.cursor()

#chars to replace
char_to_replace = {'€': 'e',
                   '3': 'e'}
                  
id = 0

#Define schema for DataFrame
""" schema = {
    'properties' : {
        'id': {'type': 'integer'}
        'name': {'type': 'string'}
        'postCode': {'type': 'string'}
        'phone': {'type': 'string'}
        'country': {'type': 'string'}
        'county': {'type': 'string'}
        'long': {'type': 'string'}
        'lat': {'type': 'string'}
        'hasSpecialCharacters': {'type': 'boolean'}
        'noSpecialCharacters': {'type': 'string'}
    }
} """

#Read csv PostCode column to DataFrame
df = pd.read_csv("customer_list.csv")

for index, row in df.iterrows():
    #get each company info from CSV
    name = row['Company Name']
    post_code = row['PostCode'].rstrip()
    phone = row['Phone']

    noSpecialChar = name
    hasSpecialChar = False

    #filter each name for special chars
    if re.search('[^A-z\s\d-][\\\^]?' ,name):

        hasSpecialChar = True
        # Replace key character with value character in string
        for key, value in char_to_replace.items():
            noSpecialChar = noSpecialChar.replace(key, value)

        noSpecialChar = re.sub('[^A-z\s\d-][\\\^]?',"",noSpecialChar)

    #make request to API postcodes.io
    response = requests.get(f'http://api.postcodes.io/postcodes/{post_code}').json()

    if response['status'] == 200:
        lat = response['result']['latitude']
        long = response['result']['longitude']
        country = response['result']['country']
        county = response['result']['european_electoral_region']
        id = id + 1

        #singer.write_schema('trucks', schema)
        #singer.write_records('trucks', [{'id': id, 'name': name, 'postCode' : post_code, 'phone' : phone, 'country': country, 'county' : county, 'long' : long, 'lat' : lat, 'hasSpecialCharacters' : hasSpecialChar, 'noSpecialCharacters' : noSpecialChar})

        query = """ INSERT INTO trucks (id, name, postCode, phone, country, county, long, lat, hasSpecialCharacters, noSpecialCharacters) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        cursor.execute(query, (id, name, post_code, phone, country, county, long, lat, hasSpecialChar, noSpecialChar))
        
cursor.execute("SELECT * FROM trucks")
print(cursor.fetchall())

conn.commit()
conn.close()