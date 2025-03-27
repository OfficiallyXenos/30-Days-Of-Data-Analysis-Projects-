# -*- coding: utf-8 -*-
"""Customer Orders Merging & Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MwmUtaTLyJoQ0cSW6Syb5-V2GcDgvC5W
"""

# import the pandas library as pd to work on data
import pandas as pd

# loading the orders and customers data into pandas for analysis
df_orders, df_customers, new_customers, new_orders, df_payments = map(
    pd.read_csv,
    ['/content/orders.csv',
     '/content/customers.csv',
     '/content/new_customers.csv',
     '/content/new_orders.csv',
     '/content/payments.csv']
    )

# printing the first 5 rows of the two datasets
df_orders.head()

df_customers.head()

df_orders.shape, df_customers.shape

"""# 1️⃣ Basic Merging & Joining"""

# performing an inner join on the two datasets on the customer_id column
inner_df = pd.merge(df_orders, df_customers, on='Customer_ID')
inner_df.head()

# performing a left join on the same column
left_df = pd.merge(df_orders, df_customers, on='Customer_ID', how='left')
left_df.head()

# performing a right join on the same column
right_df = pd.merge(df_orders, df_customers, on='Customer_ID', how='right')
right_df.head()

# performing an outer join on the same column
outer_df = pd.merge(df_orders, df_customers, on='Customer_ID', how='outer')
outer_df.head()

"""# 2️⃣ Advanced Merging with Multiple Keys"""

# subsetting the outer_df dataframe to find the customers who didn't order
no_orders = outer_df[outer_df['Order_ID'].isna()]
print(
    f'{no_orders.shape[0]} customers out of {df_customers.shape[0]} placed no orders'
    )

# finding orders with no customer ID
orders_with_no_customers = outer_df[
    (outer_df['Customer_ID'].isna()) & (outer_df['Order_ID'].notna())
    ]

print(
    f'{orders_with_no_customers.shape[0]} orders out of {df_orders.shape[0]} had no customers'
    )

# count the number of customers with over 5 orders
over_5 = inner_df[inner_df['Quantity'] > 5.0]

print(
    f'The number of customers with orders above 5 are {over_5.shape[0]}'
)

#Counting how many Gold & Platinum customers have placed an order.
gold_platinum = inner_df[
    (inner_df['Membership_Level'] == 'Gold') | (inner_df['Membership_Level'] == 'Platinum')
    ]

print(
    f'The number of customers with Gold or Platinum membership are {gold_platinum.shape[0]}'
)

"""# 3️⃣ Using `.concat()` for Stacking Data"""

# stacking the datasets using `concat()`
concat_customers_df = pd.concat([df_customers, new_customers])
concat_customers_df.head()

concat_orders_df = pd.concat([df_orders, new_orders])
concat_orders_df.head()

#checking for duplicates
if concat_customers_df.duplicated().sum() > 0:
  print(
      f'There are {concat_customers_df.duplicated().sum()} duplicates in the concat_customers_df dataframe'
      )
else:
  print('There are no duplicates in the concat_customers_df dataframe')

if concat_orders_df.duplicated().sum() > 0:
  print(
      f'There are {concat_orders_df.duplicated().sum()} duplicates in the concat_orders_df dataframe'
      )
else:
  print('There are no duplicates in the concat_orders_df dataframe')

"""# 4️⃣ Using merge_asof() for Time-Based Merging"""

# Use merge_asof() to match the closest payment transaction to each order.
concat_orders_df['Order_Date'] = pd.to_datetime(concat_orders_df['Order_Date'])
df_payments['Payment_Date'] = pd.to_datetime(df_payments['Payment_Date'])

merged_df = pd.merge_asof(
    concat_orders_df.sort_values('Order_Date'),
    df_payments.sort_values('Payment_Date'),
    by = 'Customer_ID',
    left_on='Order_Date',
    right_on='Payment_Date',
    direction= 'backward')

merged_df.shape

missing_payments = merged_df[merged_df["Payment_Date"].isnull()]
print(f"Number of orders with no matching payment:{missing_payments.shape[0]}")
print(f"Number of orders with matching payment:{merged_df.shape[0] - missing_payments.shape[0]}")

underpaid_orders = merged_df[merged_df["Payment_Amount ($)"] < merged_df["Total_Amount ($)"]]
print(f"Number of underpaid orders: {underpaid_orders.shape[0]}")

print(merged_df.duplicated().sum())
print(merged_df.isna().sum())

merged_df.to_csv("merged_customer_orders.csv", index=False)

from google.colab import files
files.download("merged_customer_orders.csv")