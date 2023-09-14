from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
  return LaunchDescription([
      Node(
          package='brain',
          namespace='robot_one',
          executable='brain',
          name='brain_node'
      ),
      Node(
          package='perception',
          namespace='robot_one',
          executable='perception',
          name='perception_node'
      ),
      Node(
          package='actuation',
          namespace='robot_one',
          executable='actuation',
          name='actuation_node'
      )
  ])
