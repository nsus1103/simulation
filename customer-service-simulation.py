"""
Model to simulate customer service with customers arriving interval following Poisson distribution (rate=1)
and service times following Exponential distribution. Each customer has a patience (uniformly distributed)
and does not wait longer than the patience interval.
"""

import numpy as np
import pandas as pd


def Served(arr, ser, pat):

    time_counter=0
    time_last_customer=0
    customer_wait_times = {}
    customer_total_time = {}
    served = {}
    for customer in range(len(arr)):
        time_counter+=arr[customer]
        wait = max(0,time_last_customer-arr[customer])

        if wait>pat[customer]:
            served[customer+1] = 0
            ser[customer] = 0
            customer_total_time[customer+1] = pat[customer]
            time_last_customer = wait - arr[customer]
        else:
            served[customer+1] = 1
            service_time = ser[customer]

            time_last_customer = service_time + wait
            customer_total_time[customer+1] = wait + service_time


        customer_wait_times[customer+1] = wait
        # customer_total_time[customer+1] = wait + service_time


    return customer_wait_times, customer_total_time, served


arrival_mean = 1
service_mean = 2
l = 1/service_mean

simulations = 1000
wait50=0
total50=0
served50=0
m = 500
for s in range(simulations):
    if s%100==0:
        print('Simulation cycles completed:',s)

    arr = np.random.poisson(1, m)
    ser = np.random.exponential(l, m)
    pat = np.random.uniform(0.3, 0.7, m)

    wait, total, served = Served(arr, ser, pat)
    wait50+=wait[50]
    total50+=total[50]
    served50+=served[50]


d = {'CustomerNo':wait.keys(),
     'ArrivalTime':arr,
     'ServiceTime':ser,
     'Patience': pat,
     'WaitTime':wait.values(),
     'TotalTime':total.values(),
     'Served':served.values()}
df = pd.DataFrame(d)
df.to_csv('simulation.csv', index=False)
print('Average Service time of the 50th customer is:',total50/1000)
print('Average Wait time of the 50th customer is:',wait50/1000)
print('Probability of the 50th customer being served is:', served50/1000)