#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import math
import random

class BatteryTemperatureSensor(Node):

    def __init__(self):
        super().__init__("battery_temp_sensor")
        self.counter = 0
        self.create_timer(0.5, self.send_temperature_data)
        self.battery_temp_pub = self.create_publisher(Float32,"/battery", 10)

    def send_temperature_data(self):
        base_temp = 20*math.sin(0.047*self.counter) + 20
        noise = random.gauss(0, 0.5)
        temperature = Float32()
        temperature.data = base_temp + noise
        self.battery_temp_pub.publish(temperature)

        self.counter += 1
        


def main(args=None):
    rclpy.init(args = args)

    node = BatteryTemperatureSensor()
    rclpy.spin(node)

    rclpy.shutdown

if __name__ == "__main__":
    main()