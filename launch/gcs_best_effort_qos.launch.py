from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    image_listener_node = Node(
        package="image_tools",
        executable="showimage",
        parameters=[
            {"reliability": "best_effort"}
        ]
    )
    sensor_listener_node = Node(
        package="operation_control",
        executable="sensor_bridge_listener",
        parameters=[
            {"reliability": "best_effort"}
        ]
    )
    ld.add_action(image_listener_node)
    ld.add_action(sensor_listener_node)
    return ld
