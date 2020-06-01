# exercise 1

# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales["weekly_sales"].mean())

# Print the median of weekly_sales
print(sales["weekly_sales"].median())

# ----//---- ----//---- ----//---- ----//---- ----//---- ----//---- 
# exercise 2

# Print the maximum of the date column
print(sales["date"].max())

# Print the minimum of the date column
print(sales["date"].min())

# ----//---- ----//---- ----//---- ----//---- ----//---- ----//---- 
# exercise 3

# Import NumPy and create custom IQR function
import numpy as np
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr,np.median]))

# ----//---- ----//---- ----//---- ----//---- ----//---- ----//---- 
# exercise 4

# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values("date")

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])

# ----//---- ----//---- ----//---- ----//---- ----//---- ----//---- 
# exercise 5

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store","type"])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store","department"])
print(store_depts.head())

# Subset the rows that are holiday weeks and drop duplicate dates
holiday_dates = sales[sales["is_holiday"]].drop_duplicates("date")

# Print date col of holiday_dates
print(holiday_dates["date"])

# ----//---- ----//---- ----//---- ----//---- ----//---- ----//---- 
# exercise 6

# Count the number of stores of each type
store_counts = stores["store_type"].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = stores["store_type"].value_counts(normalize=True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = departments["department_num"].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = departments["department_num"].value_counts(sort=True, normalize=True)
print(dept_props_sorted)

# ----//---- ----//---- ----//---- ----//---- ----//---- ----//---- 
# exercise 7








# ----//---- ----//---- ----//---- ----//---- ----//---- ----//---- 
# exercise 8