# This node is associated with the tugbot_ignition_battery_adapter node
battery_state = gd.shared.battery_state
if battery_state is not None:
    # publish top_bat_soc
    gd.oport['top_bat_soc'].send(battery_state.percentage)
    # publish top_bat_current
    gd.oport['top_bat_current'].send(battery_state.current)
