# Callback Code
gd.shared.sw_detected = msg.data
if msg.data:
    cmd_to_pub = Twist()
    cmd_to_pub.linear.x = 0.0
    cmd_to_pub.angular.z = 0.0
    gd.oport["cmd_vel_control"].send(cmd_to_pub)
    gd.oport["release_cmd"].send(False)