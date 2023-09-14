from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
  return LaunchDescription([

      Node(
          package='brain',
          namespace='robot_one',
          executable='brain',
          name='brain_node',
          parameters=[
              {'trashDetectionTopic': 'trash_detection',
               'componentStatusService': 'component_status',
               }
          ]
      ),
      Node(
          package='perception',
          namespace='robot_one',
          executable='perception',
          name='perception_node',
          parameters=[
              {'cameraTopic': 'camera',
               'trashDetectionTopic': 'trash_detection',
               'componentStatusService': 'component_status',
               }
          ]
      ),
      Node(
          package='actuation',
          namespace='robot_one',
          executable='actuation',
          name='actuation_node',
          parameters=[
              {
                  'actuation_command_topic': 'actuation_command'
               }
          ]
      )
  ])
  
