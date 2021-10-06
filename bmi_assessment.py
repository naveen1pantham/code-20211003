from data_file import bmi_list, bmi_category, health_risk

def get_bmi(record): 
    '''Calculating BMI by using given formula and adding new columns'''
    
    bmi = round(record['WeightKg']/(record['HeightCm']*0.01)**2, 2)
    record['BMI'] = bmi
    
    if bmi <= 18.4:
        record['health_risk'] = health_risk[0]
        record['bmi_category'] = bmi_category[0]
    elif bmi >= 18.5 and bmi <= 24.9:
        record['health_risk'] = health_risk[1]
        record['bmi_category'] = bmi_category[1]
    elif bmi >= 25 and bmi <= 29.9:
        record['health_risk'] = health_risk[2]
        record['bmi_category'] = bmi_category[2]
    elif bmi >= 30 and bmi <= 34.9:
        record['health_risk'] = health_risk[3]
        record['bmi_category'] = bmi_category[3]
    elif bmi >= 35 and bmi <= 39.9:
        record['health_risk'] = health_risk[4]
        record['bmi_category'] = bmi_category[4]
    elif bmi >= 40:
        record['health_risk'] = health_risk[5]
        record['bmi_category'] = bmi_category[5]
    
    return record

#Task 1
result = list(map(get_bmi, bmi_list))
print("List of dictionaries with new columns")
print("*"*20)
print("*"*20)
print(result)
print("*"*20)
print("*"*20)

#Task 2
count_list = filter(lambda record: record['bmi_category']=='Overweight', result)
print("Count of Overweight persons",len(count_list))