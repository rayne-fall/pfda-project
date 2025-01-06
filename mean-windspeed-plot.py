# mean windspeed plot
# author: Sylvia Chapman Kent
# produces a scrollable plot recording the mean daily windspeed at Johnstown Castle weather station between 2003 and 2024

# import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.widgets import Button

# load data
df=pd.read_csv("hly1775.csv", skiprows=17, low_memory=False)
# split date column into date and time columns
df[['date', 'time']] = df['date'].str.split(' ', n=1, expand=True)
# convert date column to datetime 
df["date"]=df['date'].astype('datetime64[ns]')
# set date column as index column
df.set_index('date', inplace=True)
# drop missing values from windspeed data
df["wdsp"]= df.loc[:,("wdsp")].replace(' ', np.nan)
df.dropna(inplace=True)
# convert windspeed values to floats
df['wdsp']=df['wdsp'].astype(float)
# calculate mean figures for each numerical column per day
mean_per_day=df.groupby([df.index]).mean(numeric_only =True)

# plot windspeed vs date
fig, ax = plt.subplots(figsize=(50,15))

wdsp=mean_per_day["wdsp"]
wdsp=wdsp.to_numpy()

# set visible range (reference 8)
display_range = 100
current_index = 0

# label axes
ax.set_xlabel("Date")
ax.set_ylabel("Windspeed (knot)")
# add title
ax.set_title("Mean windspeed per day 2003-2024")

# plot data within current visible range
plot=ax.plot(mean_per_day.index[current_index:current_index + display_range], wdsp[current_index:current_index + display_range], "*:c")

# define function for scrolling through plot (reference 8)
def update_plot(forward=True):
    global current_index
    step = display_range if forward else -display_range
    current_index += step
 
    if current_index < 0:
        current_index = 0
    elif current_index + display_range > len(mean_per_day.index):
        current_index = len(mean_per_day.index) - display_range
 
    plot.set_xdata(mean_per_day.index[current_index:current_index + display_range])
    plot.set_ydata(wdsp[current_index:current_index + display_range])
    plt.draw()

# Create buttons
ax_next_button = plt.axes([0.81, 0.01, 0.1, 0.05])
ax_prev_button = plt.axes([0.7, 0.01, 0.1, 0.05])
 
next_button = Button(ax_next_button, 'Next')
prev_button = Button(ax_prev_button, 'Previous')
 
# Connect buttons to update functions
next_button.on_clicked(lambda event: update_plot(forward=True))
prev_button.on_clicked(lambda event: update_plot(forward=False))

plt.show()
 