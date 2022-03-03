value = std_msgs.msg.Bool()
value.data = gd.params['value']
gd.oport['std_msgs_publisher'].send(value)
if count > 10:
    gd.oport['exit'].send()