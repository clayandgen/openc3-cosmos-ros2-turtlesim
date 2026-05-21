# Sample turtlesim procedure — drives turtle1 in a square, then draws a star.
import time
import math

# Show the overview telemetry screen
display_screen("TURTLESIM", "overview")

# Reset the sim and clear drawings
cmd("TURTLESIM RESET_SRV")
wait(2)

# --- Drive in a square ---
for _ in range(4):
    # Move forward
    cmd("TURTLESIM TURTLE1_CMD_VEL_PUB with LINEAR_X 2.0, ANGULAR_Z 0.0")
    wait(2)
    # Stop
    cmd("TURTLESIM TURTLE1_CMD_VEL_PUB with LINEAR_X 0.0, ANGULAR_Z 0.0")
    wait(0.5)
    # Turn 90 degrees
    cmd("TURTLESIM TURTLE1_CMD_VEL_PUB with LINEAR_X 0.0, ANGULAR_Z 1.5708")
    wait(1)
    # Stop
    cmd("TURTLESIM TURTLE1_CMD_VEL_PUB with LINEAR_X 0.0, ANGULAR_Z 0.0")
    wait(0.5)

# Check final pose
pose = tlm("TURTLESIM TURTLE1_POSE X")
print(f"Final X position: {pose}")

# --- Clear and draw a star ---
cmd("TURTLESIM CLEAR_SRV")
wait(1)

# Teleport to starting position
cmd("TURTLESIM TURTLE1_TELEPORT_ABSOLUTE_SRV with X 5.5, Y 3.0, THETA 1.5708")
wait(0.5)

# Set pen to red
cmd("TURTLESIM TURTLE1_SET_PEN_SRV with R 255, G 50, B 50, WIDTH 3, OFF 0")
wait(0.5)

# Draw a 5-pointed star using teleport_relative
star_angle = math.radians(144)  # exterior angle for a 5-pointed star
for _ in range(5):
    cmd("TURTLESIM TURTLE1_TELEPORT_RELATIVE_SRV with LINEAR 4.0, ANGULAR 0.0")
    wait(0.3)
    cmd("TURTLESIM TURTLE1_TELEPORT_RELATIVE_SRV with LINEAR 0.0, ANGULAR {a}".format(a=star_angle))
    wait(0.3)

# Rotate to face right using the action
cmd("TURTLESIM TURTLE1_ROTATE_ABSOLUTE_ACT with THETA 0.0")
wait(2)

print("Done! Check the turtlesim window.")
