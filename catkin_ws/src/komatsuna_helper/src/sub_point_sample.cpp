#include "ros/ros.h"
#include "geometry_msgs/PoseStamped.h"


void poseCallback(const geometry_msgs::PoseStamped::ConstPtr& msg)
{
  ROS_INFO("Messgae receive.");
  ROS_INFO("    posi_x : %lf", msg->pose.position.x);
  ROS_INFO("    posi_y : %lf", msg->pose.position.y);
  ROS_INFO("    posi_z : %lf", msg->pose.position.z);
  ROS_INFO("    ori_x  : %lf", msg->pose.orientation.x);
  ROS_INFO("    ori_y  : %lf", msg->pose.orientation.y);
  ROS_INFO("    ori_z  : %lf", msg->pose.orientation.z);
  ROS_INFO("    ori_w  : %lf", msg->pose.orientation.w);
  ROS_INFO("");
}

int main(int argc, char **argv)
{

  ros::init(argc, argv, "sub_point_sample");
  ros::NodeHandle n;

  ros::Subscriber sub = n.subscribe("clicked_position", 1, poseCallback);
  ros::spin();

  return 0;
}