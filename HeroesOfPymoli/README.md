
# Heroes Of Pymoli Data Analysis

* Of the 1,163 players, 82.03% are male and 16.08% are female.

* Most of the players fall within the 20-24 age range followed by the 15-19 age range.

* The top spender spent $4.81$ total, over one and a half times the average purchase price ($2.92)

### Player Count

* Total Number of Players


```python
import pandas as pd
file = "players_complete.csv"
players = pd.read_csv(file)
```


```python
players_total = len(players)
players_total_df = pd.DataFrame({
    "Total players": [players_total]
})
players_total_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1163</td>
    </tr>
  </tbody>
</table>
</div>



### Purchasing Analysis (Total)

* Number of Unique Items
* Average Purchase Price
* Total Number of Purchases
* Total Revenue


```python
file = "purchase_data_3.csv"
purchases = pd.read_csv(file)
```


```python
file = "items_complete.csv"
items = pd.read_csv(file)
```


```python
unique = len(items["Item Name"].unique())
avg_price = purchases["Price"].mean()
total_purchases = len(purchases)
total_revenue = purchases["Price"].sum()

purchases_df = pd.DataFrame({
    "Number of Unique Items": [unique],
    "Average Purchase Price": [avg_price],
    "Total Purchases": [total_purchases],
    "Total Revenue":[total_revenue]
})

purchases_df["Average Purchase Price"] = purchases_df["Average Purchase Price"].map("${:,.2f}".format)
purchases_df["Total Revenue"] = purchases_df["Total Revenue"].map("${:,.2f}".format)

purchases_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Number of Unique Items</th>
      <th>Total Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>$2.92</td>
      <td>186</td>
      <td>78</td>
      <td>$228.10</td>
    </tr>
  </tbody>
</table>
</div>



### Gender Demographics

* Percentage and Count of Male Players
* Percentage and Count of Female Players
* Percentage and Count of Other / Non-Disclosed


```python
gender_group = players.groupby("Gender")
player_count_gender = gender_group["Player ID"].count()
player_percent_gender = (gender_group["Player ID"].count()/players_total)*100

gender_df = pd.DataFrame({
    "Percentage of Players": player_percent_gender,
    "Total Count": player_count_gender
})

gender_df["Percentage of Players"] = gender_df["Percentage of Players"].map("{:.2f}%".format)

gender_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>16.08%</td>
      <td>187</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>82.03%</td>
      <td>954</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.89%</td>
      <td>22</td>
    </tr>
  </tbody>
</table>
</div>



### Purchasing Analysis (Gender)

* The below each broken by gender
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value
  * Normalized Totals


```python
gender_purchases = purchases.groupby("Gender")
purchase_count = gender_purchases["Item ID"].count()
gender_avg_price = gender_purchases["Price"].mean()
gender_total_price = gender_purchases["Price"].sum()

gender_purchase_df = pd.DataFrame({
    "Purchase Count": purchase_count,
    "Average Purchase Price": gender_avg_price,
    "Total Purchase Value": gender_total_price
})

normalized_purchase = gender_purchase_df["Total Purchase Value"]/gender_df["Total Count"]
gender_purchase_df["Normalized Total"] = normalized_purchase

gender_purchase_df["Average Purchase Price"] = gender_purchase_df["Average Purchase Price"].map("${:.2f}".format)
gender_purchase_df["Total Purchase Value"] = gender_purchase_df["Total Purchase Value"].map("${:.2f}".format)
gender_purchase_df["Normalized Total"] = gender_purchase_df["Normalized Total"].map("${:.2f}".format)

gender_purchase_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
      <th>Normalized Total</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>$3.18</td>
      <td>13</td>
      <td>$41.38</td>
      <td>$0.22</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>$2.88</td>
      <td>64</td>
      <td>$184.60</td>
      <td>$0.19</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>$2.12</td>
      <td>1</td>
      <td>$2.12</td>
      <td>$0.10</td>
    </tr>
  </tbody>
</table>
</div>



### Age Demographics

* The below each broken into bins of 4 years (i.e. &lt;10, 10-14, 15-19, etc.)
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value
  * Normalized Totals


```python
purchases["Age"].max()

bins = [0, 10, 14, 19, 24, 29, 34, 39, 100]
group_names = ["0-10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

purchases["Age Range"] = pd.cut(purchases["Age"], bins, labels = group_names)

age_group = purchases.groupby("Age Range")
age_purchase_ct = age_group["Purchase ID"].count()
age_purchase_avg = age_group["Price"].mean()
age_purchase_val = age_group["Price"].sum()

age_purchase_df = pd.DataFrame({
    "Purchase Count": age_purchase_ct,
    "Average Purchase Price": age_purchase_avg,
    "Total Purchase Value": age_purchase_val
})

normalized_age = age_purchase_df["Total Purchase Value"]/age_purchase_df["Total Purchase Value"].sum() #???
age_purchase_df["Normalized Total"] = normalized_age

age_purchase_df["Average Purchase Price"] = age_purchase_df["Average Purchase Price"].map("${:.2f}".format)
age_purchase_df["Total Purchase Value"] = age_purchase_df["Total Purchase Value"].map("${:.2f}".format)
age_purchase_df["Normalized Total"] = age_purchase_df["Normalized Total"].map("${:.2f}".format)

age_purchase_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
      <th>Normalized Total</th>
    </tr>
    <tr>
      <th>Age Range</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0-10</th>
      <td>$2.76</td>
      <td>5</td>
      <td>$13.82</td>
      <td>$0.06</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>$2.99</td>
      <td>3</td>
      <td>$8.96</td>
      <td>$0.04</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>$2.76</td>
      <td>11</td>
      <td>$30.41</td>
      <td>$0.13</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>$3.02</td>
      <td>36</td>
      <td>$108.89</td>
      <td>$0.48</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>$2.90</td>
      <td>9</td>
      <td>$26.11</td>
      <td>$0.11</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>$1.98</td>
      <td>7</td>
      <td>$13.89</td>
      <td>$0.06</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>$3.56</td>
      <td>6</td>
      <td>$21.37</td>
      <td>$0.09</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>$4.65</td>
      <td>1</td>
      <td>$4.65</td>
      <td>$0.02</td>
    </tr>
  </tbody>
</table>
</div>



### Top Spenders

* Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
  * SN
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value


```python
spending_group = purchases.groupby("SN")
top_spend = spending_group["Purchase ID"].count()
top_avg_price = spending_group["Price"].mean()
top_total_value = spending_group["Price"].mean()

top_df = pd.DataFrame({
    "Purchase Count": top_spend,
    "Average Purchase Price": top_avg_price,
    "Total Purchase Value": top_total_value
})

top_df["Average Purchase Price"] = top_df["Average Purchase Price"].map("${:.2f}".format)
top_df["Total Purchase Value"] = top_df["Total Purchase Value"].map("${:.2f}".format)

top_spend_sort = top_df.sort_values(["Total Purchase Value"], ascending = False).head()
top_spend_sort.reset_index(inplace = True)
top_spend_sort
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SN</th>
      <th>Average Purchase Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Eusty71</td>
      <td>$4.81</td>
      <td>1</td>
      <td>$4.81</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Chanirra64</td>
      <td>$4.78</td>
      <td>1</td>
      <td>$4.78</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Alarap40</td>
      <td>$4.71</td>
      <td>1</td>
      <td>$4.71</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Aerithllora36</td>
      <td>$4.65</td>
      <td>1</td>
      <td>$4.65</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Jiskjask76</td>
      <td>$4.59</td>
      <td>1</td>
      <td>$4.59</td>
    </tr>
  </tbody>
</table>
</div>



### Most Popular Items

* Identify the 5 most popular items by purchase count, then list (in a table):
  * Item ID
  * Item Name
  * Purchase Count
  * Item Price
  * Total Purchase Value



```python
popular_group = purchases.groupby(["Item Name", "Item ID", "Price"])
purchase_count = popular_group["Item Name"].count()
purchase_value = popular_group["Price"].sum()

popular_df = pd.DataFrame({
    "Purchase Count": purchase_count,
    "Total Purchase Value": purchase_value
})

popular_sort = popular_df.sort_values(["Purchase Count"], ascending = False).head()
popular_sort.reset_index(inplace = True)

popular_sort["Price"] = popular_sort["Price"].map("${:.2f}".format)
popular_sort["Total Purchase Value"] = popular_sort["Total Purchase Value"].map("${:.2f}".format)
popular_sort.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Item ID</th>
      <th>Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mourning Blade</td>
      <td>94</td>
      <td>$3.64</td>
      <td>3</td>
      <td>$10.92</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Deadline, Voice Of Subtlety</td>
      <td>98</td>
      <td>$1.29</td>
      <td>2</td>
      <td>$2.58</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Stormcaller</td>
      <td>180</td>
      <td>$2.77</td>
      <td>2</td>
      <td>$5.54</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Relentless Iron Skewer</td>
      <td>176</td>
      <td>$2.12</td>
      <td>2</td>
      <td>$4.24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Apocalyptic Battlescythe</td>
      <td>93</td>
      <td>$4.49</td>
      <td>2</td>
      <td>$8.98</td>
    </tr>
  </tbody>
</table>
</div>



### Most Profitable Items

* Identify the 5 most profitable items by total purchase value, then list (in a table):
  * Item ID
  * Item Name
  * Purchase Count
  * Item Price
  * Total Purchase Value


```python
popular_group = purchases.groupby(["Item Name", "Item ID", "Price"])
purchase_count = popular_group["Item Name"].count()
purchase_value = popular_group["Price"].sum()

popular_df = pd.DataFrame({
    "Purchase Count": purchase_count,
    "Total Purchase Value": purchase_value
})

profit_sort = popular_df.sort_values(["Total Purchase Value"], ascending = False).head()
profit_sort.reset_index(inplace = True)

profit_sort["Price"] = profit_sort["Price"].map("${:.2f}".format)
profit_sort["Total Purchase Value"] = profit_sort["Total Purchase Value"].map("${:.2f}".format)
profit_sort.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Item ID</th>
      <th>Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mourning Blade</td>
      <td>94</td>
      <td>$3.64</td>
      <td>3</td>
      <td>$10.92</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Heartstriker, Legacy of the Light</td>
      <td>117</td>
      <td>$4.71</td>
      <td>2</td>
      <td>$9.42</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Apocalyptic Battlescythe</td>
      <td>93</td>
      <td>$4.49</td>
      <td>2</td>
      <td>$8.98</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Betrayer</td>
      <td>90</td>
      <td>$4.12</td>
      <td>2</td>
      <td>$8.24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Feral Katana</td>
      <td>154</td>
      <td>$4.11</td>
      <td>2</td>
      <td>$8.22</td>
    </tr>
  </tbody>
</table>
</div>


