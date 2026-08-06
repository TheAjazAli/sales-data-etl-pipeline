import pandas as pd 
df= pd.read_csv('data/Sales_data.csv')
print(df.head())
print(df.info())

null_percent=df.isnull().sum()/len(df)*100
print(null_percent)

# data Cleaning part of removing the null values from columns
df['Size'] = df['Size'].fillna('Unknown')
df['Units_Sold']=df['Units_Sold'].fillna(df['Units_Sold'].median())
df['MRP']=df['MRP'].fillna(df['MRP'].median())
df['Discount_Applied'] = df['Discount_Applied'].fillna(0)

# convert to datetime
df['Order_Date']= pd. to_datetime(
    df['Order_Date'],
    errors='coerce',
    dayfirst=True
)
# negative to positive numbers in the Units_Sold and Revenue columns
df['Units_Sold'] = df['Units_Sold'].abs()
df['Revenue'] = df['Revenue'].abs()

# the region wise inconsistent data
df['Region'] =df['Region'].replace({
   'Hyd' : 'Hyderabad',
   'hyderbad' : 'Hyderabad',
   'Bangalore': 'Bengaluru',
   'bengaluru' : 'Bengaluru',
})

# recalculate the revenue column by multiplying the units sold with the MRP 
df ['Revenue']=df['Units_Sold']*df['MRP']*(1-df['Discount_Applied']/100)

# show the cleaned data
print(df.head(50))
print(df['Region'].unique())
print(df['Region'].value_counts())
print(df.info())
# the negative number in the Units_Sold column is not possible, so we will replace it with the median value of the column
df['Units_Sold']= df['Units_Sold'].abs()

# the profit column has some negative values, which is not possible, so we will replace it with the median value of the column
df.to_csv("cleaned_sales_data.csv", index=False)
