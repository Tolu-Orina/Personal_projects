import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

df = pd.read_csv('fcc.csv', nrows=500, index_col='date', parse_dates=True)

# print(df.head())

clean_df = df[(df.value >= df.value.quantile(0.025)) &
              (df.value <= df.value.quantile(0.975))]
# print(clean_df.head())

# fig, ax = plt.subplots()

# ax.plot(clean_df.index, clean_df['value'])
# ax.set_xlabel('Date')
# ax.set_ylabel('Page Views')
# ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

# plt.show()

months = [i.strftime('%B') for i in clean_df.index.date]
# clean_df['Months'] = months
# fig, ax = plt.subplots()
# sns.barplot(x=clean_df.index.year, y=clean_df.value,
#             hue=clean_df.Months, data=clean_df, ax=ax)
# yearly_val = clean_df.groupby(
#     [clean_df.index.year, clean_df.index.month]).value.mean()
# yearly_val_month = yearly_val.unstack()
# yearly_val_month.columns = ['January', 'February', 'March', 'April',
#                             'May', 'June', 'July', 'August', 'September',
#                             'October', 'November', 'December']
# yearly_val_month.plot(kind='bar')
# plt.xlabel('Years')
# plt.ylabel('Average Page Views')
# plt.legend(loc='upper left', title='Months')
# plt.show()

fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2)
sns.boxplot(x=clean_df.index.year, y='value', data=clean_df, ax=ax0)

sns.boxplot(x=clean_df.index.month,
            y='value', data=clean_df, ax=ax1)
ax0.set(xlabel='Year', ylabel='Page Views', title='Year-wise Box Plot (Trend)')
ax1.set(xlabel='Month', ylabel='Page Views',
        title="Month-wise Box Plot (Seasonality)")
ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr',
                     'May', 'Jun', 'Jul', 'Aug', 'Sep',
                            'Oct', 'Nov', 'Dec'])
plt.show()
