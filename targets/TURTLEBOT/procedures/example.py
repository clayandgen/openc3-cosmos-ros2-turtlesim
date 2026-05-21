# Example TurtleBot3 COSMOS Script Runner procedures.
# Drives the bot in a slow circle, then resets.

from openc3.script import *
import time


def drive(linear_x: float = 0.15, angular_z: float = 0.5):
    """Publish a Twist to /cmd_vel via the TURTLEBOT plugin."""
    cmd(
        "TURTLEBOT CMD_VEL_PUB "
        f'with LINEAR \'{{"x":{linear_x},"y":0,"z":0}}\', '
        f'ANGULAR \'{{"x":0,"y":0,"z":{angular_z}}}\''
    )


def stop():
    drive(0.0, 0.0)


def reset():
    cmd("TURTLEBOT RESET_SRV")


def circle_demo(seconds: int = 6):
    drive(0.15, 0.5)
    time.sleep(seconds)
    stop()
