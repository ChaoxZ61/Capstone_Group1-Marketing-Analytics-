# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Stars, Alcohol, BikeParking, BusinessAcceptsCreditCards, Caters, GoodForKids, HasTV, NoiseLevel, OutdoorSeating, RestaurantsAttire, RestaurantsDelivery, RestaurantsGoodForGroups, RestaurantsPriceRange2, RestaurantsReservations, RestaurantsTakeOut, WiFi)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
from joblib import dump,load
import pandas as pd
import numpy as np
import xgboost as xgb
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import LabelEncoder

replace = list(dataset['Alcohol'].unique())
dataset.replace(replace,[np.nan,'2','0','1'],inplace=True)

replace = list(dataset['NoiseLevel'].unique())
replace.remove(np.nan)
dataset.replace(replace,['1','0','2','3'],inplace=True)

replace = list(dataset['RestaurantsAttire'].unique())
replace.remove(np.nan)
dataset.replace(replace,['0','1','2'],inplace=True)

replace = list(dataset['WiFi'].unique())
replace.remove(np.nan)
dataset.replace(replace,['2','0','1'],inplace=True)

for i in dataset.columns:
    dataset[i] = pd.to_numeric(dataset[i])

dataset['Stars'] = dataset['Stars'].astype(int)

X = dataset.copy()
X.drop('Stars',axis=1,inplace=True)
y = dataset['Stars'].copy()
le = LabelEncoder()
y = le.fit_transform(y)


clf = load('D:\Documents\Dev10\CourseNotes\Module11_Capstone\Capstone_MachineLearning.model')
y_predicted = clf.predict(X)

labels = [1,2,3,4,5]
ticks = [0,1,2,3,4]
cm = confusion_matrix(y,y_predicted)
cmd = ConfusionMatrixDisplay(confusion_matrix=cm)
cmd.plot()
plt.xlabel('Predicted Stars')
plt.ylabel('Actual Stars')
plt.xticks(ticks,labels)
plt.yticks(ticks,labels)
plt.title(f'Matthews Correlation Coefficient: 0.265')
plt.show()
