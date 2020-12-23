#   Load data into pandas

import pandas as pd 
df=pd.read_csv('pokemon_data.csv')
print(df)
print(df.head(3)) #print the top 3
print(df.tail(3)) #print the bottom 3

df_txt=pd.read_csv('pokemon_data.txt' ,delimiter='\t') #for txt file seperate with a tab
df_xlsx=pd.read_excel('pokemon_data.xlsx') #for excel file

#      Reading Data (Getting rows,colums,cells,headers,...)
    #Read Headers

print(df.columns)
    
    #Read each column

print(df['Name'])
print(df['Name'][0:5]) #print the top 5
print(df[['Name','Type 1','HP']]) #print Name Type1 and HP column
    
    #Read each Row

print(df.iloc[0]) #priint the first row
print(df.iloc[0:5]) #print top5

    #Read a specific locat (R,C)

print(df.iloc[1,2])

#Iterate through each row

for index, row in df.iterrows():
    print(index,row['Name'])

#Gettibg rows based on a specific condition

print(df.loc[df['Type 1']=="Fire"]) #print row with type1 is fire

#High Level description of you data

df.describe() #give us all the decription min mac count ...

#Sorting values 

df.sort_values('Name')
df.sort_values('Name',ascending=False)
df.sort_values(['Name','HP'])
df.sort_values(['Type 1','HP'], ascending=[1,0])

#Making Changes to 
    #Adding a Column

df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

    #Deleting a column

df=df.drop(columns=['Total'])
#Summing Multiple Columns to Create new Column

df['Total']=df.iloc[:,4:10].sum(axis=1)

#Rearranging columns

cols=list(df.columns.values) #cols in a list
df=df[cols[0:4]+[cols[-1]]+cols[4:12]]#Total col to 4 instead of 12

#Saving our data

df.to_csv('modified.csv', index=False)
df.to_csv('modified.txt',index=False ,sep='\t')

#Filetring data

df.loc[df['Type 1'] == 'Grass']
df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]
df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]
new_df=df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70) ]
new_df.to_csv('filtered.csv')

#Reset Index

new_df=new_df.reset_index()
new_df=new_df.reset_index(drop=True)
new_df=new_df.drop(columns=['index'])
new_df.reset_index(drop=True,inplace=True) #if you dont want to create a new data frame use this

#Regex Filtering(filter based on textual patterns)

df.loc[df['Name'].str.contains('Mega')] #show names that contains Mega
df.loc[~df['Name'].str.contains('Mega')] #l3ks
import re
df.loc[df['Type 1'].str.contains('Fire|Grass',regex=True)]
df.loc[df['Type 1'].str.contains('fiRe|grAss', flags=re.I ,regex=True)] #to ignore uppercases
df.loc[df['Name'].str.contains('pi[a,z]*', flags=re.I ,regex=True)] #name contains pi * meant to say zero or more
df.loc[df['Name'].str.contains('^pi[a,z]*', flags=re.I ,regex=True)] #start with pi

#Conditional Changes

df.loc[df['Type 1'] == 'Fire','Type 1'] = 'Ikhn' #changing fire to ikhn in type1
df.loc[df['Type 1'] == 'Fire','Legendary'] = 'True' #ch,agign legen of type 1 fire to true
df.loc[df['Total'] > 500 , ['Generation','Legendary']] = 'TEST VALUE' # change gene and leg of total>500 to test value
df.loc[df['Total'] > 500 , ['Generation','Legendary']] = ['TEST VALUE'
df.loc[df['Total'] > 500 , ['Generation','Legendary']] = ['TEST GENE','TEST LEGE']
df =pd.read_csv('modified.csv')

#Aggregate statistics using group by (sum,mean,counting)

df.groupby(['Type 1']).mean()
df.groupby(['Type 1']).mean().sort_values('Defense',ascending=False) #sort by defende desc
df.groupby(['Type 1']).sum()
df.groupby(['Type 1']).count()

df = pd.read_csv('modified.csv')

df['count'] = 1

df.groupby(['Type 1', 'Type 2']).count()['count']

#Workin with large amounts of data



new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('modified.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()
    
    new_df = pd.concat([new_df, results])

    print("walo ")

