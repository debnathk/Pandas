#Some basic methods and their application in pandas.
#Importing Pandas to use the methods.
import pandas as pd

#To create DataFrames.
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})

#To create DataFrames using index.
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
             
#To create Series.
pd.Series([1, 2, 3, 4, 5])

#To create Series using index.
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
