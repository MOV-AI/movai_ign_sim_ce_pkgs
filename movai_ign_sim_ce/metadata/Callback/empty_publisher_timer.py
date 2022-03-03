# This callback is associated with the empty_publisher node.

# publish the empty messge 10 times and exit
gd.oport['std_msgs_publisher'].send(Empty())
if count > 10:
    gd.oport['exit'].send()
