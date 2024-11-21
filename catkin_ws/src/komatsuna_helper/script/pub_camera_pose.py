#!/usr/bin/env python3
# coding: UTF-8

import os
import yaml

import tf.transformations as tr
# http://docs.ros.org/en/jade/api/tf/html/python/transformations.html

import tf
import rospy
import roslib.packages
from std_srvs.srv import *
import numpy as np

class CameraTFPublisher:
    def __init__(self):
        config_file = os.path.join(roslib.packages.get_pkg_dir('komatsuna_helper'), 'config', 'init_pose.yaml')
        if os.path.exists(config_file):
            with open(config_file) as f:
                dat = yaml.safe_load(f)
            self.pos_x, self.pos_y, self.pos_z = dat['position']
            self.rot_x, self.rot_y, self.rot_z, self.rot_w = dat['orientation']
        else :
            self.pos_x, self.pos_y, self.pos_z = 0,0,0
            self.rot_x, self.rot_y, self.rot_z, self.rot_w = 0,0,0,1
        print(self.pos_z)
        self.global_fix_frame = 'stage'
        self.ar_marker_frame = 'ar_marker_187'
        self.camera_frame = 'camera_base'        
        self.listener = tf.TransformListener()
        self.br = tf.TransformBroadcaster()
        self.srv = rospy.Service('setcamerapos', Trigger, self.setpose)

        rospy.Timer(rospy.Duration(0.01), self.timer_callback)

    def timer_callback(self, event):
        self.br.sendTransform((self.pos_x, self.pos_y, self.pos_z),
                [self.rot_x, self.rot_y, self.rot_z, self.rot_w],
                rospy.Time.now(),
                self.camera_frame,
                self.global_fix_frame)

    def setpose(self, req):
        now = rospy.Time.now()
        self.listener.waitForTransform(self.camera_frame, self.ar_marker_frame, now, rospy.Duration(5.0))
        tf1 = self.listener.lookupTransform(self.camera_frame,  self.ar_marker_frame, now)
        self.pos_x, self.pos_y, self.pos_z = -tf1[0][0], -tf1[0][1], -tf1[0][2]
        self.rot_x, self.rot_y, self.rot_z, self.rot_w = -tf1[1][0], -tf1[1][1], -tf1[1][2], tf1[1][3]
        print(self.pos_x, self.pos_y, self.pos_z)
        print(self.rot_x, self.rot_y, self.rot_z, self.rot_w)
        return TriggerResponse(True, "")

if __name__ == '__main__':
    rospy.init_node('camera_calib_node')
    ctp = CameraTFPublisher()
    rospy.spin()
