#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped
from rospy.timer import sleep
from cobjectfollow import MoveItIkFollow
from std_msgs.msg import Bool

update_flag = False
def get_pose(msg):
    global update_flag
    global obj
    obj.header = msg.header
    obj.pose = msg.pose
    update_flag = True

#状态变量回调函数
def get_state(msg):
    global state
    global state_update_flag
    state = msg.data
    state_update_flag = True
    

if __name__ == "__main__":
    # 初始化ROS节点
    rospy.init_node('moveit_ik_follow')

    #初始化跟随对象
    follow = MoveItIkFollow()
    
    #初始化物体的消息对象
    obj = PoseWithCovarianceStamped()
    rospy.Subscriber('object_pose', PoseWithCovarianceStamped, get_pose, queue_size=2)
    
    #初始化是否执行跟随的状态变量
    state = False
    state_update_flag = False
    rospy.Subscriber('follow_state', Bool, get_state, queue_size=2)

    rate = rospy.Rate(30)
    follow.clear_obstacle() #清除所有物体
    while rospy.is_shutdown() == False:
        
        if state == True:
            follow.update_box1(obj)#让物体跟随机械臂
            
        if state == False:
            if state_update_flag == False:
                pass
            else:
                follow.clear_obstacle() 
                follow.place_obstacle() #放下物体
                state_update_flag = False
               
        rate.sleep() 
        

    rospy.spin()

    
    
