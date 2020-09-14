#Some basic methods and their application in pandas.
#Importing Pandas to use the methods.
import pandas as pd

#---------------------------------------------------------------------------------------------------

#Creating Data files - DataFrames & Series

#To create DataFrames.
first_df = pd.DataFrame({'A': [50, 21, 34, 99, 21, 231], 'B': [131, 2, 342, 563, 90, 88], 'C' : [12, 22, 55, 98, 94, 21], 'D' : [11, 236, 54, 75, 91, 20]})
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


#Reading Data files - Comma Separated Values(CSV)
first_df.to_csv("first_df.csv")
print(first_df.shape)
print("\n")
print(first_df.head())

#--------------------------------------------------------------------------------------------------------

#Native accessors
print(first_df)

#To print the A column elements
print(first_df.A)
print(first_df['A']
print(first_df.C)
print(first_df['C']      
      
#To print a specific element of Yes column
print(first_df['A'][0])

   
      
#Indexing
#Index-based selection     
print(first_df.iloc[0])
      
#To get a column with iloc      
print(first_df.iloc[:, 0])  
print(first_df.iloc[:4, 0])      
print(first_df.iloc[1:4, 0])

#To pass a list
print(first_df.iloc[[0, 1, 2], 2])     

#To get last 3 elements
print(first_df.iloc[-3: ])    
      
      
#Label-based selection
print(first_df.loc[0, 'B'])
print(first_df.loc[:, ['A', 'B', 'D']])      
      
#Choosing between iloc and loc - 
#iloc uses the Python stdlib indexing scheme,
#where the first element of the range is included and the last one excluded. 
#So 0:10 will select entries 0,...,9. 
#loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.   
      

      
#Manupulating the index
print(first_df.set_index("D"))  
      
    
      
#Conditional Selection
print(first_df.A == 21)
print(first_df.loc[first_df.A == 21])     
print(first_df.loc[(first_df.A == 21) & (first_df.C ==21)])      
print(first_df.loc[(first_df.A == 21) | (first_df.C ==21)])     
print(first_df.loc[first_df.A.isin([50, 99])]) 
print(first_df.loc[first_df.A.notnull()])      

      
      
#Assigning Data
first_df['A'] = 100
print(first_df['A'])  
      
first_df['B'] = range(len(first_df), 0, -1)
print(first_df['B'])   
      
#-----------------------------------------------------------------------------------------------------------      
            
#Summary functions
      
print(first_df.C.describe())   
      
#To get the `mean`
print(first_df.C.mean())       

#To check the unique values
print(first_df.C.unique())       
      
#To count each values
print(first_df.C.value_counts()) 
      
      
#Maps
#Using map() function      
first_df_C_mean = first_df.C.mean()
print(first_df.map(lambda p: p - first_df_C_mean))   
      
#Using apply() function
def remean_C(row):
      row.C = row.C - first_df_C_mean
      return row    
print(first_df.apply(remean_C, axis = 'columns'))     
      
#----------------------------------------------------------------------------------------------------------------     
      
#Groupwise analysis
#Using value_counts() function
print(first_df.D.value_counts())    
      
#Using min() function
print(first_df.groupby('C').D.min())
      
#using apply() function
print(first_df.groupby('C').apply(lambda df: df.A.iloc[0]))
print(first_df.groupby(['C', 'A']).apply(lambda df: df.loc[df.A.idxmax()]))
      
#Using agg() function
print(first_df.groupby(['C']).A.agg([len, min, max]))   
      
      
#Multi - indexes
first_df_2 = first_df.groupby(['A', 'C']).description.agg([len])
print(first_df_2)  
      

#Sorting
print(first_df_2.sort_values(by='len', ascending=False))
      
#-----------------------------------------------------------------------------------------------------------------      
      
      
      
      
      
      
      
      
     
      
      
      
      
      
      
      

























