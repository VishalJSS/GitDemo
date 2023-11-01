import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)

"""
    cars  passings
0    BMW         3
1  Volvo         7
2   Ford         2
"""

print(pd.__version__)     #2.1.2

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
"""
0    1
1    7
2    2
dtype: int64
"""
print(myvar[0])   #1

myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
"""
x    1
y    7
z    2
dtype: int64
"""

print(myvar["y"])   #7

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
"""
day1    420
day2    380
day3    390
dtype: int64
"""
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)

"""
day1    420
day2    380
dtype: int64
"""

#Dataframes
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
print(df)

"""
   calories  duration
0       420        50
1       380        40
2       390        45
"""
print(df.loc[0])    #calories    420
print(df.loc[[0, 1]])   #duration     50

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)

"""
      calories  duration
day1       420        50
day2       380        40
day3       390        45
"""

print(df.loc["day2"])
"""
calories    380
duration     40
Name: day2, dtype: int64
"""

df = pd.read_csv('data.csv')
print(df)

"""
         calories  duration
0  day1       420        50
1  day2       380        40
2  day3       390        45
3  day4       360        56
4  day5       365        48
5  day6       370        51
6  day7       375        53
7  day8       378        58
8  day9       382        60
9  day10      385        62
"""

df = pd.read_csv('data.csv')
print(df.to_string())

"""
         calories  duration
0  day1       420        50
1  day2       380        40
2  day3       390        45
3  day4       360        56
4  day5       365        48
5  day6       370        51
6  day7       375        53
7  day8       378        58
8  day9       382        60
9  day10      385        62
"""
df = pd.read_csv('data.csv')
print(df.head(10))

"""
         calories  duration
0  day1       420        50
1  day2       380        40
2  day3       390        45
3  day4       360        56
4  day5       365        48
5  day6       370        51
6  day7       375        53
7  day8       378        58
8  day9       382        60
9  day10      385        62
"""
print(pd.options.display.max_rows)   #60

print(df.head())
"""
         calories  duration
0  day1       420        50
1  day2       380        40
2  day3       390        45
3  day4       360        56
4  day5       365        48
"""
print(df.tail())

"""
5  day6       370        51
6  day7       375        53
7  day8       378        58
8  day9       382        60
9  day10      385        62
"""

print(df.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 1 columns):
 #   Column                    Non-Null Count  Dtype 
---  ------                    --------------  ----- 
 0         calories  duration  10 non-null     object
dtypes: object(1)
memory usage: 208.0+ bytes
None
"""

pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)

"""
         calories  duration
0  day1       420        50
1  day2       380        40
2  day3       390        45
3  day4       360        56
4  day5       365        48
5  day6       370        51
6  day7       375        53
7  day8       378        58
8  day9       382        60
9  day10      385        62
"""

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)
print(df)
"""
   Duration  Pulse  Maxpulse  Calories
0        60    110       130       409
1        60    117       145       479
2        60    103       135       340
3        45    109       175       282
4        45    117       148       406
5        60    102       127       300
"""

df = pd.read_json('data.json')
print(df.to_string())

"""
   Duration  Pulse
0        60    110
1        60    117
2        60    103
3        45    109
4        45    117
5        60    102
"""

df = pd.read_csv('clear_data')
new_df = df.dropna()      #If you need to change original df.dropna(inplace = True)
print(new_df.to_string())

#df = pd.read_csv('clear_data')
#df.fillna(130)

#df = pd.read_csv('data.csv')
#df["Calories"].fillna(130, inplace = True)    #To specifically fill a column

#Mean = the average value (the sum of all values divided by number of values).
#df = pd.read_csv('data.csv')
#x = df["Calories"].mean()
#df["Calories"].fillna(x, inplace = True)

#Median = the value in the middle, after you have sorted all values ascending.
#x = df["Calories"].median()
#df["Calories"].fillna(x, inplace = True)

#Mode = the value that appears most frequently.
#x = df["Calories"].mode()[0]
#df["Calories"].fillna(x, inplace = True)

#df['Date'] = pd.to_datetime(df['Date'])
#print(df.to_string())

#df.dropna(subset=['Date'], inplace = True)   #Remove value

#df.loc[7, 'Duration'] = 45

#for x in df.index:
#  if df.loc[x, "Duration"] > 120:
#    df.loc[x, "Duration"] = 120

#for x in df.index:           #To Delete row
#  if df.loc[x, "Duration"] > 120:
#    df.drop(x, inplace = True)

#print(df.duplicated())

#df.drop_duplicates(inplace = True)   #To delete duplicate

#df.corr()