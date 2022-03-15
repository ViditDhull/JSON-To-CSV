# Importing required libraries

import pandas as pd

#Reading files in pandas

csv_pd = pd.read_csv('products_reference.csv')
json_pd = pd.read_json('scrapped.json')

#Parsing required data form json file

description = json_pd['tags'][0]['meta'][22]['content']
raw_price = json_pd['tags'][0]['meta'][24]['content']
title = json_pd['tags'][0]['meta'][18]['content']
vendor = json_pd['tags'][0]['meta'][26]['content']
images = json_pd['classes'][2]['img__1bebd']

#Coping the required data from csv file

fixrate = csv_pd['arg_fxrate']
url = csv_pd['arg_url']
type = csv_pd['arg_type']


#Parsing the data into csv file
csv_pd['source_description'] = description
csv_pd['source_price'] = float(raw_price) * float(fixrate)
csv_pd['source_url'] = url
csv_pd['product_title'] = title
csv_pd['vendor'] = vendor
csv_pd['product_type'] = type
csv_pd['images_array'] = [images]

#Saving the changes to new csv file

csv_pd.to_csv('updated_products_reference.csv')
