#Some basic methods and their application in pandas.
#Importing Pandas to use the methods.
import pandas as pd

#To create DataFrames.
first_df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(first_df)
second_df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
print(second_df)

#To create DataFrames using index.
third_df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
print(third_df)



#To create Series.
first_se = pd.Series([1, 2, 3, 4, 5])
print(first_se)

#To create Series using index.
second_se = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(second_se)
