import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor


class ActuationNode(Node):

    def __init__(self):
        super().__init__("actuation_node")
        print("hey")
        self.actuation_command_topic = self.declare_parameter(
            "actuation_command_topic",
            "None"
        )

        self.get_parameter_values()
        self.callback_group = ReentrantCallbackGroup()

        self.actuation_command_subscriber = self.create_subscription(
            String,
            self.actuation_command_topic,
            self.actuation_command_callback,
            10,
            callback_group=self.callback_group
        )
    print("wjkhd")
    def get_parameter_values(self):
        self.actuation_command_topic = self.get_parameter(
            'actuation_command_topic').get_parameter_value().string_value
        print("getparameter")

    def actuation_command_callback(self, msg):
        self.get_logger().info("I heard: %s" % msg.data)
        if "run" in msg.data:
            self.get_logger().info("actuator is running")
        else:
            self.get_logger().info("nothing happened")
        print("actuation callback")


def main(args=None):
    rclpy.init(args=args)

    actuationNode = ActuationNode()
    executor = MultiThreadedExecutor()
    rclpy.spin(actuationNode, executor)

    actuationNode.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
