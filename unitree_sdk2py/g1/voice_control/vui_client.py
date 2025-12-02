"""
VUIClient starter module
Processes voice commands and sends them to the robot
"""

from .vui_client_api import VOICE_COMMANDS
import random  # Simülate

class VUIClient:
    def __init__(self):
        self.initialized = False

    def initialize(self):
        # Initialize voice recognition system (placeholder)
        self.initialized = True
        print("VUI Client initialized.")

    def listen_command(self):
        """
        Simulate listening to a voice command.
        Replace with actual voice recognition in real implementation.
        """
        return random.choice(list(VOICE_COMMANDS.keys()))

    def execute_command(self, command):
        if command in VOICE_COMMANDS:
            print(f"[Voice Command] Executing: {VOICE_COMMANDS[command]}")
        else:
            print(f"[Voice Command] Unknown command: {command}")

# Example usage
if __name__ == "__main__":
    client = VUIClient()
    client.initialize()
    while True:
        cmd = client.listen_command()
        client.execute_command(cmd)
