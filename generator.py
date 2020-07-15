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
import datetime
import time
import os

# Random date generator


def str_time_prop(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)


gender_choice = [1, 2]
gender_dist = [.48, .52]
genders = []

# Initial function


def generate(amount):
    for i in range(0, amount):
        genders.append(str(random.choices(gender_choice, gender_dist)
                           ).replace('[', '').replace(']', ''))


amount_generate = int(input("Enter amount of data to generate: "))

generate(amount_generate)


# Age generate

ten_percent_age = int((amount_generate/100)*10)

young_age = []
old_age = []
age = []

for i in range(0, ten_percent_age):
    young_age.append(np.random.normal(loc=35))

for i in range(0, amount_generate - ten_percent_age):
    old_age.append(np.random.normal(loc=85))

age = young_age + old_age
random.shuffle(age)

# ID
user_id = []

for ID in age:
    user_id.append(int(id(ID)))

# Birth Date Generate

birth_date = []
birth_year = []
birth_month = []
birth_day = []
yearNow = int(str(datetime.datetime.now()).split()[0].split('-')[0])

for Age in age:
    birth_year.append(yearNow - round(Age))
    birth_month.append(round(float("0."+str(Age).split('.')[1])*12)) if round(
        float("0."+str(Age).split('.')[1])*12) != 0 else birth_month.append(1)

    if (round(float("0."+str(Age).split('.')[1])*12) == 2):
        birth_day.append(random.randint(0, 28))
    elif((round(float("0."+str(Age).split('.')[1])*12) == 2) and int(birth_year) % 4 == 0):
        birth_day.append(random.randint(0, 29))
    else:
        birth_day.append(random.randint(0, 30))

# Saving to CSV

df = pd.DataFrame({"Patient ID": user_id, "Gender": genders, "Age": age,
                   "Birth Year": birth_year, "Birth Month": birth_month, "Birth Day": birth_day})
df.to_csv("output.csv", index=False)
print(str(amount_generate) +
      " datasets has been successfully generated and saved to output.csv at "+str(os.getcwd()))
