# coding=utf-8
# filename: JSONDecoder.py

"""
This file includes the procedure to process the data from iperf3 with single thread, i.e. "iperf3 -c hostname
[-i time]" and draws a LINE CHART for it.
"""

import matplotlib.pyplot as plt
import json
import re

import Statistics


def read_text_file(file_name):
    """
    Read experiment result in text file

    :param file_name:   File path to result file
    :return:    Data text in list, line by line
    """
    target_file = open(file_name)
    lines = target_file.readlines()

    target_file.close()
    return lines


def get_source_ready(document):
    """
    Prepare all data in list for plotting

    :param document:            Data text in list, line by line
    """
    for j in range(len(document)):
        line = document[j]
        bandwidth.append(line[4])
        retr.append(line[6])
        cwnd.append(line[7])


doc = read_text_file("./json.log")

docstring = re.sub("[\n|\t]", "", "".join(doc))

results = json.loads("".join(doc))

intervals = results["intervals"]

for i in range(len(intervals)):
    print intervals[i]["streams"][0]["rtt"]

retr = []
bandwidth = []
cwnd = []

get_source_ready(doc)

stat = Statistics.Stats(bandwidth)

print "Max bandwidth:"
print stat.max(), "Mbit/sec"

'''
Print the chart with code below.
'''
y = []

for i in range(len(bandwidth)):
    y.append(i)

plt.subplot(311)
plt.title("Bandwidth in 24h")
plt.ylabel("Bandwidth(Mbit/sec)")
plt.plot(y, bandwidth, 'grey', label='bandwidth', linewidth=2.0)

plt.subplot(312)
plt.title("Retransmitted packet number in 24h")
plt.ylabel("Packets number")
plt.plot(y, retr, 'red', label='retransmission', linewidth=2.0)

plt.subplot(313)
plt.title("Congestion window size in 24h")
plt.ylabel("Size(KB)")
plt.plot(y, cwnd, 'blue', label='cwnd', linewidth=2.0)

plt.show()
