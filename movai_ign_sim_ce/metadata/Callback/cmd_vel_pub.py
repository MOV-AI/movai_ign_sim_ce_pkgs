value = geometry_msgs.msg.Twist()
value.linear.x = gd.params['linear_x']
value.linear.y = gd.params['linear_y']
value.linear.z = gd.params['linear_z']
value.angular.z = gd.params['angular']
gd.oport['cmd_msgs_publisher'].send(value)
if count > 10:
    gd.oport['exit'].send()