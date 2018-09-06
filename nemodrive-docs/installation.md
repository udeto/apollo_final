# Installation
#### Apollo side
1. Clone the repos
**Recommended**
    - Clone and install apollo from the [official repo](https://github.com/ApolloAuto/apollo)
    - Clone the folder ws_apollo_carla_bridge from [nemodrive/apollo](https://github.com/nemodrive/apollo) repo (see [sparse checkout](https://gist.github.com/sumardi/5559896))
    - Copy the cloned directory to the apollo folder  

    **Alternative**
    - Clone the whole [nemodrive/apollo](https://github.com/nemodrive/apollo) repo and install apollo from there (it is probably behind the official repo)  
  
2. Install (do this in apollo docker)
   ```
   cd ws_apollo_carla_bridge
   catkin_make
   ```

#### Carla side
- Clone [nemodrive/carla](https://github.com/nemodrive/carla)
- Create a catkin workspace anywhere
- ln -s \${carla_root}/carla-ros-bridge \${catkin_workspace}/src/carla-ros-bridge
- cd \${catkin_workspace}
- catkin_make