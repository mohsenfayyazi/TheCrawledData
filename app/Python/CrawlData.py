import  requests
import json
from pymongo import MongoClient

#connect to mongodb database and collection
myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["Test"]
mycol = mydb["TheCrawledData"]
#delete collection to stop insert duplicated data
mycol.drop()


# Start the session
session = requests.Session()

# Create the Login Information
payload = {'email':'mohsen.fayyazi@gmai.com', 
          'password':'12345678'
         }

# Post the payload to the site to log in
s = session.post("https://www.rrpcanada.org/#/login", data=payload)


# Navigate to the next page and scrape the data
res = session.get("https://api.rrpcanada.org/supplies")
data = res.json()


# get data from scrap json and insert to collection
for key in data['content']['content']:
    print(key['minimumOrder'],key['productName'])
    mycol.insert_one({"Product_Name":key['productName'],"Total_Available":key['minimumOrder']})

        

