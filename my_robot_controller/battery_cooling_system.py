#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class CoolingSystem(Node):

    def __init__(self):
        super().__init__("battery_cooling_system")
        self.battery_temp_sub = self.create_subscription(Float32,"/battery",self.battery_cooling_system, 10)

    def battery_cooling_system(self, temperature: Float32):
        if temperature.data > 35:
            self.get_logger().info(f"Critical temperature reached! Current temp: {temperature.data:.1f}°C")
        else:
            self.get_logger().info(f"System operating under normal temperature. Current temp: {temperature.data:.1f}°C")


def main(args=None):
    rclpy.init(args=args)

    node = CoolingSystem()
    rclpy.spin(node)

    rclpy.shutdown()