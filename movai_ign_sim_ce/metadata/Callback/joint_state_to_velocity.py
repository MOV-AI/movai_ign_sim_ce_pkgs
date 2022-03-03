# Check if the Joint is in the msg.
if gd.params['joint_name'] in msg.name:
    # Get the index of the Joint in the msg and the speed of this joint.
    joint_index = msg.name.index(gd.params['joint_name'])
    joint_speed = msg.velocity[joint_index]
    
    # Create the message
    speed_msg = Int32()
    if gd.params['rpm_type']:
        # Convert from rad/s to RPM
        speed_msg.data = int(joint_speed / 0.10472)
    else:
        # Convert from m/s to mm/s
        speed_msg.data = int(joint_speed * 1000)
    gd.oport['joint_speed'].send(speed_msg)