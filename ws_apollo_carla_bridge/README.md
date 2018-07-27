Installation:
```
catkin_make
```  
If `catkin_make` results in an error like `ImportError: No module named cli.find_pkg` then run: `sudo /usr/local/miniconda2/bin//conda install -c auto catkin_pkg` and then retry the installation.

Run with:
```
. devel/setup.bash
rosrun apollo_carla_bridge carla_pose.py
```

**Important! Run everything in this order:**
```
dreamview (/apollo/scripts/bootstrap.sh)
carla_pose.py node (steps from above)
carla simulator
carla_ros_bridge
```