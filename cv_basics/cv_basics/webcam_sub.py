#!usr/bin/python3

import signal
import sys
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def signal_handler(signal, frame):
    print('\nYou pressed Ctrl+C... exit image sub.')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

class ImageSub(Node):

  def __init__(self):

    super().__init__('image_sub')

    self.subscriber = self.create_subscription(
      Image,
      'video_frames',
      self.listener_callback,
      10)
    self.subscriber

    self.br = CvBridge()

  def listener_callback(self, data):

    self.get_logger().info('Receiving video frame')

    current_frame = self.br.imgmsg_to_cv2(data)

    # Display image
    cv2.imshow("camera", current_frame)

    cv2.waitKey(1)

def main(args=None):

  rclpy.init(args=args)

  image_sub = ImageSub()

  rclpy.spin(image_sub)

  image_sub.destroy_node()

  rclpy.shutdown()

if __name__ == '__main__':
  main()
