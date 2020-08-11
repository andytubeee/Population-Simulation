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
import uuid

# Variables

check_duplicate_file = False

# Gender
gender_choice = [1, 2]
gender_dist = [.48, .52]
genders = []

# Age

reg_age_gen = False

age = []
average_age = 80
case_percent = 10

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
exitcodechoices = ["00", "01"]

# Health Authority
ha_code = []

# ICD 10 Code
icd_code = []

# Department
department = []

# Operative death code
od_code = []

# Supplementry Death Code:
sd_code = []

# Procedure Code
pro_code = []

# Environment
environ_department = []

# CCI Desc
cci_ver = []
cci_desc = []
cci = []

#############################################################################################################################################################

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


def average_int(average):
    return np.random.normal(average)


# Initial function

amount_generate = int(input("Enter amount of data to generate: "))

# Gender and Age

male_age = []

reg_age = []
age_case = []
high_age = 93
fem_age = []

for i in range(0, amount_generate):
    rand_gender = str(random.choices(gender_choice, gender_dist)
                      ).replace('[', '').replace(']', '')
    genders.append(rand_gender)
    # age.append(80.0)

if (reg_age_gen == True):
    for i in range(0, amount_generate):
        age.append(round(np.random.normal(80), 1))
else:
    male_count = int(genders.count("1"))

    ten_percent = int((male_count/100)*case_percent)

    for i in range(0, genders.count("2")):
        fem_age.append(round(average_int(80), 1))

    for i in range(0, ten_percent):
        age_case.append(round(average_int(high_age), 1))
    for i in range(0, int(male_count)-ten_percent):
        reg_age.append(round(average_int(average_age-1), 1))

    age = age_case+reg_age+fem_age


# print(male_count)
# print(ten_percent)
# print(age_case)
# print(len(fem_age))


age.sort()
# print(age)


# for g in genders:
#     if (int(g)==1):
#         ten_percent_male_age = int((male_count/100)*10)
#         for i in range (0, ten_percent_male_age):
#             age_case.append(np.random.normal(high_age))
#         for i in range (0, male_count-ten_percent_male_age):
#             reg_age.append(average_age)

#         male_age = age_case + reg_age
#     else:
#         for i in range(0, amount_generate-male_count):
#             fem_age.append(np.random.normal(average_age))

#     age = male_age+fem_age


genders.sort(reverse=True)
# print(genders)

temp_group = list(zip(genders, age))
random.shuffle(temp_group)

genders, age = zip(*temp_group)


# # Age generate old

# ten_percent_age = int((amount_generate/100)*10)

# for i in range(0, ten_percent_age):
#     age_case.append(np.random.normal(high_age))

# for i in range(0, amount_generate - ten_percent_age):
#     reg_age.append(np.random.normal(average_age-1))

# age = age_case + reg_age
# random.shuffle(age)

# Age New
# male_age = []
# fem_age = []
# global male_count
# male_count = 0

# for g in genders:
#     if int(g) == 1:
#         male_count += 1
# ten_percent_age = int((male_count/100)*10)
# for i in range(0, ten_percent_age):
#     age_case.append(np.random.normal(loc=high_age))
# for i in range(0, male_count - ten_percent_age):
#     reg_age.append(np.random.normal(loc=average_age-1))

# male_age = age_case + reg_age
# random.shuffle(male_age)

# for i in range(0, amount_generate-male_count):
#     fem_age.append(np.random.normal(40))


# age = male_age+fem_age
# random.shuffle(age)

# ID

for ID in age:
    # user_id.append(str(int(id(ID)))[3:])
    # user_id.append(str(uuid.uuid4()).split('-')[0][:9])
    user_id.append(uuid.uuid4().node)

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

global random_stay_date

for Age in age:
    if Age >= 80:
        random_stay_date = random.randint(14, 30)
    else:
        random_stay_date = random.randint(1, 12)

    admdate = random_date("1/1/2020 12:00 AM",
                          "5/31/2020 11:59 PM", random.random())
    admission_date.append(str(admdate).split()[0])

    admdate_day = str(admdate).split()[0].split('/')[1]
    admdate_month = str(admdate).split()[0].split('/')[0]

    discharge_date.append(pd.to_datetime(
        str(admdate).split()[0]) + pd.DateOffset(days=random_stay_date))

    lnth_of_stay.append(random_stay_date)
    icu_len = random.randint(0, random_stay_date)
    if (icu_len == random_stay_date):
        icu_len = 0
    elif ((random_stay_date - icu_len) < 2):
        icu_len = icu_len - 2

    if (icu_len < 0):
        icu_len = 0
    icu_day.append(icu_len)


for i in range(0, amount_generate):
    pass


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

    exit_code.append(str(random.choices(exitcodechoices)
                         ).replace("['", '').replace("']", ''))


# Health Authority

for i in range(0, amount_generate):
    ha_code.append(str(random.choice([1, 2, 3, 4])))


# Department Options


# ICD10

for i in range(0, amount_generate):
    icd_letter = str(random.choice('abcdefghijklmnopqrstvwxyz')).upper()

    icd_number = str("{0:0=2d}".format(random.randrange(0, 10**2)))

    # Remove Invalid ICD Number

    if (icd_letter == 'D'):
        icd_number = str("{0:0=2d}".format(random.randrange(0, 90)))
        if (icd_number == "49"):
            icd_number = "50"
    if (icd_letter == 'E'):
        icd_number = str("{0:0=2d}".format(random.randrange(0, 91)))
    if (icd_letter == 'H'):
        icd_number = str("{0:0=2d}".format(random.randrange(0, 96)))
    if (icd_letter == 'K'):
        icd_number = str("{0:0=2d}".format(random.randrange(0, 94)))
    if (icd_letter == 'P'):
        icd_number = str("{0:0=2d}".format(random.randrange(0, 97)))
    if (icd_letter == 'T'):
        icd_number = str("{0:0=2d}".format(random.randrange(0, 99)))
    if (icd_letter == 'Y'):
        icd_number = str("{0:0=2d}".format(random.randrange(0, 99)))

    icd_code.append(icd_letter +
                    icd_number)

    if (icd_letter == 'A' or icd_letter == 'B'):
        department.append("Certain infectious and parasitic diseases")
    elif (icd_letter == 'C'):
        department.append("Neoplasms")
    elif (icd_letter == 'D'):
        # 0 - 49
        if (int(icd_number) in range(0, 49)):
            department.append("Neoplasms")
        elif(int(icd_number) in range(50, 90)):
            department.append(
                "Diseases of the blood and blood-forming organs and certain disorders involving the immune mechanism")
        else:
            department.append("Error, ICD-10 Chapter Not Found")
    elif (icd_letter == 'E'):
        if (int(icd_number) in range(0, 91)):
            department.append(
                "Endocrine, nutritional and metabolic diseases")
        else:
            department.append(
                "Error, ICD-10 Chapter Not Found")
    elif (icd_letter == 'F'):
        department.append(
            "Mental and behavioural disorders")
    elif (icd_letter == 'G'):
        department.append(
            "Diseases of the nervous system")
    elif (icd_letter == 'H'):
        if(int(icd_number) in range(0, 60)):
            department.append(
                "Diseases of the eye and adnexa")
        elif (int(icd_number) in range(60, 96)):
            department.append(
                "Diseases of the ear and mastoid process")
        else:
            department.append(
                "Error, ICD-10 Chapter Not Found")
    elif (icd_letter == 'I'):
        department.append(
            "Diseases of the ear and mastoid process")
    elif (icd_letter == 'J'):
        department.append(
            "Diseases of the respiratory system")
    elif (icd_letter == 'K'):
        if (int(icd_number) in range(0, 94)):
            department.append(
                "Diseases of the digestive system")
        else:
            department.append(
                "Error, ICD-10 Chapter Not Found")
    elif (icd_letter == 'L'):
        department.append(
            "Diseases of the skin and subcutaneous tissue")
    elif (icd_letter == 'M'):
        department.append(
            "Diseases of the musculoskeletal system and connective tissue")
    elif (icd_letter == 'N'):
        department.append(
            "Diseases of the genitourinary system")
    elif (icd_letter == 'O'):
        department.append(
            "Pregnancy, childbirth and the puerperium")
    elif (icd_letter == 'P'):
        if(int(icd_number) in range(0, 97)):
            department.append(
                "Certain conditions originating in the perinatal period")
        else:
            department.append(
                "Error, ICD-10 Chapter Not Found")
    elif (icd_letter == 'Q'):
        department.append(
            "Congenital malformations, deformations and chromosomal abnormalities")
    elif (icd_letter == 'R'):
        department.append(
            "Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified")
    elif (icd_letter == 'S'):
        department.append(
            "Injury, poisoning and certain other consequences of external causes")
    elif (icd_letter == 'T'):
        if (int(icd_number) in range(0, 99)):
            department.append(
                "Injury, poisoning and certain other consequences of external causes")
        else:
            department.append(
                "Error, ICD-10 Chapter Not Found")
    elif (icd_letter == 'U'):
        department.append(
            "Error, ICD-10 Chapter Not Found")
    elif (icd_letter == 'V'):
        department.append(
            "External causes of morbidity and mortality")
    elif (icd_letter == 'W'):
        department.append(
            "External causes of morbidity and mortality")
    elif (icd_letter == 'X'):
        department.append(
            "External causes of morbidity and mortality")
    elif (icd_letter == 'Y'):
        if(int(icd_number) in range(0, 99)):
            department.append(
                "External causes of morbidity and mortality")
        else:
            department.append(
                "Error, ICD-10 Chapter Not Found")
    elif (icd_letter == 'Z'):
        department.append(
            "Factors influencing health status and contact with health services")
    else:
        department.append("Other")


# Operative Death Code

for i in range(0, int((amount_generate / 100) * 90)):
    od_code.append(str(random.choice(["01"])))
for i in range(0, int((amount_generate / 100) * 10)):
    od_code.append(str(random.choice(["00"])))

random.shuffle(od_code)
# Supplementary Death Code

for i in range(0, amount_generate):
    sd_code.append(str(random.choice(["91", "92", "00", "01"])))

# Procedure Code

for i in range(0, amount_generate):
    pro_code.append(str("{0:0=2d}".format(
        random.choice([0, 1, 2, 3, 4, 5, 6, 7]))))

# Hospital or Clinic

for i in range(0, amount_generate):
    environ_department.append(str(random.choice(["Hospital", "Clinic"])))
    cci_ver.append("CCI2009")

# CCI CodeBypass lacr excret sys EPO
for i in icu_day:
    if i >= 15:
        bypass_proc = random.choice(["Bypass lacr excret sys EPO", "Bypass lacr excret sys EPO &lasr", "Bypass lacr excret sys EPO &stent", "Bypass lacr excret sys OA", "Bypass lacr excret sys OA &stent", "Bypass lacr excret sys EPO nas cavity app",
                                     "Bypass lacr excret sys EPO nas cavity app &lasr", "Bypass lacr excret sys OA term site nose", "Bypass lacr excret sys EPO nas cavity app &stent", "Bypass lacr excret sys OA term site nose &stent"])
        cci_desc.append(bypass_proc)

        if (bypass_proc == "Bypass lacr excret sys EPO"):
            cci.append("1CU76BA")
        elif (bypass_proc == "Bypass lacr excret sys EPO &lasr"):
            cci.append("1CU76BAAG")
        elif (bypass_proc == "Bypass lacr excret sys EPO &stent"):
            cci.append("1CU76BANR")
        elif (bypass_proc == "Bypass lacr excret sys OA"):
            cci.append("1CU76LA")
        elif (bypass_proc == "Bypass lacr excret sys OA &stent"):
            cci.append("1CU76LANR")
        elif (bypass_proc == "Bypass lacr excret sys EPO nas cavity app"):
            cci.append("1CU76BE")
        elif (bypass_proc == "Bypass lacr excret sys EPO nas cavity app &lasr"):
            cci.append("1CU76BEAG")
        elif (bypass_proc == "Bypass lacr excret sys OA term site nose"):
            cci.append("1CU76ML")
        elif (bypass_proc == "Bypass lacr excret sys EPO nas cavity app &stent"):
            cci.append("1CU76BENR")
        elif (bypass_proc == "Bypass lacr excret sys OA term site nose &stent"):
            cci.append("1CU76BENR")
    else:
        scan_proc = random.choices(["Scan", "Other"], [.3, .7])
        cci_desc.append(str(scan_proc).replace("['", '').replace("']", ''))
        if (str(scan_proc).replace("['", '').replace("']", '') == "Scan"):
            rand_scan_cci_code = random.choice(["3FU70CA", "3FU70CC", "3FU70CE", "3OA70CE", "3OC70CB", "3OC70CD", "3PC70CC", "3PC70TF", "3PC70SQ", "3NZ70MX", "3NZ70MY", "3NZ70MZ", "3NZ70SC", "3IP70KG", "3IP70KS", "3LZ70CC", "3PB70CA", "3PB70CC", "3AN70CB", "3AN70CD", "3FV70CC", "3GT70CA", "3GT70CE", "3GT70KD", "3AW70CD", "3AW70CF",
                                                "3CU70CC", "3FP70CC", "3KR70ZZ", "3OD70CE", "3OT70CE", "3PZ70TK", "3PZ70TL", "3QG70CA", "3QG70CB", "3QG70CC", "3QG70CE", "3RM70CA", "3RM70CC", "3RM70CE", "3SC70CA", "3SC70CC", "3SC70CE", "3TA70CA", "3TA70CC", "3TM70CA", "3NZ70SE", "3NZ70SN", "3NZ70SP", "3NZ70TB", "3NZ70TC", "3OC70KP", "3OC70CE", "3OC70CC"])
            cci.append(str(rand_scan_cci_code).replace(
                "['", '').replace("']", ''))
        else:
            rand_other_cci_code = random.choice(["2KG28TP", "2KG28ZZ", "2KG29TA", "2KG29TP", "2LZ28JA", "2LZ28JAPL", "2ZZ02ZS", "2ET70BA", "2FA70BA", "2FX70BA", "2FX70LA", "2GM70BA", "1NA35BAX4", "2NA70BA", "2NA70BN",
                                                 "2NF70BA", "2NF70BN", "2OW70BN", "2NM70BABH", "2NM70BNBG", "2NT70BA", "2DE70CA", "2PQ70BA", "2RS70CA", "2GJ70BA", "3AF20WA", "3AF20WE", "3FE10AR", "3FE10AQ", "3CU12VA", "3EE12VA", "3SF12VL", "3SC10KM"])
            cci.append(rand_other_cci_code)


# Saving to CSV

df = pd.DataFrame({"Patient ID": user_id, "Gender": genders, "Age": age,
                   "Birth Year": birth_year, "Birth Month": birth_month, "Birth Day": birth_day, "Birth Date": birth_date, "Exit Code": exit_code, "Admission Date": admission_date, "Admission Time": admission_time, "Discharge Date": discharge_date, "Discharge Time": discharge_time, "Total Length of Stay": lnth_of_stay, "Intensive Care Unit Days": icu_day, "Health Authority Code": ha_code, "Operative Death Code": od_code, "Supplementary Death Code": sd_code, "Procedure Code": pro_code, "Version Year": cci_ver, "CCI": cci, "CCI Description": cci_desc, "ICD-10 Code": icd_code, "ICD-10 Chapter": department, "Environment": environ_department})

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
