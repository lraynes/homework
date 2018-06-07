import os
import csv

employees_combined = []

def format_first_name(full_name):
    split = full_name.rpartition(" ")
    first = split[0]
    return(first)

def format_last_name(full_name):
    split = full_name.rpartition(" ")
    last = split[2]
    return(last)

def format_date(dob_year):
    split = dob_year.split("-")
    year = split[0]
    month = split[1]
    day = split[2]
    return(month + "/" + day + "/" + year)

def format_ssn(ssn_full):
    split = ssn_full.split("-")
    last_four = split[2]
    return("***-**-" + last_four)

def format_state(state_full):
    
    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }
    
    return(us_state_abbrev[state_full])



employee_1_path = os.path.join(".", "employee_data1.csv")
with open(employee_1_path, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        emp_id = row["Emp ID"]
        full_name = (row["Name"])
        dob_year = row["DOB"]
        ssn_full = row["SSN"]
        state_full = row["State"]

        employees_combined.append({
            "Emp ID": emp_id,
            "First Name": format_first_name(full_name),
            "Last Name": format_last_name(full_name),
            "DOB": format_date(dob_year),
            "SSN": format_ssn(ssn_full),
            "State": format_state(state_full)
        })
        
employee_2_path = os.path.join(".", "employee_data2.csv")
with open(employee_2_path, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        emp_id = row["Emp ID"]
        full_name = row["Name"]
        dob_year = row["DOB"]
        ssn_full = row["SSN"]
        state_full = row["State"]

        employees_combined.append({
            "Emp ID": emp_id,
            "First Name": format_first_name(full_name),
            "Last Name": format_last_name(full_name),
            "DOB": format_date(dob_year),
            "SSN": format_ssn(ssn_full),
            "State": format_state(state_full)
        })


print(employees_combined)


output_path = os.path.join(".", "employee_data_formatted.csv")

with open(output_path, "w", newline="") as csvfile:
    fieldnames = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=",")
    writer.writeheader()
    
    for dictionary in employees_combined:
        writer.writerow(dictionary)