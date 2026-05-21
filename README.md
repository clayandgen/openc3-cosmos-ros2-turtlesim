# openc3-cosmos-ros2-turtlesim

<p align="center">
  <img src="public/store_img.png" alt="openc3-cosmos-ros2-turtlesim" />
</p>

OpenC3 COSMOS plugin for **turtlesim** running on ROS2.
Bridges via [`rosbridge_suite`](https://github.com/RobotWebTools/rosbridge_suite)
(WebSocket transport).

> Generated from [openc3-cosmos-ros2](https://github.com/clayandgen/openc3-cosmos-ros2).
> Use that repo to regenerate when the topic set changes.

## Discovered interfaces

| Direction | Name | Type |
| --------- | ---- | ---- |
| TLM + CMD | `/turtle1/cmd_vel` | `geometry_msgs/msg/Twist` |
| TLM | `/turtle1/color_sensor` | `turtlesim/msg/Color` |
| TLM + CMD | `/turtle1/pose` | `turtlesim/msg/Pose` |
| CMD (srv) | `/clear` | `std_srvs/srv/Empty` |
| CMD (srv) | `/kill` | `turtlesim/srv/Kill` |
| CMD (srv) | `/reset` | `std_srvs/srv/Empty` |
| CMD (srv) | `/spawn` | `turtlesim/srv/Spawn` |
| CMD (srv) | `/turtle1/set_pen` | `turtlesim/srv/SetPen` |
| CMD (srv) | `/turtle1/teleport_absolute` | `turtlesim/srv/TeleportAbsolute` |
| CMD (srv) | `/turtle1/teleport_relative` | `turtlesim/srv/TeleportRelative` |
| CMD (act) | `/turtle1/rotate_absolute` | `turtlesim/action/RotateAbsolute` |

Parameters (background RGB, holonomic, etc.) are also exposed as GET/SET commands.

## Setup

On the ROS2 host:

```bash
sudo apt install ros-${ROS_DISTRO}-rosbridge-suite
source /opt/ros/${ROS_DISTRO}/setup.bash
ros2 run turtlesim turtlesim_node
ros2 launch rosbridge_server rosbridge_websocket_launch.xml
```

## Install into COSMOS

```bash
rake build VERSION=0.0.1
# Upload openc3-cosmos-ros2-turtlesim-0.0.1.gem via Admin → Plugins
```

Plugin variables (set defaults or override at install):

- `rosbridge_host` — host running rosbridge (default: `host.docker.internal`)
- `rosbridge_port` — WebSocket port (default: `9090`)

## Example usage

In Script Runner:

```python
# Publish a velocity command
cmd("TURTLESIM TURTLE1_CMD_VEL_PUB with LINEAR '{\"x\":2.0,\"y\":0,\"z\":0}', ANGULAR '{\"x\":0,\"y\":0,\"z\":1.8}'")

# Teleport the turtle
cmd("TURTLESIM TURTLE1_TELEPORT_ABSOLUTE_SRV with X 5.0, Y 5.0, THETA 0.0")

# Clear the drawing
cmd("TURTLESIM CLEAR_SRV")
```

## Regenerate

```bash
cd ../openc3-cosmos-ros2
./bin/scaffold-ros2-plugin \
  --target TURTLESIM \
  --out ../openc3-cosmos-ros2-turtlesim \
  --discover --force
```

## License

MIT.
