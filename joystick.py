from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

topic_name = 'cmd_vel'

class TurtleCmdPub():
    def __init__(self, node):
        super(TurtleCmdPub, self).__init__()
        self.node = node
        
        self.pub_velocity = Twist()
        self.pub_velocity.linear.x = 0.0
        self.pub_velocity.angular.z = 0.0
        self.sub_velocity = Joy()
        self.pub_velocity.linear.x = 0.0
        self.pub_velocity.angular.z = 0.0
        
        qos = QoSProfile(depth=1)
        self.publisher = self.node.create_publisher(Twist, topic_name, qos)
        self.subscriber = self.node.create_subscriber(Joy, topic_name, self.get_velocity, qos)
        
    def get_velocity(self, joy):
        self.sub_velocity = joy
        
        