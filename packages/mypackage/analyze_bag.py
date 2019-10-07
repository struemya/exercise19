#!/usr/bin/env python
import rosbag
import numpy as np
def get_average(time_array):
	return (time_array[-1]-time_array[0])/len(time_array)

def get_min(time_array):
	if len(time_array) > 1:
		return min(np.diff(time_array))
	else: return 0

def get_max(time_array):
	if len(time_array) > 1:
		return max(np.diff(time_array))
	else: return 0
def get_median(time_array):
	if len(time_array) > 1:
		return np.median(np.diff(time_array))
	else: return 0

def print_stats(topic, time_array):
	print("{}: num_messages: {} period: min: {} max: {} average: {} median: {}".format(topic, len(time_array), get_min(time_array), get_max(time_array), get_average(time_array), get_median(time_array)))
bag = rosbag.Bag('/home/example_rosbag_H3.bag')
time=[]

#print(bag.read_messages(topics=['/tesla/camera_node/camera_info']))
for topic, msg, t in bag.read_messages(topics=['/tesla/camera_node/camera_info']):
	sec = t.to_sec()
	time.append(sec)
print_stats(topic, time)
time=[]

for topic, msg, t in bag.read_messages(topics=['/tesla/line_detector_node/segment_list']):
	sec = msg.header.stamp.to_sec()
	time.append(sec)
print_stats(topic, time)
time=[]

for topic, msg, t in bag.read_messages(topics=['/tesla/wheels_driver_node/wheels_cmd']):
	sec = msg.header.stamp.to_sec()
	time.append(sec)
	
print_stats(topic, time)

bag.close()
