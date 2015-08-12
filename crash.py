%matplotlib inline

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
plt.rcParams['figure.figsize'] = (15, 5)
plt.rcParams['font.family'] = 'sans-serif'

# This is necessary to show lots of columns in pandas 0.12.
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

crash = pd.read_csv('../data/crash.csv',
                    sep=';', encoding='latin1',
                    parse_dates=['Crash_Date'], dayfirst=True,
                    index_col='Crash_Date')
# Add the weekday column
durham_crash = crash[crash['County'] == "Durham"].copy()
durham_crash.loc[:,'weekday'] = durham_crash.index.weekday

# Add up the number of cyclists by weekday, and plot!
weekday_counts = durham_crash.groupby('weekday').aggregate('count')
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_counts.plot(kind='bar')
