# openc3-cosmos-ros2-turtlebot

OpenC3 COSMOS plugin for **TurtleBot3** (Burger / Waffle) running ROS2.
Bridges to the bot over [`rosbridge_suite`](https://github.com/RobotWebTools/rosbridge_suite)
(TCP transport) and exposes the standard sensor topics as COSMOS telemetry plus
`/cmd_vel` publishing and the `/reset` service as commands.

> **This plugin was generated from the
> [openc3-cosmos-ros2](https://github.com/clayandgen/openc3-cosmos-ros2)
> scaffolding project.** The discovery + generator scripts in that repo
> produced everything under `targets/TURTLEBOT/cmd_tlm/` and the vendored
> `targets/TURTLEBOT/lib/rosbridge_subscribe_protocol.py`. Use that repo to
> regenerate definitions when the bot's topic set changes, or to bootstrap a
> plugin for a different ROS2 robot.

## Topics covered

| Direction | Topic / Service   | Type                              |
| --------- | ----------------- | --------------------------------- |
| TLM       | `/scan`           | `sensor_msgs/msg/LaserScan`       |
| TLM       | `/odom`           | `nav_msgs/msg/Odometry`           |
| TLM       | `/imu`            | `sensor_msgs/msg/Imu`             |
| TLM       | `/battery_state`  | `sensor_msgs/msg/BatteryState`    |
| TLM       | `/joint_states`   | `sensor_msgs/msg/JointState`      |
| TLM + CMD | `/cmd_vel`        | `geometry_msgs/msg/Twist`         |
| CMD (srv) | `/reset`          | `std_srvs/srv/Empty`              |

The full subscription list lives in `targets/TURTLEBOT/lib/topics.txt`.

## On the TurtleBot host

```bash
# Install rosbridge once
sudo apt install ros-${ROS_DISTRO}-rosbridge-suite

# Bring up TurtleBot3 (your usual launch), then start the bridge:
source /opt/ros/${ROS_DISTRO}/setup.bash
ros2 launch rosbridge_server rosbridge_tcp.launch.xml
# rosbridge_tcp listens on tcp://0.0.0.0:9090 by default
# Each JSON envelope is null-terminated; this plugin uses
# OpenC3's terminated_protocol to frame the stream.
```

If COSMOS runs on a different machine from the bot, replace
`host.docker.internal` in `plugin.txt` with the bot's IP (and open port 9090
on the host).

## Install into OpenC3 COSMOS

```bash
rake build VERSION=0.0.1
# upload openc3-cosmos-ros2-turtlebot-0.0.1.gem via Admin → Plugins
```

When prompted, leave the variables at defaults unless rosbridge_tcp runs on a
different host / port:

- `ros2_target_name` = `TURTLEBOT`
- `rosbridge_host`   = `host.docker.internal` (macOS / Windows Docker)
- `rosbridge_port`   = `9090` (rosbridge_tcp default)

## Drive the bot from COSMOS

In Script Runner:

```python
cmd("TURTLEBOT CMD_VEL_PUB with LINEAR '{\"x\":0.2,\"y\":0,\"z\":0}', " \
    "ANGULAR '{\"x\":0,\"y\":0,\"z\":0.5}'")
```

Or call the reset service:

```python
cmd("TURTLEBOT RESET_SRV")
```

## Regenerate against a live bot

Standard topic set was captured offline (`manifest.turtlebot3.json`). If your
TurtleBot exposes extra topics (Nav2, slam_toolbox, custom nodes), regenerate
with the live discovery:

```bash
# From the openc3-cosmos-ros2 checkout, with ROS2 sourced and bot running:
./helpers/discover_ros2.sh \
  --target TURTLEBOT \
  --out-dir /path/to/openc3-cosmos-ros2-turtlebot/targets/TURTLEBOT/cmd_tlm \
  --topics-file /path/to/openc3-cosmos-ros2-turtlebot/targets/TURTLEBOT/lib/topics.txt
```

## Layout

```
plugin.txt                                # COSMOS plugin config + variables
requirements.txt                          # pip deps (websocket-client)
manifest.turtlebot3.json                  # canned manifest for offline regen
targets/TURTLEBOT/
  target.txt
  cmd_tlm/cmd.txt                         # generated commands
  cmd_tlm/tlm.txt                         # generated telemetry
  lib/rosbridge_subscribe_protocol.py     # vendored from openc3-cosmos-ros2
  lib/topics.txt                          # subscription list (one per line)
  procedures/example.py                   # sample drive / reset script
  screens/status.txt                      # minimal status screen
```

## License

MIT. See [LICENSE.txt](LICENSE.txt).
