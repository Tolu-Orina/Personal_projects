import pandas as pd
import numpy as np


my_cols = ['age', 'workclass', 'fnlwgt', 'education',
           'education-num', 'marital-status', 'occupation',
           'relationship', 'race', 'sex', 'capital-gain',
           'capital-loss', 'hours-per-week', 'native_country',
           'salary']
df = pd.read_csv('adult.data.csv', header=None, names=my_cols)

# print(df.head())
per_race = df['race'].value_counts()
# print(per_race) 1
age_men = df[df['sex'] == ' Male']['age'].mean()

average_age = df.groupby('sex')['age'].mean()
average_age_men = average_age[average_age.index == ' Male']
# print(round(age_men, 1)) 2
tot_educ = df['education'].value_counts(normalize=True)
percentage_bachelors = round(
    (tot_educ[tot_educ.index == ' Bachelors'] * 100).item(), 1)
# print(percentage_bachelors) 3

advanced_educ = [' Bachelors', ' Masters', ' Doctorate']
df_adv = df[df.education.isin(advanced_educ)]
adv_sal = df_adv['salary'].value_counts(normalize=True)

# percentage with salary >50K
higher_education_rich = adv_sal[adv_sal.index == ' >50K']
higher_education_rich = round(higher_education_rich.item() * 100, 1)
# print(higher_education_rich) 4

df_ill = df[~df.education.isin(advanced_educ)]
ill_sal = df_ill['salary'].value_counts(normalize=True)

lower_education_rich = ill_sal[ill_sal.index == ' >50K']
lower_education_rich = round(lower_education_rich.item() * 100, 1)
# print(lower_education_rich) 5

min_work_hours = df['hours-per-week'].min()
# print(min_work_hours) 6

peep_min_hr = df[df['hours-per-week'] == min_work_hours]
sal_min_peep = peep_min_hr['salary'].value_counts(normalize=True) * 100
num_min_workers = sal_min_peep[sal_min_peep.index == ' >50K'].item()
# print(num_min_workers) 7

my_conty = df.groupby(['native_country'])[
    'salary'].value_counts(normalize=True)
# print(my_conty.unstack()[' >50K'].idxmax()) 8
# print(round((my_conty.unstack()[' >50K'].max() * 100), 1)) 9

india_peeps = df[(df['native_country'] == ' India') & (df.salary == ' >50K')]
# print(india_peeps['occupation'].value_counts().idxmax()) 10
