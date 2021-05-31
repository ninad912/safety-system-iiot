# -*- coding: utf-8 -*-
"""
Created on Sun May 23 21:19:00 2021

@author: LAZY146
"""

import pandas as pd
import urllib.request
import matplotlib.pyplot as plt
import datetime as dti
import time as tm

url = "http://192.168.43.13/"                         # change ip adress according to requirement
column_name = ["Time", "vib", "gas"]        # remove arduino program posts only 2 values, remove the third value i.e extra
df = pd.DataFrame(columns = column_name)
time = "0" 

fig,ax = plt.subplots(2, 1)
fig.tight_layout(pad=3.0)
plt.show()

def read_data():                                    #reading data from URL
    global dt
    rec = urllib.request.urlopen(url).read()
    rec = rec.decode("utf-8")
    dt = rec
   
def get_time():                                     # reading time from the laptop and resolving it
    global time
    time = str(dti.datetime.now())
    k= time.split()
    k = k[1].split(":")
    time = k[0] + ":" + k[1] + ":" + k[2][:2]
   
while True:
    read_data()
    get_time()
    k = list(map(int,dt.split()))
    k.insert(0,time)
    
    df.loc[len(df)] = k 
                           #adding obtained new values into dataframe
    print("data recieved : ", list(map(int,dt.split())))
  
    ax[0].plot(df["Time"], df["vib"])
    ax[0].set_xlabel("Time")
    ax[0].set_xticklabels(df["Time"], rotation=45, ha="center")
    ax[0].set_ylabel("vibration values")
    ax[0].set_title("measured vibration value")
    
    ax[1].plot(df["Time"], df["gas"])
    ax[1].set_xlabel("Time")
    ax[1].set_xticklabels(df["Time"], rotation=45, ha="center")
    ax[1].set_ylabel("gas values in ppm")
    ax[1].set_title("measured gas value") 
    
    """
    will be using this if we implement hebbian rule
    ax[1,0].plot(df["Time"], df["vib"])
    ax[1,0].set_xlabel("Time")
    ax[1,0].set_xticklabels(df["Time"], rotation=45, ha="center")
    ax[1,0].set_ylabel("vibration values")
    ax[1,0].set_title("expected vibration value")
    
    ax[1,1].plot(df["Time"], df["gas"])
    ax[1,1].set_xlabel("Time")
    ax[1,1].set_xticklabels(df["Time"], rotation=45, ha="center")
    ax[1,1].set_ylabel("gas values in ppm")
    ax[1,1].set_title("expected gas value")
    """
    plt.pause(0.05)
    