import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from custom_interfaces.srv import ComponentStatus

from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor


class ActuationNode(Node):

    def __init__(self):
        super().__init__("actuation_node")

        self.actuation_command_subscriber = self.create_subscription(
            String,
            'actuation_command',
            self.actuation_command_callback,
            10
        )

    def actuation_command_callback(self, msg):
        self.get_logger().info("I heard: %s" % msg.data)

        print(msg)
        if "run" in msg.data:
            self.get_logger().info("actuator is running")
        else:
            self.get_logger().info("nothing happened")

def main(args=None):
    rclpy.init(args=args)

    actuationNode = ActuationNode()

    rclpy.spin(actuationNode)

    """
  Destroy the node explicitly
  (optional - otherwise it will be done automatically
  when the garbage collector destroys the node object)
  """
    actuationNode.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
