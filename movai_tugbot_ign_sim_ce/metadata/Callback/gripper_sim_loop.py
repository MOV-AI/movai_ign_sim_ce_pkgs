# Get orientation quaternion of the gripper
quaternion = [msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w]

# Isolate yaw angle (radians)
(_, _, yaw) = tf.transformations.euler_from_quaternion(quaternion)

# Round yaw angle to 3 decimal spaces
center_state = round(yaw,3)

# Read parameters
center_tolerance = gd.params['center_pos_tolerance']
center_force = gd.params['center_force']

# Check if centered withing tolerance
center_sensor =  (-center_tolerance <= center_state <= center_tolerance)

# Assign direction for the center gripper message
if gd.shared.center_gripper:
    if center_state > center_tolerance:
        msg2send = -center_force
    elif center_state < -center_tolerance:
        msg2send = center_force
    else:
        gd.shared.center_gripper = False
        msg2send = 0.0
    gd.oport['center_action'].send(msg2send)
    
# Send the simulated gripper center sensor (True if gripper is centered, withing tolerance)
gd.oport["center_sensor"].send(center_sensor)

# Send the gripper position
gd.oport["center_state"].send(center_state)

# Send the roller position
if center_state <= 0.0:
    gd.oport["roller_switch_detect"].send(True)
else:
    gd.oport["roller_switch_detect"].send(False)

    
