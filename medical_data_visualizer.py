import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('medical_examination.csv', nrows=500)
# print(df.head())
#  BMI is Weight(kg) / height**2(meters)
bmi = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = pd.Series([1 if i > 25 else 0 for i in bmi.values])
# print(df.overweight.head(10))
# Cholesterol & Gluc re-engineered
df['cholesterol'] = [0 if i <= 1 else 1 for i in df.cholesterol]
df['gluc'] = [0 if i <= 1 else 1 for i in df.gluc]
# print(df.gluc.head())

melted_df = df.melt(
    id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
melted_df['total'] = 1
irom = melted_df.groupby(
    ['cardio', 'variable', 'value'], as_index=False).count()

# fig, ax = plt.subplots()
# ax = sns.catplot(x='variable', y='total', col='cardio',
#                  hue='value', data=irom, kind='bar')
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(7, 4))
sns.barplot(x=irom[irom.cardio == 0]['variable'],
            y=irom[irom.cardio == 0]['total'], hue=irom.value, ax=ax0)
sns.barplot(x=irom[irom.cardio == 1]['variable'],
            y=irom[irom.cardio == 1]['total'], hue=irom.value, ax=ax1)
plt.show()


# # print(df.head())
# new_df = df[(df['ap_lo'] <= df['ap_hi'])
#             & (df['height'] >= df['height'].quantile(0.025))
#             & (df['height'] <= df['height'].quantile(0.975))
#             & (df['weight'] >= df['weight'].quantile(0.025))
#             & (df['weight'] <= df['weight'].quantile(0.975))]
# # print(new_df.head())
# # crosstab_obj = pd.crosstab(index, columns)
# mask = np.triu(np.ones_like(new_df.corr(), dtype=bool))

# print(new_df.corr())
# fig, ax = plt.subplots(figsize=(11, 9))
# sns.heatmap(new_df.corr(), annot=True, mask=mask, linewidths=.5, fmt='.1f')
# plt.show()
