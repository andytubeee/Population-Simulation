import csv
import random
import datetime
import time
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import randint
from scipy.stats import truncnorm
import math
import array
import pandas.core.arrays.datetimes
import time
import os
import pathlib
import string

# Variables

check_duplicate_file = False

# Gender
gender_choice = [1, 2]
gender_dist = [.48, .52]
genders = []

# Age
age = []
average_age = 80

# ID
user_id = []

# Birth Dates
birth_date = []
birth_year = []
birth_month = []
birth_day = []
yearNow = int(str(datetime.datetime.now()).split()[0].split('-')[0])

# Admission and Discharge Date
admission_date = []
discharge_date = []
lnth_of_stay = []
icu_day = []

# Admission and Discharge Time
admission_time = []
discharge_time = []

# Entry Code
entry_code = []

# Exit Code
exit_code = []
exitcodechoices = ["91", "92", "00", "01"]

# Healt Authority
ha_code = []

# ICD 10 Code
icd_num = []

# Random date generator


def str_time_prop(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)


def month_round(input):
    input = round(input)

    if input != 0:
        return input
    else:
        return 1


# Initial function

def generate(amount):
    for i in range(0, amount):
        genders.append(str(random.choices(gender_choice, gender_dist)
                           ).replace('[', '').replace(']', ''))


amount_generate = int(input("Enter amount of data to generate: "))

generate(amount_generate)


# Age generate old

# ten_percent_age = int((amount_generate/100)*10)

# young_age = []
# old_age = []
# age = []

# for i in range(0, ten_percent_age):
#     young_age.append(np.random.normal(loc=35))

# for i in range(0, amount_generate - ten_percent_age):
#     old_age.append(np.random.normal(loc=85))

# age = young_age + old_age
# random.shuffle(age)

# Age New

for i in range(0, amount_generate):
    age.append(np.random.normal(average_age))

# ID

for ID in age:
    user_id.append(int(id(ID)))

# Birth Date Generate

for Age in age:
    birth_year.append(yearNow - round(Age))
    birth_month.append(round(float("0."+str(Age).split('.')[1])*12)) if round(
        float("0."+str(Age).split('.')[1])*12) != 0 else birth_month.append(1)
    birth_date.append(str(yearNow - round(Age))+"/" +
                      str(month_round(float("0."+str(Age).split('.')[1])*12)))

    if (round(float("0."+str(Age).split('.')[1])*12) == 2):
        birth_day.append(random.randint(0, 28))
    elif((round(float("0."+str(Age).split('.')[1])*12) == 2) and int(birth_year) % 4 == 0):
        birth_day.append(random.randint(0, 29))
    else:
        birth_day.append(random.randint(0, 30))


# Admission and Discharge Date

for i in range(0, amount_generate):

    admdate = random_date("1/1/2020 12:00 AM",
                          "5/31/2020 11:59 PM", random.random())
    admission_date.append(str(admdate).split()[0])

    admdate_day = str(admdate).split()[0].split('/')[1]
    admdate_month = str(admdate).split()[0].split('/')[0]

    random_stay_date = random.randint(1, 12)

    discharge_date.append(pd.to_datetime(
        str(admdate).split()[0]) + pd.DateOffset(days=random_stay_date))

    lnth_of_stay.append(random_stay_date)
    icu_day.append(random.randint(0, random_stay_date))


# Admission and Discharge Time

for i in range(0, amount_generate):
    admission_time.append(str(random_date("1/1/2020 12:00 AM",
                                          "5/31/2020 11:59 PM", random.random())).split()[1] + " "+str(random.choices(["AM", "PM"])).replace(
                                              "['", ''
    ).replace("']", ""))
    discharge_time.append(str(random_date("1/1/2020 12:00 AM",
                                          "5/31/2020 11:59 PM", random.random())).split()[1] + " "+str(random.choices(["AM", "PM"])).replace(
                                              "['", ''
    ).replace("']", ""))


# Entry Code

for i in range(0, amount_generate):
    entry_code.append(str(random.choice(["91", "92"])))


# Exit Code

for i in range(0, amount_generate):
    # exit_code.append("%02d" % int(str(random.choices([91, 92, 0, 1])
    #                                   ).replace('[', '').replace(']', '')))

    exit_code.append("_"+str(random.choices(exitcodechoices)
                             ).replace("['", '').replace("']", ''))


# Health Authority

for i in range(0, amount_generate):
    ha_code.append(str(random.choice([1, 2, 3, 4])))


# ICD10

for i in range(0, amount_generate):
    icd_num.append(str(random.choice(string.ascii_letters)).upper() +
                   str("{0:0=2d}".format(random.randrange(1, 10**2))))


# Saving to CSV

df = pd.DataFrame({"Patient ID": user_id, "Gender": genders, "Age": age,
                   "Birth Year": birth_year, "Birth Month": birth_month, "Birth Day": birth_day, "Birth Date": birth_date, "Entry Code": entry_code, "Exit Code": exit_code, "Admission Date": admission_date, "Admission Time": admission_time, "Discharge Date": discharge_date, "Discharge Time": discharge_time, "Total Length of Stay": lnth_of_stay, "Intensive Care Unit Days": icu_day, "Health Authority Code": ha_code, "ICD10 Code": icd_num})

output_name = str(input("Please Enter an Output Name: "))

if (not check_duplicate_file):
    if (os.path.isfile(output_name+".csv")):
        # print(output_name+" already exists, please enter another file name!")

        df.to_csv(output_name+".csv", index=False)

        if (".csv" in output_name):
            output_name.replace('.csv', '')

        print(str(amount_generate) +
              " datasets has been successfully generated and saved to "+str(os.getcwd())+"\\"+output_name+".csv")
    else:

        df.to_csv(output_name+".csv", index=False)

        if (".csv" in output_name):
            output_name.replace('.csv', '')

        print(str(amount_generate) +
              " datasets has been successfully generated and saved to "+str(os.getcwd())+"\\"+output_name+".csv")
else:
    if (os.path.isfile(output_name+".csv")):
        print(output_name+" already exists, please enter another file name!")
    else:

        df.to_csv(output_name+".csv", index=False)

        if (".csv" in output_name):
            output_name.replace('.csv', '')

        print(str(amount_generate) +
              " datasets has been successfully generated and saved to "+str(os.getcwd())+"\\"+output_name+".csv")
