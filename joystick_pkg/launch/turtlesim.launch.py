#!/usr/bin/python3

from http.server import executable
import os
from unicodedata import name

from launch import LaunchDescription
from launch.actions import LogInfo
from launch_ros.actions import Node

def generate_launch_description():
  return LaunchDescription([
    LogInfo(msg=['Execute the turtlesim joy with turtlesim node']),

    Node(
      namespace='turtle1',
      package='joystick_pkg',
      executable='turtlesim_joy',
      name='turtlesim_joy',
      output='screen'),

    Node(
      package='turtlesim',
      executable='turtlesim_node',
      name='turtlesim',
      output='screen'),

    Node(
      package='joy',
      executable='joy_node',
      name='joy'),
  ])
