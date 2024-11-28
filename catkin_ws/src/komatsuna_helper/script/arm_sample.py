import rospy

from open_manipulator_msgs.srv import *
from open_manipulator_msgs.msg import *
from sensor_msgs.msg import JointState

class TestControl:
    def __init__(self):
        self.joint_func = rospy.ServiceProxy('/goal_joint_space_path', SetJointPosition)
        self.pos_func = rospy.ServiceProxy('/goal_task_space_path', SetKinematicsPose)
        self.sub_pos = None
        self.sub_joint = None
        self.sub_pos_sub = rospy.Subscriber("/gripper/kinematics_pose", KinematicsPose, self.pos_callback)
        self.sub_joint_sub = rospy.Subscriber("/joint_states", JointState, self.joint_callback)

    def pos_callback(self, msg):
        self.sub_pos = msg
        print(msg)

    def joint_callback(self, msg):
        self.sub_joint = msg

    def send_joint(self, joint_angles, path_time = 2.0):
        joint_req = SetJointPositionRequest()
        joint_req.joint_position.joint_name.extend(['joint1', 'joint2', 'joint3', 'joint4'])
        joint_req.joint_position.position.extend(joint_angles)
        joint_req.path_time = path_time
        res = self.joint_func(joint_req)
    
    def send_pos(self, pos, end_effector_name='gripper', path_time = 2.0):
        pos_req = SetKinematicsPoseRequest()
        pos_req.end_effector_name = end_effector_name
        pos_req.kinematics_pose.pose.position.x = pos[0]
        pos_req.kinematics_pose.pose.position.y = pos[1]
        pos_req.kinematics_pose.pose.position.z = pos[2]
        pos_req.kinematics_pose.pose.orientation = self.sub_pos.pose.orientation
        pos_req.path_time = path_time
        res = self.pos_func(pos_req)

if __name__ == '__main__':
    rospy.init_node("test_node")
    test_obj = TestControl()
    test_obj.send_joint([0,0,0,1.57])
    rospy.sleep(2)
    test_obj.send_pos([0.2,0,0.08])
    rospy.spin()