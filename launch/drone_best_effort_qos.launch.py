from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    image_publisher_node = Node(
        package="image_tools",
        executable="cam2image",
        output='screen',
        parameters=[
            {"reliability": "best_effort"}
        ]
    )
    sensor_publisher_node = Node(
        package="px4_ros_com",
        executable="sensor_combined_listener",
        output='screen',
        parameters=[
            {"reliability": "best_effort"}
        ]
    )
    offboard_control_node = Node(
        package="px4_ros_com",
        executable="offboard_control",
        output='screen',
        parameters=[
            {"reliability": "best_effort"}
        ]
    )
    ld.add_action(image_publisher_node)
    ld.add_action(sensor_publisher_node)
    ld.add_action(offboard_control_node)
    return ld
