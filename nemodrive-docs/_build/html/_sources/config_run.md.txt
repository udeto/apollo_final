# Config
Most setup is to be done on carla's side of the bridge, in the file `${carla-ros-bridge}/conf/settings.yaml`. Modify this file to add / remove sensors.

Camera image and information will be published on topics with the following format:
- ***\${camera_name}/image_raw*** -> *sensor_msgs/Image*
- ***\${camera_name}/camera_info*** -> *sensor_msgs/CameraInfo* (camera's intrinsic parameters)

Vehicle information is published on ***/player_vehicle***.
Carla listens to control on ***/carla_control***.

# Running
**To run the bridge do everything in the order specified!!!**
Run the apollo part first:
```
dev_Start && dev_into && bootstrap.sh + modules: localization, perception, planning, routing, prediction, control
(in docker) cd ws_apollo_carla_bridge
(in docker) source devel/setup.bash
(in docker) rosrun apollo_carla_bridge bridge.py
```
Now run the carla part:
```
start carla
cd ${carla_ros_bridge_ws}
source devel/setup.bash
roslaunch carla_ros_bridge client.launch
```

If you've done everything correctly, you should see the car in dreamview. :)