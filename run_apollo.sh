rosparam set use_sim_time True

for i in {1..150}
do

    echo "start tf_broadcaster"
    python tf_broadcaster.py &

    echo "start apollo modules"
    localization.sh
    routing.sh
    planning.sh
    perception.sh
    prediction.sh
    control.sh
    relative_map.sh

    sleep 3

    echo "starting calra-apollo bridge"
    source /apollo/ws_apollo_carla_bridge/devel/setup.bash
    rosparam set use_sim_time True
    rosrun apollo_carla_bridge bridge.py &

    echo "wait for the route to terminate"
    python wait_during_route.py

    echo "stop apollo modules and bridge"
    rosnode kill carla_to_apollo_data
    
    localization.sh stop
    routing.sh stop
    planning.sh stop
    perception.sh stop
    prediction.sh stop
    control.sh stop
    relative_map.sh stop

    rosnode kill tf_broadcaster
    sleep 2
    rosnode cleanup <<< 'y'
    echo "cleanup done"
done