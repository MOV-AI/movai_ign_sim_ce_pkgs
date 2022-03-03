# publish all frames from the robot SDF
if gd.params['generate_tfs']:
    base_link_frame = str(gd.params['base_link_frame'])
    child_frame = msg.child_frame_id.split('/')
    if len(child_frame) > 1:
        if child_frame[1] != base_link_frame:
            # instanciate and populate pose message
            transform_msg = Pose()
            transform_msg.position.x = msg.transform.translation.x
            transform_msg.position.y = msg.transform.translation.y
            transform_msg.position.z = msg.transform.translation.z
            transform_msg.orientation = msg.transform.rotation

            # publish tf
            gd.oport['tf'].send(transform_msg, child=child_frame[1], parent=base_link_frame)