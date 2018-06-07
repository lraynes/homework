#Import the two sets of revenue data (`budget_data_1.csv` and `budget_data_2.csv`). 
import os
import csv
data_1_path = os.path.join(".", "budget_data_1.csv")

combined_data = {}

#function to re-format dates
def format_date(full_date):
    split = full_date.rpartition("-")
    month = split[0]
    year = split[2]

    if month == "Jan":
        month = "01"
    elif month == "Feb":
        month = "02"
    elif month == "Mar":
        month = "03"
    elif month == "Apr":
        month = "04"
    elif month == "May":
        month = "05"
    elif month == "Jun":
        month = "06"
    elif month == "Jul":
        month = "07"
    elif month == "Aug":
        month ="08"
    elif month == "Sep":
        month = "09"
    elif month == "Oct":
        month = "10"
    elif month == "Nov":
        month = "11"
    elif month == "Dec":
        month = "12"
    
    if len(year) > 2:
        year = year[2:]
    
    return(str(year) + "-" + str(month))

def month_year(formatted_date):
    split = formatted_date.rpartition("-")
    year = split[0]
    month = split[2]
    return(str(month) + "-" + str(year))


#open first CSV
with open(data_1_path, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        date = format_date(row["Date"])
        revenue = row["Revenue"]
        combined_data[date] = revenue

#open second CSV
data_2_path = os.path.join(".", "budget_data_2.csv")

with open(data_2_path, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        date = format_date(row["Date"])
        revenue = row["Revenue"]
        if date not in combined_data:
            combined_data[date] = revenue
        #put the date/revenue in the dictionary
        else:
            combined_data[date] = int(combined_data[date]) + int(revenue)
        #add the revenue to the matching date


#The total number of months included in the dataset
print("Total months: " + str(len(combined_data)))


#The total amount of revenue gained over the entire period
revenue_sum = 0

for data in combined_data:
    #print(data)
    revenue_sum = revenue_sum + int(combined_data[data])

print("Total revenue: $" + str(revenue_sum))

revenue_change = 0
previous = None
greatest_inc = 0
greatest_dec = 0


for key in sorted(combined_data.keys()):

    if previous is None:
        previous = combined_data[key]
    
    else:
        #Gathering total revenue change
        revenue_change = revenue_change + int(combined_data[key]) - int(previous)
        
        #The greatest increase in revenue (date and amount) over the entire period
        if int(combined_data[key]) - int(previous) > greatest_inc:
            greatest_inc = int(combined_data[key]) - int(previous)
            inc_date = str(key)
        
        #The greatest decrease in revenue (date and amount) over the entire period
        if int(combined_data[key]) - int(previous) < greatest_dec:
            greatest_dec = int(combined_data[key]) - int(previous)
            dec_date = str(key)
        
        previous = combined_data[key]
    
        

print("Average change over time: $" + str(revenue_change/len(combined_data)))
print("Greatest increase: $" + str(greatest_inc) + ", occurred " + month_year(inc_date))
print("Greatest decrease: $" + str(greatest_dec) + ", occurred " + month_year(dec_date))

file = open("mainpy.txt","w") 
 
file.write("Total months: " + str(len(combined_data)) + "\n")
file.write("Total revenue: $" + str(revenue_sum) + "\n")
file.write("Average change over time: $" + str(revenue_change/len(combined_data)) + "\n")
file.write("Greatest increase: $" + str(greatest_inc) + ", occurred " + month_year(inc_date) + "\n")
file.write("Greatest decrease: $" + str(greatest_dec) + ", occurred " + month_year(dec_date) + "\n")
 
file.close() 

    



#Your final script should both print the analysis to the terminal and export a text file with the results.

