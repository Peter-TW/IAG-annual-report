import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np
import seaborn as sns

# Get data
data = pd.read_excel("IAGExcel.xlsx")

### Cash and cash equivalents (figure 16)
sns.lineplot(data.Year,data["Cash and cash equivalents"],marker="o")
for x1,y1 in data.iterrows():
    plt.text(x1+2011,y1["Cash and cash equivalents"]*1.01,int(y1["Cash and cash equivalents"]),ha="center")
plt.title("Cash and Cash Equivalents")
plt.ylabel("Cash and cash equivalents € million")
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.show()

### Operating cost (figure 15)
sns.lineplot(data.Year,data["Operating cost"],marker="o")
for x1 ,y1 in data.iterrows():
    plt.text(x1+2011,y1["Operating cost"]*1.01,int(y1["Operating cost"]),ha="center")
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.ylabel("Operating cost € million")
plt.title("Operating Cost")
plt.show()

### Cargo revenue (figure 14) (figure 12)
plt.plot(data.Year,data["Passenger revenue"])
sns.set()
plt.plot(data.Year,data["Cargo revenue"],marker="o")
# plt.plot(data.Year,data["Other revenue"])
plt.ylabel("revenue € million ")
plt.title("Cargo Revenue")
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.show()

### leverage (figure 13)
leverage = ((data["Total liabilities"]/(data["Total liabilities"]+data["Total equity"]))*100).round(2)
plt.plot(data.Year,leverage,marker="o")
for x1,y1 in enumerate(leverage):
    plt.text(x1+2011,y1+0.8,str(y1)+"%",ha="center")
plt.title("Leverage Percentage")
plt.ylabel("Percentage % ")
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.show()

### Return on assets (figure 11)
ROA = ((data["Net income"]/data["Total assets"])*100).round(2)
NIP = ((data["Net income"]/data["Total revenue"])*100).round(2)
ROA_data = pd.DataFrame({"Year":data.Year,"Return on assets":ROA,"Net income profit":NIP})
sns.set()
plt.plot(ROA_data.Year,ROA_data["Return on assets"],label="Return on assets",marker="o")
for x1,y1 in ROA_data.iterrows():
    plt.text(x1+2011,y1["Return on assets"]+1.25,y1["Return on assets"],ha="center")
plt.legend()
plt.title("Return On Assets (ROA)")
plt.ylabel("Percentage %")
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.show()

### haul data (figure 10)
haul = data.loc[4:]
y=haul.fleet_in_service
sns.set()
sns.lineplot(x=haul.Year, y=haul.short_haul,label="Short-haul",color="r", marker="o")
sns.lineplot(x=haul.Year, y=haul.long_haul,label="Long-haul",color="g", marker="o")
plt.bar(haul.Year,haul.fleet_in_service,label="total",color="lightsteelblue",alpha=0.8)
for x1, y1 in enumerate(haul.fleet_in_service[::-1]):
    plt.text(x1+2014.8,y1,int(y1))
plt.ylabel("Fleet in service count")
plt.title("Fleet Segments")
plt.legend(loc="center right")
plt.show()

### Current ratio (figure 9)
sns.set()
dd = data["Current assets"]/data["Current liabilities"]
sns.lineplot(data.Year,dd,marker="o",label="Current ratio")
plt.title("Current Ratio Chart")
plt.ylabel("Current ratio")
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.show()

### Adjested debt and current assets (figure 8)(figure 7)
NB = data.loc[3:]
fig, ax = plt.subplots()
plt.bar(NB.Year,NB["Current assets"],label="Current assets",color="tab:orange")
for x1,y1 in enumerate(NB["Current assets"]):
    plt.text(x1+2014, y1, y1,ha='center',fontsize=10)
plt.plot(NB.Year,NB["Adjusted net debt"],label="Adjusted net deb",color ="tab:red",marker="o")
plt.plot(NB.Year,NB["Net_debt"],label="Net_debt",color ="tab:blue",marker="o")
plt.legend(loc="best")
plt.title("Current Assets and Net Debt")
plt.xlabel("Year")
plt.ylabel(" € Million")
plt.show()

###2020 operation segements (figure 6)
segments=["Employee costs","Fuel, oil costs and emissions charges", "Handling, catering and other operating costs",
          "Landing fees and en-route charges", "Engineering and other aircraft costs", "Property, IT and other costs",
"Selling costs","Depreciation, amortisation and impairment", "Currency differences"]
cos= [3560, 3735, 1340,918, 1456, 782, 405, 2955,81]
plt.pie(cos,labels=segments,pctdistance = 0.7,
        textprops = {"fontsize":10},autopct = "%1.1f%%",
        explode = [.05,.05,0,0,0,0,0,0,0])
plt.title("2020 Expenditure On Operations Segments")
plt.show()

### brent-crude-oil with IAG cost (figure 5)
oil=pd.read_csv("brent-crude-oil-prices-10-year-daily-chart.csv")
oil_mea = oil.groupby("year")["Brent oil price"].mean().round(2).reset_index()
CORR =pd.DataFrame({"Fuel cost": data["Fuel oil costs"][1::],"Brent price": oil_mea["Brent oil price"][1::]})
fig, ax=plt.subplots()
ax=sns.lineplot(x=data.Year,y=data["Fuel oil costs"],marker="o",label="Fuel oil costs",color="r")
plt.legend(loc="center left")
plt.ylabel("Fuel oil costs € million")
ax2=ax.twinx()
ax2=sns.lineplot(x=oil_mea.year,y=oil_mea["Brent oil price"],marker="o",label="Brent oil price",color="g")
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.legend(loc="upper left")
plt.title("10 years trend between Brent and IAG cost")
plt.show()


### Total revenue and operating profit  (figure 4)
sns.set()
RE=data[["Year","Total revenue","Operating profit"]]
x = np.arange(len(RE.Year))
width = 0.35
fig, ax = plt.subplots()
ax.bar(x - width/2, data["Total revenue"], width, label="Total revenue")
ax.bar(x + width/2, data["Operating profit"], width, label="Operating profit")
ax.set_ylabel("Total revenue € million")
ax.set_xticks(x)
ax.set_xticklabels(RE.Year)
for x1,y1 in enumerate(data["Total revenue"]):
    plt.text(x1-0.2, y1+200, y1,ha='center',fontsize=10)
for x2,y2 in enumerate(data["Operating profit"]):
    plt.text(x2+0.2,y2+200,y2,ha='center',fontsize=10)
ax.legend()
plt.title("Total Revenue and Operating Profit")
plt.show()

### Passenger numbers (thousands) (figure 3)
sns.lineplot(x=data.Year,y=data["Passenger numbers (thousands)"],marker="o")
plt.bar(data.Year,data["Passenger numbers (thousands)"])
sns.set()
sns.barplot(x=data.Year,y=data["Passenger numbers (thousands)"],order=data.Year,palette="flare")
for x1,y1 in data.iterrows():
    plt.text(x1,y1["Passenger numbers (thousands)"]*1.005,int(y1["Passenger numbers (thousands)"]),ha="center")
plt.title("Passenger Numbers")
plt.show()

### 2019 revenue segements (figure 2)
select_year=data[data["Year"]==2019]
year_num = np.array([int(select_year["Passenger revenue"].values),
                     int(select_year["Cargo revenue"].values),
                     int(select_year["Other revenue"].values)])
labels=["Passenger revenue","Cargo revenue","Other revenue"]
plt.pie(year_num,labels=labels,autopct='%1.1f%%',explode = [.1,0,0])
plt.title("2019 Revenue Segments Percentage")
plt.show()

### History Revenue (figure 1)
fig,ax=plt.subplots()
sns.set()
ax=sns.barplot(y=data["Total revenue"],x=data["Year"],order=data.Year)
for x1,y1 in data.iterrows():
    ax.text(x1,y1["Total revenue"],int(y1["Total revenue"]),ha="center")
plt.ylabel("Total revenue € million")
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.title("Total revenue")
plt.show()


