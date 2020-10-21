import os
import urllib.request
import time
import matplotlib.pyplot as plt
import re
xGOLD=[]
yGOLD=[]
goldHolder=[1]
goldCounter=1
def gold():
    global xGOLD
    global yGOLD
    url= "https://goldprice.com/"
    urllib.request.urlretrieve(url,"gold.txt")
    f=open("gold.txt",'r')
    x=f.read()
    goldInUSD = re.findall('nfprice".*[0-9],[0-9]{3}.[0-9]{2}',x)
    S=re.findall('[0-9,.]{4,}',goldInUSD[0])
    price=S[0].replace(',','')
    price=float(price)
    yGOLD.append(price)
    print("The price of gold is",price)
def goldGraph():
    global xGOLD
    global yGOLD
    global goldHolder
    plt.plot(yGOLD)
    plt.ylabel("Price of Gold in USD")
    plt.xlabel("Time in minutes")
    plt.title("Price of Gold over Time")
    plt.show()
while True:
    gold()
    time.sleep(1)
