"""
Visual Feedback API for G1 robot.
Defines sensor data structures and threshold values for obstacle detection.
"""

# Threshold distances in meters
SAFE_DISTANCE = 1.5   # Green zone
WARNING_DISTANCE = 0.7 # Yellow zone
CRITICAL_DISTANCE = 0.3 # Red zone

# Display colors
DISPLAY_COLORS = {
    "SAFE": "GREEN",
    "WARNING": "YELLOW",
    "CRITICAL": "RED"
}