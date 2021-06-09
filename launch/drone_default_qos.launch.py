from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    image_publisher_node = Node(
        package="image_tools",
        executable="cam2image"
    )
    sensor_publisher_node = Node(
        package="px4_ros_com",
        executable="sensor_combined_listener"
    )
    ld.add_action(image_publisher_node)
    ld.add_action(sensor_publisher_node)
    return ld
