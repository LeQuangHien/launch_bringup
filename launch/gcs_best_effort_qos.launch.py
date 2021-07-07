from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    image_listener_node = Node(
        package="image_tools",
        executable="showimage",
        output='screen',
        parameters=[
            {"reliability": "best_effort"}
        ]
    )
    sensor_listener_node = Node(
        package="operation_control",
        executable="sensor_bridge_listener",
        output='screen',
        parameters=[
            {"reliability": "best_effort"}
        ]
    )
    setpoint_advertiser_node = Node(
        package="operation_control",
        executable="setpoint_advertiser",
        output='screen',
        parameters=[
            {"reliability": "best_effort"}
        ]
    )
    ld.add_action(image_listener_node)
    ld.add_action(sensor_listener_node)
    ld.add_action(setpoint_advertiser_node)
    return ld
