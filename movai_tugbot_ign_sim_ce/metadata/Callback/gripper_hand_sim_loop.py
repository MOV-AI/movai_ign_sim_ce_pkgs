# Get orientation quaternion
quaternion = [msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w]

# Isolate yaw angle (radians)
(_, pitch, _) = tf.transformations.euler_from_quaternion(quaternion)

# Publish yaw angle to center_state port
pitch_state = round(pitch,3)

# Send the gripper state
if pitch_state >= -0.3:
    gd.oport["down_limit"].send(False)
else:
    gd.oport["down_limit"].send(True)

# Send the force_confirmation when the gripper is in the attachment position
if pitch_state >= -0.01:
    gd.oport["force_confirmation"].send(True)
    
# Control the attach movement based on the user input
if gd.shared.attach_gripper == True:
    gd.oport['attach_action'].send(50.0)
elif gd.shared.attach_gripper == False:
    gd.oport['attach_action'].send(-10.0)
else:
    pass