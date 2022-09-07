#!/usr/bin/python3

import sys
import signal
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

#종료시 종료 메시지
def signal_handler(signal, frame):
    print('\nYou pressed Ctrl+C... exit joy_program.')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

class TurtleJoy(Node):

#Node 초기화, pub, sub 지정
    def __init__(self):
        super().__init__('turtlesim_joy')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscriber = self.create_subscription(Joy, '/joy', self.sub_callback, 10)

#Sub_callback 함수
    def sub_callback(self, data):
        msg = Twist()
        msg.linear.x = data.axes[1]
        msg.angular.z = data.axes[0]

        self.get_logger().info('linear: %f ; angular %f' %(msg.linear.x, msg.angular.z))

        self.publisher.publish(msg)

#main 함수
def main(args=None):
    rclpy.init(args=args)

    turtle_joy_class = TurtleJoy()
    rclpy.spin(turtle_joy_class)

    TurtleJoy.destory_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()
