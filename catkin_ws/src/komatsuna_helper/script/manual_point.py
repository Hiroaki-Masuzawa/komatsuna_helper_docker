#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
import numpy as np
import math
import cv2

import message_filters
from sensor_msgs.msg import Image, CameraInfo
from geometry_msgs.msg import PoseStamped
from cv_bridge import CvBridge

class ManualPointNode:
    def __init__(self):

        rospy.init_node('manualpoint_rosnode', anonymous=True)

        self.bridge = CvBridge()

        self.window_name = 'image'
        # cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)
        # cv2.imshow('image', np.zeros((100,100,3), dtype=np.uint8))
        # cv2.waitKey(10)
        # cv2.setMouseCallback(self.window_name, self.window_callback)
        self.setCallback = False
        self.resize_ratio = 0.5

        self.color_image_sub = message_filters.Subscriber('/k4a/rgb/image_rect_color', Image)
        # self.color_info_sub = message_filters.Subscriber('/k4a/rgb/camera_info', CameraInfo)
        self.depth_image_sub = message_filters.Subscriber('/k4a/depth_to_rgb/image_raw', Image)
        self.depth_info_sub = message_filters.Subscriber('/k4a/depth_to_rgb/camera_info', CameraInfo)
        self.ts = message_filters.ApproximateTimeSynchronizer(
            [self.color_image_sub, self.depth_image_sub, self.depth_info_sub], 40, 0.05)
        self.ts.registerCallback(self.data_sub_callback)

        self.pose_pub = rospy.Publisher('clicked_position', PoseStamped, queue_size=10)
    
    def window_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONUP:
            x = math.floor(x/self.resize_ratio)
            y = math.floor(y/self.resize_ratio)
            pose = PoseStamped()
            pose.header = self.depth_data.header
            depth = self.cv_depth_data[y,x]/1000.0
            pose.pose.position.x = (x-self.depth_info.K[2])/self.depth_info.K[0] * depth
            pose.pose.position.y = (y-self.depth_info.K[5])/self.depth_info.K[4] * depth
            pose.pose.position.z = depth
            pose.pose.orientation.x = 0
            pose.pose.orientation.y = 0
            pose.pose.orientation.z = 0
            pose.pose.orientation.w = 1
            print(pose)
            self.pose_pub.publish(pose)

    def data_sub_callback(self,  color_data,  depth_data, depth_info):
        self.depth_data = depth_data
        self.cv_color_data = self.bridge.imgmsg_to_cv2(color_data, "bgr8")
        self.cv_depth_data = self.bridge.imgmsg_to_cv2(depth_data, "passthrough")
        self.depth_info = depth_info
        new_w = math.floor(self.cv_color_data.shape[1] * self.resize_ratio)
        new_h = math.floor(self.cv_color_data.shape[0] * self.resize_ratio)
        resize=cv2.resize(self.cv_color_data, (new_w,new_h))
        cv2.imshow(self.window_name, resize)
        cv2.waitKey(10)
        if not self.setCallback:
            cv2.setMouseCallback(self.window_name, self.window_callback)
            self.setCallback = True
    
if __name__ =='__main__':
    node = ManualPointNode()
    rospy.spin()
