#!/usr/bin/env python

import rospy

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math
import numpy

pose = None
goal_pose = None

def callbackPose(msg):
	global pose
	pose = msg

def callbackgoalpose(msg):
	global goal_pose
	goal_pose = msg

def move(speed,goal):
	while pose == None:
		rospy.sleep(0.1)
	
	goal_x = goal.x
	goal_y = goal.y
	print("Hedef pozisyon",goal_x,goal_y)

	vel_msg = Twist()

	while True:
		dist = math.sqrt((pose.x-goal_x)**2 + (pose.y-goal_y)**2)
		print("Hedefe kalan mesafe: ", dist)
		
		if dist>0.1:
			vel_msg.linear.x = speed
			vel_pub.publish(vel_msg)

		else:
			vel_msg.linear.x = 0
			vel_pub.publish(vel_msg)
			break
	
		loop_rate.sleep()

def rotate(speed,angle):
	while pose == None:
		rospy.sleep(0.1)

	vel_msg = Twist()
	pose_theta = pose.theta

	if pose_theta < 0:
		pose_theta += 2.0*math.pi

	if angle < 0:
		angle += 2.0*math.pi

	diff = angle - pose_theta
	print("Aci farki: ",abs(diff))

	if abs(diff) < math.pi:
		speed = speed*numpy.sign(diff)
	else:
		speed = -1.0*speed*numpy.sign(diff)

	while True:
		pose_theta = pose.theta
		if pose_theta < 0:
			pose_theta += 2.0*math.pi

		diff = angle - pose_theta
		print("Aci farki: ",diff)

		if abs(diff) > 0.01:
			vel_msg.angular.z = speed
			vel_pub.publish(vel_msg)

		else:
			vel_msg.angular.z = 0
			vel_pub.publish(vel_msg)
			break


if __name__ == "__main__":

	rospy.init_node("motioncontroller",anonymous=True)
	rospy.Subscriber("/turtle1/pose", Pose,callbackPose)
	rospy.Subscriber("/cmd/goal_pose", Pose,callbackgoalpose)
	vel_pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size = 5)
	loop_rate = rospy.Rate(5)

	while not rospy.is_shutdown():

		fark_x = goal_pose.x - pose.x
		fark_y = goal_pose.y - pose.y

		angle = math.atan2(fark_y,fark_x)
		rotate(0.05,angle)
		move(0.2,goal_pose)
		rotate(0.05,goal_pose.theta)
		
		loop_rate.sleep()