"""
Visual Feedback Client
Processes sensor data and provides visual feedback to the user.
"""

import time
import random  # Simulated sensor data
from .visual_feedback_api import SAFE_DISTANCE, WARNING_DISTANCE, CRITICAL_DISTANCE, DISPLAY_COLORS

class VisualFeedbackClient:
    def __init__(self):
        self.initialized = False

    def initialize(self):
        # Initialize sensors or connections if needed
        self.initialized = True
        print("Visual Feedback Client initialized.")

    def get_obstacle_distance(self):
        """
        Simulate reading distance from sensors.
        Replace with actual sensor reading in real implementation.
        """
        # Random distance between 0.1 and 2.0 meters
        return round(random.uniform(0.1, 2.0), 2)

    def update_display(self, distance: float):
        """
        Update visual feedback based on distance
        """
        if distance >= SAFE_DISTANCE:
            color = DISPLAY_COLORS["SAFE"]
        elif distance >= WARNING_DISTANCE:
            color = DISPLAY_COLORS["WARNING"]
        else:
            color = DISPLAY_COLORS["CRITICAL"]

        # In real robot: send command to LED/display
        print(f"[Visual Feedback] Distance: {distance} m → {color}")

# Example usage
if __name__ == "__main__":
    client = VisualFeedbackClient()
    client.initialize()
    while True:
        d = client.get_obstacle_distance()
        client.update_display(d)
        time.sleep(1)
