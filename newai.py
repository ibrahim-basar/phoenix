import requests
import json
import math
get_url = "http://localhost:3000"
post_url = "http://localhost:4000"
get_headers = {"Content-Type": "application/json"}
post_headers = {"Content-Type": "application/json"}
get_headersiki = {"Content-Type": "application/json", 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }


get_surl = "http://bdcanta.000webhostapp.com/phenix/ai.php"
previousx =0
previousy = 0
mina
maxa
stage=0
r=0
while True:
    data = requests.get(get_url, headers=get_headers)
    jsonData = json.loads(data.text)
    
    data = requests.post(get_surl, data=data, headers=get_headersiki)
    jsonData = json.loads(data.text)

    

        
    resoınse = requests.post(post_url, data=jsonData, headers=post_headers)
                      
                      
