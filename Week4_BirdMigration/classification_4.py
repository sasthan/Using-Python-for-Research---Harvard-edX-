import pandas as pd
birddata=pd.read_csv("bird_tracking.csv")

import matplotlib.pyplot as plt

import numpy as np
import pylab

bird_names = pd.unique(birddata.bird_name)
plt.figure(figsize=(7,7))
for bird_name in bird_names:
    ix = birddata.bird_name=="Eric"
    x,y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x,y,".", label=bird_name)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")

ix= birddata.bird_name=="Eric"
speed=birddata.speed_2d[ix]
ind = np.isnan(speed)
plt.hist(speed[~ind])
plt.savefig("hist.pdf")

import datetime
time1 = datetime.datetime.today()

time2 = datetime.datetime.today()

#datetime.datetime.strptime(date_str[:-3], "%Y-%m-%d %H:%M:%S")


data = birddata[birddata.bird_name == "Eric"]
times = data.timestamp
elapsed_time = [time  - times[0] for time in times]
elapsed_days = np.array(elapsed_time)/ datetime.timedelta(days=1)

next_day = 1
inds = []
daily_mean_speed = []
for (i,t) in enumerate(elapsed_days):
    if t< next_day:
        inds.append(i)
    else:
        #compute mean speed
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day +=1
        inds=[]

