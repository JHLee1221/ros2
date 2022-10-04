#! usr/bin/python3

from http.server import executable
import os
from unicodedata import name

from launch import LaunchDescription
from launch.actions import LogInfo
from launch_ros.actions import Node

def generate_launch_description():
  return LaunchDescription([
    LogInfo(msg=['Execute the webcam with ros2']),

    Node(
      namespace='camera',
      package='cv_basics',
      executable='image_pub',
      name='cv_basics',
      output='screen'),
    Node(
      namespace='camera',
      package='cv_basics',
      executable='image_sub',
      name='cv_basics',
      output='screen'),
      ])

