#Aidan Rutherford, Zach Zolikof, & Dallas Henry
import os #modules used in project
import urllib.request
import json
import time
import re
import matplotlib.pyplot as plt
yaxis=[] #global variables
xholder=[1]
xaxis=[]
counter = 1
xGOLD=[]
yGOLD=[]
goldHolder=[1]
goldCounter=1

def bitcoin():  #function that records time and price of BTC
    global yaxis
    global xaxis
    url= "https://api.coindesk.com/v1/bpi/currentprice.json" #url where price was found
    urllib.request.urlretrieve(url,"bitcoin.txt") #url saves into a text file #Thanks to Professor Marriott for helping us with this before the lecture
    with open('bitcoin.txt') as json_file: #file loaded into a json file
        data = json.load(json_file)
    bitcoinInUSD = data["bpi"]["USD"]["rate"] #extracts price of BTC
    timeRecorded = data["time"]["updated"] #extracts time of price
    print("The price of Bitcoin is",bitcoinInUSD,"at",timeRecorded)
    yaxis.append(bitcoinInUSD) #Adds price to list to be graphed
    print("The time of this price is",timeRecorded)
    xaxis.append(timeRecorded)
    
def gold(): #function that records time and price of gold
    global xGOLD
    global yGOLD
    url= "https://goldprice.com/" #url where price was found
    urllib.request.urlretrieve(url,"gold.txt") #saved url as a text file
    f=open("gold.txt",'r') #opens and reads that file
    x=f.read() #Thanks to Professor Marriott again for showing us regular expressions before the lecture
    goldInUSD = re.findall('nfprice".*[0-9],[0-9]{3}.[0-9]{2}',x) #finds instance of gold price with use of regular expressions
    S=re.findall('[0-9,.]{4,}',goldInUSD[0]) #takes the line of code with price and extracts just numerical data
    price=S[0].replace(',','') #Allows price to be converted to floating point number
    price=float(price) #converts to float so it can be appended
    yGOLD.append(price) #appends to list to be plotted
    print("The price of gold is",price)
    
def bitcoinGraph():  #Graphs the price of Bitcoin
    global yaxis
    global xaxis
    global xholder
    plt.plot(yaxis)
    plt.ylabel("Price of Bitcoin(BTC) in USD")
    plt.xlabel("Time in Minutes (UTC)")
    plt.title("Price of Bitcoin(BTC) over time")
    plt.show()
def goldGraph(): #Graphs the price of Gold
    global xGOLD
    global yGOLD
    global goldHolder
    plt.plot(yGOLD)
    plt.ylabel("Price of Gold in USD")
    plt.xlabel("Time in minutes")
    plt.title("Price of Gold over Time")
    plt.show()
    
runTime=int(input("Collect data for how many minutes?")) #Prompts the user to enter duration that while loop runs
while True:
    for i in range(runTime):  #iruns only number of times specified by user
        bitcoin() 
        gold()
        time.sleep(60) #Timer keeps track of when price updates
    showGraph=input("Would you like to view a graph? Enter y or n.") #Prompts user if they want to see a graph
    if showGraph == 'y':
        whichGraph=input("Which graph would you like to see? gold or BTC.") #Prompts the user to show them a different graph
        if whichGraph=='gold': #Logic to decide which graph to display
            goldGraph()
        elif whichGraph=="btc" or "BTC":
            bitcoinGraph()
        else:
            resume=input("Would you like to resume collecting data? y or n.") #Prompts user if they want more data
            resume.lower()
            if resume=="y":
                continue #if they say yes, it continues the infinite loop
            else:
                print("goodbye.")
                break #if they say no, it stops the infinite loop
    else: #if someone doesn't want to see a graph, they're prompted to resume collecting
            resume=input("Would you like to resume collecting data? y or n.")
            resume.lower()
            if resume=="y":
                continue
            else:
                print("goodbye.")
                break 
                

    
                

