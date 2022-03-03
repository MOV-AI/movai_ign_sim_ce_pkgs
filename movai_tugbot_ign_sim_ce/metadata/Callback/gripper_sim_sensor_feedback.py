cart_distance = msg.ranges[1]
if cart_distance <= gd.params['cart_gripper_distance']:
    gd.oport["gripper_inductive_sensor"].send(True)
else:
    gd.oport["gripper_inductive_sensor"].send(False)