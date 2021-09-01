import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

df = pd.read_csv('epa-sea-level.csv', parse_dates=['Year'])
df['Year'] = df['Year'].dt.year
# print(df.head())


# Using linregress
x = df.Year
y = df['CSIRO Adjusted Sea Level']

df_2000 = df[df.Year >= 2000]
x_2000 = df_2000.Year
y_2000 = df_2000['CSIRO Adjusted Sea Level']
mask1 = ~np.isnan(x_2000) & ~np.isnan(y_2000)
res1 = linregress(x_2000[mask1], y_2000[mask1])

mask = ~np.isnan(x) & ~np.isnan(y)
res = linregress(x[mask], y[mask])
# print(res)
slope, Intercept, r, p, bsexa = res
# print(xs.max())
x2 = np.arange(x.min(), 2051)
y2 = slope * x2 + Intercept

# res1 = linregress()
x3 = np.arange(x_2000.min(), 2051)
y3 = res1.slope * x3 + res1.intercept
# print(slope)
# print(fy[:10])
# fig, ax = plt.subplots()
plt.scatter(x=df.Year, y=df['CSIRO Adjusted Sea Level'])

plt.plot(x2, y2, 'r', label='Predictor1')
plt.plot(x3, y3, 'g', label='Predictor2')

plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()
plt.show()

# # ax2 =ax.twin()
# plt.plot(fx, fy, '-')
# ax.set_xlabel('Year')
# ax.set_ylabel('CSIRO Adjusted Sea Level')

# plt.show()
