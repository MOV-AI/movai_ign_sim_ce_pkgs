config_name = gd.params['configuration_name']

if config_name is not None:
    config = Configuration(config_name).get_value()
    gd.oport['parameters'].send(config)
else:
   logger.error("Could not load parameters, because no configuration name is available!")

gd.oport['exit'].send()