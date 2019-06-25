#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

# for calculating the person of interest
no_of_poi=0
for features in enron_data.values():
    if features["poi"]==True:
        no_of_poi+=1
print(no_of_poi)


# loading the file with the names of people of interest
# and finding the people of interest in text file
poi_names_txt = open("poi_names.txt","r").read()
poi_names_list = poi_names_txt.split("\n")


poi_in_txt=0
for poi in poi_names_list:
    poi_in_txt+=1
print(poi_in_txt-2)



# calculating the value of stock belonging to James Prentice
print("Value of stock belonging to James Prentice:",enron_data["PRENTICE JAMES"]["total_stock_value"])

# emails from Wesley Colwell to poi
print("Emails from Wesley Colwell to poi:",enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

# value of stock exercisd by Jeffrey K Skilling
print("Stock exercisd by Jeffrey K Skilling:",enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

# for calculating quantified salary
# and quantified email

quantified_salary = 0
quantified_email = 0
total_payment_with_NaN = 0
total_people = 0
poi_with_NaN = 0
total_poi = 0
poi_with_total_payment_NaN = 0
for i in enron_data:
        if enron_data[i]["salary"] != 'NaN':
                quantified_salary+=1
        if enron_data[i]["email_address"] != 'NaN':
                quantified_email+=1
        if enron_data[i]["total_payments"] == 'NaN':
                total_payment_with_NaN+=1
        if enron_data[i]["poi"] == 'NaN':
                poi_with_NaN+=1
        if enron_data[i]["poi"] == True:
                total_poi+=1
                if enron_data[i]["total_payments"] == 'NaN':
                        poi_with_total_payment_NaN+=1
        total_people+=1

print("Number of quantified salary:",quantified_salary)
print("Number of quantified email:",quantified_email)


# people with payment = NaN
print("People whose total payment is not given:",total_payment_with_NaN)

# percentage of total_payment_with_NaN
print("Percentage of above people",total_payment_with_NaN/total_people*100,"%")

print("People with unknown poi:",poi_with_NaN)

print("Total people in dataset:",total_people)

print("Total people of intereset:",total_poi)

print("POI with unknown total payment:",poi_with_total_payment_NaN)