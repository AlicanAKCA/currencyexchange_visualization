#####################################################################################
#                            Dec 16 2020                                            #
#                            github.com/Alicanakca                                  #
#####################################################################################
import requests
import json
from datetime import datetime
from matplotlib import pyplot as plt

x = [] #For dates : year-month-day
y = [] #For TRY values

currency = requests.get("https://api.exchangeratesapi.io/history?start_at=2005-1-1&end_at=2020-12-13&symbols=USD,TRY&base=USD") #Api
currency = json.loads(currency.text)
currency = currency["rates"] #There are dictionary items in "rates"
for dates in sorted(currency, key=lambda date: datetime.strptime(date, "%Y-%m-%d")): #I sorted the elements historically
    #print("%s: %s" % (dates, currency[dates]))
    x.append(dates) #Added
    y.append(currency[dates]["TRY"]) #Added

result2005 = []
result2006 = []
result2007 = []
result2008 = []
result2009 = []
result2010 = []
result2011 = []
result2012 = []
result2013 = []
result2014 = []
result2015 = []
result2016 = []
result2017 = []
result2018 = []
result2019 = []
result2020 = []
input2005 =[]
input2006 =[]
input2007 =[]
input2008 =[]
input2009 =[]
input2010 =[]
input2011 =[]
input2012 =[]
input2013 =[]
input2014 =[]
input2015 =[]
input2016 =[]
input2017 =[]
input2018 =[]
input2019 =[]
input2020 =[]

i=0
while True: #I classified the years to be colored in the chart. Added to the result20xx lists. 
    #Attention! datetime.strptime(x[i], "%Y-%m-%d").YEAR -> Just year
    if datetime.strptime(x[i], "%Y-%m-%d").year == 2005:
        result2005.append(y[i])
    if datetime.strptime(x[i], "%Y-%m-%d").year == 2006:
        result2006.append(y[i])
    if datetime.strptime(x[i], "%Y-%m-%d").year == 2007:
        result2007.append(y[i])
    if datetime.strptime(x[i], "%Y-%m-%d").year == 2008:
        result2008.append(y[i])
    if datetime.strptime(x[i], "%Y-%m-%d").year == 2009:
        result2009.append(y[i])
    if datetime.strptime(x[i], "%Y-%m-%d").year == 2010:
        result2010.append(y[i])
    if datetime.strptime(x[i], "%Y-%m-%d").year == 2011:
        result2011.append(y[i])
    if datetime.strptime(x[i], "%Y-%m-%d").year == 2012:
        result2012.append(y[i])
    if datetime.strptime(x[i], "%Y-%m-%d").year == 2013:
        result2013.append(y[i])
    if datetime.strptime(x[i], "%Y-%m-%d").year == 2014:
        result2014.append(y[i])
    if datetime.strptime(x[i], "%Y-%m-%d").year == 2015:
        result2015.append(y[i])
    if datetime.strptime(x[i], "%Y-%m-%d").year == 2016:
        result2016.append(y[i])
    if datetime.strptime(x[i], "%Y-%m-%d").year == 2017:
        result2017.append(y[i])
    if datetime.strptime(x[i], "%Y-%m-%d").year == 2018:
        result2018.append(y[i])
    if datetime.strptime(x[i], "%Y-%m-%d").year == 2019:
        result2019.append(y[i])
    if datetime.strptime(x[i], "%Y-%m-%d").year == 2020:
        result2020.append(y[i])  
    i+=1
    if i >= len(x):
        break #Ended
#I added money values corresponding to years to input20xx lists
#Attention v2 : In the 15-year data set, we added the money values at the limits of the length of result20xx to input20xx.
#Example: The length of result2006 is 365. We have added 365 out of list x (sorted list) to input2006 list. They have money values here.
sumresults = len(result2005)
for a in range(0,sumresults):   
    input2005.append(x[a])
sumresults+= len(result2006)
for a in range(sumresults - len(result2006),sumresults):
    input2006.append(x[a])
sumresults += len(result2007)

for a in range(sumresults-len(result2007),sumresults):
    input2007.append(x[a])
sumresults += len(result2008)

for a in range(sumresults-len(result2008),sumresults):
    input2008.append(x[a])
sumresults += len(result2009)

for a in range(sumresults-len(result2009),sumresults):
    input2009.append(x[a])
sumresults += len(result2010)

for a in range(sumresults-len(result2010),sumresults):
    input2010.append(x[a])
sumresults += len(result2011)

for a in range(sumresults-len(result2011),sumresults):
    input2011.append(x[a])
sumresults += len(result2012)

for a in range(sumresults-len(result2012),sumresults):
    input2012.append(x[a])
sumresults += len(result2013)

for a in range(sumresults-len(result2013),sumresults):
    input2013.append(x[a])
sumresults += len(result2014)

for a in range(sumresults-len(result2014),sumresults):
    input2014.append(x[a])
sumresults += len(result2015)

for a in range(sumresults-len(result2015),sumresults):
    input2015.append(x[a])
sumresults += len(result2016)

for a in range(sumresults-len(result2016),sumresults):
    input2016.append(x[a])
sumresults += len(result2017)

for a in range(sumresults-len(result2017),sumresults):
    input2017.append(x[a])
sumresults += len(result2018)

for a in range(sumresults-len(result2018),sumresults):
    input2018.append(x[a])
sumresults += len(result2019)

for a in range(sumresults-len(result2019),sumresults):
    input2019.append(x[a])
sumresults += len(result2020)

for a in range(sumresults-len(result2020),sumresults):
    input2020.append(x[a])
#art title and Axis names added.
#Colors added.
#The colors of the year-value function determined
plt.xlabel('Dates')
plt.ylabel('Dollar to TRY')
plt.title("Currency Exchange Rates Between 2005-2020 in Turkey")
plt.plot(input2005,result2005, color = "xkcd:purple" , label="2005")
plt.plot(input2006,result2006, color = "xkcd:green", label="2006")
plt.plot(input2007,result2007, color = "xkcd:blue", label="2007")
plt.plot(input2008,result2008, color = "xkcd:brown", label="2008")
plt.plot(input2009,result2009, color = "xkcd:dark pink", label="2009")
plt.plot(input2010,result2010, color = "xkcd:dark turquoise", label="2010")
plt.plot(input2011,result2011, color = "xkcd:greyish blue", label="2011")
plt.plot(input2012,result2012, color = "xkcd:dark mauve", label="2012")
plt.plot(input2013,result2013, color = "xkcd:dark plum", label="2013")
plt.plot(input2014,result2014, color = "xkcd:gold", label="2014")
plt.plot(input2015,result2015, color = "xkcd:dark", label="2015")
plt.plot(input2016,result2016, color = "xkcd:radioactive green", label="2016")
plt.plot(input2017,result2017, color = "xkcd:purplish brown", label="2017")
plt.plot(input2018,result2018, color = "xkcd:peacock blue", label="2018")
plt.plot(input2019,result2019, color = "xkcd:rust orange", label="2019")
plt.plot(input2020,result2020, color = "xkcd:red", label="2020")
plt.legend(loc="upper left")
plt.xticks(color = "white",rotation=90)
plt.show()

