import pandas as pd

input_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
"HeightCm": 167, "WeightKg": 82}]


df = pd.DataFrame(input_data)

df['HeightCm'] = df['HeightCm'].apply(lambda x:(x/100))
df.rename(columns = {'HeightCm' : 'Heightm2'}, inplace = True)
df['BMI'] = df['WeightKg']/df['Heightm2']
Under_weight =  df[df['BMI']<= 18.4]
Normal_weight = df[(df['BMI']>= 18.4) & (df['BMI']<= 24.9)]
Over_weight = df[(df['BMI']>= 25) & (df['BMI']<= 29.9)]
Moderately_obese = df[(df['BMI']>= 30) & (df['BMI']<= 29.9)]
Severely_obese = df[(df['BMI']>= 35) & (df['BMI']<= 39.9)]
Very_severely_obese = df[(df['BMI']>= 40)]
if not Under_weight.empty:
    Under_weight['BMI Category'] = 'Under weight'
    Under_weight['Health risk'] = 'Malnutrition risk'
if not Normal_weight.empty:
    Normal_weight['BMI Category'] = 'Normal weight'
    Normal_weight['Health risk'] = 'Low risk'
if not Over_weight.empty:
    Over_weight['BMI Category'] = 'Over weight'
    Over_weight['Health risk'] = 'Enhanced risk'
if not Moderately_obese.empty:
    Moderately_obese['BMI Category'] = 'Moderately obese'
    Moderately_obese['Health risk'] = 'Medium risk'
if not Severely_obese.empty:
    Severely_obese['BMI Category'] = 'Severely obese'
    Severely_obese['Health risk'] = 'High risk'
if not Very_severely_obese.empty:
    Very_severely_obese['BMI Category'] = 'Very severely obese'
    Very_severely_obese['Health risk'] = 'Very High risk'

result = pd.concat((Under_weight,Normal_weight,Over_weight,Moderately_obese,Severely_obese,Very_severely_obese),
                   axis=0,ignore_index=True)
print(result)                                                                                                     