# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Text, Stars)
# dataset = dataset.drop_duplicates()


# Paste or type your script code here:

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataset['Length of Text'] = dataset['Text'].str.len()
dataset.drop(['Text'], axis=1)

dataset = dataset.groupby('Stars',as_index=False)['Length of Text'].mean()
axes = plt.axes()


dataset.plot(kind="scatter", x = 'Stars', y = 'Length of Text', color = 'red',  s = 45)

plt.rc('axes', labelsize = 20)
plt.xticks(np.arange(1, 6, 1.0))
plt.yticks(np.arange(350, 750, 50))

plt.show()