import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import grocery

#task1
print('_____________task1____________')
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
df = pd.DataFrame(grocery.data[:,1:],
                  index=grocery.data[:,0], columns=months)
print(df)
print('_____________task2___________________')
#task2

march = df['Mar']
march1996 = march.loc[1996]   #inclusive
march_range = march.loc[1998:2003]
print(march)
print(march1996)
print(march_range)

print('_____________task3___________________')
# task3
march = df['Mar']
temp = march.iloc[4]  # Retrieve 5th item (1996, since 0-indexed)
print(np.allclose(temp, march1996))

# Use .loc[1996] instead of iloc[1996] to get 1996 data
march1996_2 = march.loc[1996]

temp_slice = march.iloc[6:12]  # Slice from 7th to 12th item (1998-2003)
print(np.allclose(temp_slice, march_range))

# temp = march.iloc[4]
# print(np.allclose(temp, march1996))
# march1996 = march.iloc[1996]
# temp = march.iloc[6:12]  # inclusive and exclusive , slicing with array 
# print(np.allclose(temp,march_range)) 

print('_____________task4___________________')
#task4
#compare between what is obtained using loc and iloc
#task5
#o the same as #4 except with the columns April, June, and December.
df3 = df.loc[1996, 'Aug':'Oct'] 
df4 = df.loc[1998:2003, 'Aug':'Oct']
print(df3)
print(df4)

print('_____________task5___________________')
temp = df.iloc[4, [3,5,11]]
print(temp)
temp = df.iloc[6:12, [3,5,11]] #upper bound inclusive ,
print(np.allclose(temp,df4)) 

print('_____________task6___________________')
#task6
# January values are greater than 45,000 
bigjan = df[df['Jan'] > 45000] 
print(bigjan)

print('_____________task7___________________')
#task7
#save all values of bigjan that are greater than 48,000 millions of USD and less than 50,000
subset = bigjan[(bigjan> 48000) & (bigjan < 50000)]
print(subset)

print('_____________task8___________________')
#task8
#Create a copy of df and sort that so the rows are ordered in descending years
df_reverse = df.copy().sort_index(ascending=False)
print(df_reverse)

print('_____________task9___________________')
#task 9 
valid = df4[(df4 < 34000) | (df4 >=35000)]
print(valid.sort_values(by='Dec', ascending=False).iloc[1,[0,1]])



