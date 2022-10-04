#!usr/bin/python3

import sys
import signal
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def signal_handler(signal, frame):
    print('\nYou pressed Ctrl+C... exit image pub.')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

class ImagePub(Node):

  def __init__(self):

    super().__init__('image_pub')

    self.publisher_ = self.create_publisher(Image, 'video_frames', 10)

    timer_period = 0.1

    self.timer = self.create_timer(timer_period, self.timer_callback)

    self.cap = cv2.VideoCapture(4)

    self.br = CvBridge()

  def timer_callback(self):
    ret, frame = self.cap.read()

    if ret == True:
      self.publisher_.publish(self.br.cv2_to_imgmsg(frame))

    self.get_logger().info('Publishing video frame')

def main(args=None):

  rclpy.init(args=args)

  image_pub = ImagePub()


  rclpy.spin(image_pub)

  image_pub.destroy_node()

  rclpy.shutdown()

if __name__ == '__main__':
  main()
