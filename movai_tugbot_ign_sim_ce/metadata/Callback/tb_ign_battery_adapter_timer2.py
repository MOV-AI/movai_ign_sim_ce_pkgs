# This node is associated with the tugbot_ignition_battery_adapter node
battery_state = gd.shared.battery_state
if battery_state is not None:
    # publish time
    # the time is the difference between the last valid reading and now
    # since the reading in the simulator is always correct, we send zero, but,
    # in the real robot it could vary due to hardware latency (eg: bluetooth issues)
    gd.oport['time'].send(0)