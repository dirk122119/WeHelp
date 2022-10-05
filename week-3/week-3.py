from urllib.request import urlopen
import urllib
import json
import ssl
import datetime
import csv 
from bs4 import BeautifulSoup

def w3FirstAssignment():
    url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
    ssl._create_default_https_context = ssl._create_unverified_context
    response = urlopen(url)
    data = json.loads(response.read())
    areaList=["中正區","萬華區","中山區","大同區","大安區","松山區","信義區","士林區","文山區","北投區","內湖區","南港區"]
    dataFilter=data["result"]["results"]

    for item in data["result"]["results"]:
        if (item["address"].split(" ")[2][0:3] in areaList):
            pass
        else:
            dataFilter.remove(item)

    with open('data.csv', 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)
        targetDate = datetime.datetime(2015,1,1)
        
        for item in dataFilter:
            postDate = datetime.datetime(int(item["xpostDate"].split("/")[0]),int(item["xpostDate"].split("/")[1]),int(item["xpostDate"].split("/")[2]))

            if(targetDate<=postDate):
                img=item["file"].split("https://www")
                # print(item["stitle"],item["address"].split(" ")[2][0:3],item["longitude"],item["latitude"])
                writer.writerow([item["stitle"],item["address"].split(" ")[2][0:3],item["longitude"],item["latitude"],"https://www"+img[1]])
def w3SecondAssignment():
    url="https://www.ptt.cc/bbs/movie/index.html"
    ssl._create_default_https_context = ssl._create_unverified_context

    headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
    req=urllib.request.Request(url,headers=headers)
    page=urllib.request.urlopen(req)
    html=page.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    indexNum=int(soup.find_all("a",string="‹ 上頁")[0]["href"].split("/")[3][5:-5])+1
    good=[]
    normal=[]
    bad=[]
    for i in range (indexNum,indexNum-10,-1):
        url="https://www.ptt.cc/bbs/movie/index"+str(i)+".html"
        req=urllib.request.Request(url,headers=headers)
        page=urllib.request.urlopen(req)
        html=page.read()
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all("div",class_="title"):
            try:
                if(item.a.get_text().split("]")[0][1:]=="好雷"):
                    good.append(item.a.get_text()+"\n")
                elif(item.a.get_text().split("]")[0][1:]=="普雷"):
                    normal.append(item.a.get_text()+"\n")
                elif(item.a.get_text().split("]")[0][1:]=="負雷"):
                    bad.append(item.a.get_text()+"\n")
            except:
                pass

    txtFile = open("movie.txt","w")
    txtFile.writelines(good)
    txtFile.writelines(normal)
    txtFile.writelines(bad)
    txtFile.close()
    
    



w3SecondAssignment()
                
        
    
    




