
from platform import node
import numpy as np
import rclpy
import subprocess
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
import sys
import signal
import time

def signal_handler(signal, frame):
    print("You pressed Ctrl + c  ... exit program... ")
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

class turtle():
    def __init__(self):
        super().__init__(turtle, self).__init__()
        qos = QoSProfile(depth=10)
        self.turtlejoy_publisher = self.create_publisher(Twist, '/cmd_vel', qos)
        self.turtlejoy_subscriber = self.create_publisher(Joy, '/joy', self.turtlejoy_publsih_msg)
        self.rate = rclpy.Rate(20)
        self.node = node
    def turtlejoy_publsih_msg(self, data):
        global inn
        inn = 0
        self.joy = data.buttons
        self.joy2 = data.axes
        if np.shape(self.joy) [0]>0:
            inn=1
            self.A=self.joy[0]
            self.X=self.joy[1]
            self.Y=self.joy[2]
            self.B=self.joy[3]
        if np.shape(self.joy2)[0]>0:
            inn=1
            self.linear = self.joy2[0]
            self.angular = self.joy2[1]
        if inn ==1:
            if self.joy[0]==0 and self.joy[1]==0 and self.joy[2]==0 and self.joy[3]==0 and self.joy2[0]==0 and self.joy2[1]==0:
                inn =0
            else:
                pass
        def moving(self, vel_msg):
            self.turtlejoy_publisher.publish(vel_msg)

data = Joy()
vel_msg = Twist()

turtle1 = turtle()
turtle1.turtlejoy_publsih_msg(data)
global inn
inn =0

if __name__ == '__main__':
    while 1:
      if inn ==1:
          if turtle1.A ==1:
              vel_msg.linear.x = turtle1.linear*0.1
              vel_msg.angular.z = turtle1.angular*1.2
          elif turtle1.X==1:
              p=subprocess.Popen('ros2 topic pub /reset std_msgs/Empty "{}"', shell = True)
              time.sleep(2)
              p.terminate()
          elif turtle1.Y ==1:
              vel_msg.linear.x = turtle1.linear*0.22
              vel_msg.angular.z = turtle1.angular*2
          elif turtle1.B ==1:
              vel_msg.linear.x = 0
              vel_msg.angular.z = 0
          turtle1.moving(vel_msg)
      else:
        print('no date in')
      turtle1.rate.sleep()
