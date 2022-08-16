# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Stars, Text)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

df = dataset.copy()

one = df.loc[df['Stars'] == 1.0].copy()
two= df.loc[df['Stars'] == 2.0].copy()
three = df.loc[df['Stars'] == 3.0].copy()
four = df.loc[df['Stars'] == 4.0].copy()
five = df.loc[df['Stars'] == 5.0].copy()

aDict = {}
for i in one.index:
    words = one['Text'][i].split()
    for j in words:
        if j not in aDict.keys():
            aDict[j] = 1
        else:
            aDict.update({j:aDict[j]+1})
sortedTuple = sorted(aDict.items(), key=lambda item: item[1],reverse=True)
sortedDict = {k: v for k, v in sortedTuple}
oneDict = {'food':float(sortedDict['food']/len(one.index)),'order':float(sortedDict['order']/len(one.index)),'place':float(sortedDict['place']/len(one.index)),\
    'never':float(sortedDict['never']/len(one.index)),"didn't":float(sortedDict["didn't"]/len(one.index))}

aDict = {}
for i in two.index:
    words = two['Text'][i].split()
    for j in words:
        if j not in aDict.keys():
            aDict[j] = 1
        else:
            aDict.update({j:aDict[j]+1})
sortedTuple = sorted(aDict.items(), key=lambda item: item[1],reverse=True)
sortedDict = {k: v for k, v in sortedTuple}
twoDict = {'food':float(sortedDict['food']/len(two.index)),'good':float(sortedDict['good']/len(two.index)),'place':float(sortedDict['place']/len(two.index)),\
    'ordered':float(sortedDict['ordered']/len(two.index)),"time":float(sortedDict["time"]/len(two.index))}

aDict = {}
for i in three.index:
    words = three['Text'][i].split()
    for j in words:
        if j not in aDict.keys():
            aDict[j] = 1
        else:
            aDict.update({j:aDict[j]+1})
sortedTuple = sorted(aDict.items(), key=lambda item: item[1],reverse=True)
sortedDict = {k: v for k, v in sortedTuple}
threeDict = {'food':float(sortedDict['food']/len(three.index)),'good':float(sortedDict['good']/len(three.index)),'place':float(sortedDict['place']/len(three.index)),\
    'ordered':float(sortedDict['ordered']/len(three.index)),"service":float(sortedDict["service"]/len(three.index))}

aDict = {}
for i in four.index:
    words = four['Text'][i].split()
    for j in words:
        if j not in aDict.keys():
            aDict[j] = 1
        else:
            aDict.update({j:aDict[j]+1})
sortedTuple = sorted(aDict.items(), key=lambda item: item[1],reverse=True)
sortedDict = {k: v for k, v in sortedTuple}
fourDict = {'good':float(sortedDict['good']/len(four.index)),'food':float(sortedDict['food']/len(four.index)),'place':float(sortedDict['place']/len(four.index)),\
    'great':float(sortedDict['great']/len(four.index)),"time":float(sortedDict["time"]/len(four.index))}

aDict = {}
for i in five.index:
    words = five['Text'][i].split()
    for j in words:
        if j not in aDict.keys():
            aDict[j] = 1
        else:
            aDict.update({j:aDict[j]+1})
sortedTuple = sorted(aDict.items(), key=lambda item: item[1],reverse=True)
sortedDict = {k: v for k, v in sortedTuple}
fiveDict = {'food':float(sortedDict['food']/len(five.index)),'place':float(sortedDict['place']/len(five.index)),'great':float(sortedDict['great']/len(five.index)),\
    'good':float(sortedDict['good']/len(five.index)),"best":float(sortedDict["best"]/len(five.index))}

aList = [oneDict,twoDict,threeDict,fourDict,fiveDict]
uniWord = set()
for i in aList:
    for j in i.keys():
        uniWord.add(j)
df2 = pd.DataFrame(index=[1,2,3,4,5],columns=uniWord)
for i in df2.index:
    for j in df2.columns:
        try:
            df2.at[i,j] = aList[i-1][j]
        except:
            df2.at[i,j] = 0
df2['index'] = df2.index

ax = df2.plot(x='index',y=['best',"didn't",'great','food','time','order','good','ordered','place','never','service'],figsize=(16,16),kind='bar')
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
plt.xlabel('Ratings',fontsize=16)
plt.ylabel('Percenrage in Review',fontsize=16)
plt.legend(prop={'size':17})
plt.yticks(size=14)
plt.xticks(rotation=360,size=14)
plt.show()