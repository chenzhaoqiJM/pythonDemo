#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import sys

import rospy
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from cmoveit import MoveItIkDemo
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped
from moveit_msgs.msg import RobotTrajectory
from rospy.timer import sleep

update_flag = False
def get_pose(msg):
    global update_flag
    global obj
    obj.header = msg.header
    obj.pose = msg.pose
    update_flag = True
    

if __name__ == "__main__":
    # 初始化ROS节点
    rospy.init_node('moveit_ik_demo')
    
    obj = PoseWithCovarianceStamped()   #声明物体信息的消息
    rospy.Subscriber('object_pose', PoseWithCovarianceStamped, get_pose, queue_size=2)

    mymi =  MoveItIkDemo()  #初始化机械臂规划对象
    
    mymi.update_box1()
    mymi.set_obstacle()
    mymi.set_obstacle_fixed() #设置桌面与底座
    mymi.ik_plan_use_pose()     #达到初始位姿
    rospy.sleep(3)

    # mymi.ik_plan_use_angle()
    rate = rospy.Rate(30)
    
    follow_mode = True #跟随模式
    quick_mode = True   #快速抓取模式
    
    while rospy.is_shutdown() == False:
        if  True:
            if (mymi.grasp_flag == True and mymi.place_flag == False or follow_mode == True)  and update_flag == True:
                mymi.update_box1(obj)   #更新物体
                mymi.set_obstacle()     #设置物体
                mymi.ik_plan_use_pose(obj, True) #规划并抓取目标
                if mymi.place_flag == True and follow_mode == False:
                    if quick_mode == False:
                        rospy.sleep(6)
                    else:
                        rospy.sleep(1)
                update_flag = False
                
            if mymi.grasp_flag == False and mymi.place_flag == True and follow_mode == False:
                mymi.clear_obstacle() #清楚物体
                mymi.ik_plan_use_pose_place(mymi.place_pose)    #放置物体
                if mymi.grasp_flag == True:
                    if quick_mode == False:
                        rospy.sleep(6)
                    else:
                        rospy.sleep(1)

            

        rate.sleep() 
        
        
        
    mymi.shut_down()
    rospy.spin()

    
    
