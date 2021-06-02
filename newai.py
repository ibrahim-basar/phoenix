import requests
import json
import math
get_url = "http://localhost:3000"
post_url = "http://localhost:4000"
get_headers = {"Content-Type": "application/json"}
post_headers = {"Content-Type": "application/json"}

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
    predictionData = [float(jsonData["tankA"]["x"]),
                      float(jsonData["tankA"]["y"]),
                      float(jsonData["tankA"]["r"]),
                      float(jsonData["tankA"]["can_fire"])]
    data = requests.get(get_surl, headers=get_headers)
    jsonData = json.loads(data.text)

    
    if stage==0:
        if not mina:
            mina=float(jsonData["tankA"]["r"])
        else:
            if mina>float(jsonData["tankA"]["r"]):
                mina=float(jsonData["tankA"]["r"])
        if not maxa:
            maxa=float(jsonData["tankA"]["r"])
        else:
            if maxa<float(jsonData["tankA"]["r"]):
                maxa=float(jsonData["tankA"]["r"])
            if mina== float(jsonData["tankA"]["r"]) or maxa==float(jsonData["tankA"]["r"]):
                stage=1
    if stage == 1:
        if previousx == float(jsonData["tankA"]["x"]) or previousy == float(jsonData["tankA"]["y"]):
            r=1
        else:
            r=0
        #data = {"m":m,"r":r, "f":f}
    m = 1

    data = {"m":m,"r":r, "f":0}
    data = json.dumps(data)
    resoınse = requests.post(post_url, data=jsonData, headers=post_headers)
                      
                      
