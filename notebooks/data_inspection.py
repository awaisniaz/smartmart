
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import pandas as pd
from utlity_functions import loadData


def inspect_data():
    data = loadData('data/raw/sales.csv')
    if(data is None):
        print("Data loading failed. Please check the file path.")
        return
    # print(data.head())
    # print(data.info())
    # print(data.columns)
    # print(data.shape)
    # print(data.describe())
    # print(data['quantity_sold'].dtypes)
    # print(data.isnull().sum())
    # print(data.duplicated().sum())
    # print((data.isnull().sum()/len(data))*100)
    # print(data[data.duplicated(keep=False)].head(20))
    # print(data[data.duplicated(keep=False)].shape)
    # print(data.duplicated(subset=["date","store_id","product_id"]).sum())
    # print(data[data.duplicated(subset=["date","store_id","product_id"], keep=False)].head(20))
    # duplicates = data[data.duplicated(subset=["date","store_id","product_id"], keep=False)]
    # print(duplicates.sort_values(by=["date","store_id","product_id"]).head(20))
    # print(data[data["quantity_sold"]<0])
    # print(data[data["unit_price"]<0])
    # print(data[(data["discount"]<0) | (data["discount"]>1)])
    # print(data[data["revenue"]<0])

    # print(data[["discount","revenue","unit_price","quantity_sold"]].describe())
#     print(data[["discount","revenue","unit_price","quantity_sold"]].skew())
#     print(data[data["quantity_sold"]>36].head(20))
#     print(data["product_id"].value_counts().head(20))
#     print(data["store_id"].value_counts().head(20))
#     print(data.groupby("product_id")["quantity_sold"].agg(["count","mean","median","std","min","max"]).sort_values(ascending=False).head(20))
#     print(data.groupby("store_id")["quantity_sold"].agg(
#     ["count", "mean", "median", "std", "min", "max"]
# ).sort_values("mean", ascending=False))

    # product_demand = data.groupby("product_id")["quantity_sold"].agg(
    # ["count", "mean", "median", "std", "min", "max"]
    #  ).sort_values("mean", ascending=False)  

    # print(product_demand.head(20))

    # store_demand = data.groupby("store_id")["quantity_sold"].agg(["count", "mean", "median", "std", "min", "max"]).sort_values("mean", ascending=False)
    # print(store_demand.head(20))

    # store_product_demand = data.groupby(["store_id", "product_id"])["quantity_sold"].agg(
    # ["count", "mean", "median", "std", "min", "max"]
    # ).sort_values("mean", ascending=False)
    # print(store_product_demand.head(20))
    data["date"] = pd.to_datetime(data["date"])
    print(data["date"].min(), data["date"].max())
    print(data["date"].dtype)
    daily_demand = data.groupby("date")["quantity_sold"].sum()
    print(daily_demand.head())
    plt.figure(figsize=(14,5))
    daily_demand.plot()
    plt.title("Daily Total Demand")
    plt.xlabel("Date")
    plt.ylabel("Quantity Sold")
    plt.show()
inspect_data()

def dataVisualization():
    data = loadData('data/raw/sales.csv')
    if(data is None):
        print("Data loading failed. Please check the file path.")
        return
    data['quantity_sold'].hist(bins=50)
    
    plt.title('Distribution of Quantity Sold')
    plt.xlabel('Quantity Sold')
    plt.ylabel('Frequency')
    plt.show()
    data['unit_price'].hist(bins=50)
    plt.title('Distribution of Unit Price')
    plt.xlabel('Unit Price')
    plt.ylabel('Frequency')
    plt.show()
    

# dataVisualization()


def findOutliers():
    data = loadData('data/raw/sales.csv')
    if(data is None):
        print("Data loading failed. Please check the file path.")
        return
    Q1 = data['quantity_sold'].quantile(0.25)
    Q3 = data['quantity_sold'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data['quantity_sold'] < lower_bound) | (data['quantity_sold'] > upper_bound)]
    # print(f"Number of outliers in 'quantity_sold': {outliers.shape[0]}")
    # print(outliers.head())
    print(Q1, Q3, IQR, lower_bound, upper_bound)
    print(outliers.shape)

# findOutliers()