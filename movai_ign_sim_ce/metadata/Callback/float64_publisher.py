value = std_msgs.msg.Float64()
value.data = gd.params['value']
gd.oport['std_msgs_publisher'].send(value)
if count > 10:
    gd.oport['exit'].send()