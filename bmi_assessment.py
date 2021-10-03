bmi_list =[
    {"Gender": "Male", "HeightCm": 175, "WeightKg": 75 }, 
    {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, 
    { "Gender": "Male", "HeightCm": 161, "WeightKg":85 }, 
    { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, 
    { "Gender": "Female", "HeightCm": 166,"WeightKg": 62}, 
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, 
    {"Gender": "Female","HeightCm": 167, "WeightKg": 82}
]

health_risk = ['Malnutrition risk', 'Low risk', 'Enhanced risk', 'Medium risk', 'High risk', 'Very high risk']
bmi_category = ['Underweight', 'Normal weight', 'Overweight', 'Moderately obese', 'Severely obese', 'Very severely obese']

def get_bmi(record): 
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

result = list(map(get_bmi, bmi_list))
print("List of dictionaries with new columns")
print(result)

count_list = filter(lambda record: record['bmi_category']=='Overweight', result)

print('Count of Overweight persons',len(count_list))