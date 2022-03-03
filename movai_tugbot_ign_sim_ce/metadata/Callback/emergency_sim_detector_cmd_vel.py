# Callback Code
emergency_state = gd.shared.sw_detected
if not emergency_state:
    cmd_to_pub = msg
    gd.oport["cmd_vel_control"].send(cmd_to_pub)