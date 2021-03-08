import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
with request.urlopen(src) as response:
    data=json.load(response) 

file=open("week3.txt",mode="w",encoding="utf-8")
i=0
while i<=len(data["result"]["results"])-1:
    file.write(data["result"]["results"][i]["stitle"])
    file.write(",")
    file.write(data["result"]["results"][i]["longitude"])
    file.write(",")
    file.write(data["result"]["results"][i]["latitude"])
    file.write(",")
    photoFile=data["result"]["results"][i]["file"]
    keyword="http"
    wordNumber=photoFile.find(keyword,1)
    file.write(data["result"]["results"][i]["file"][:wordNumber])   
    file.write(",\n")
    i+=1


#longitude=經度
#latitude=緯度