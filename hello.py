import ptvsd

# Allow other computers to attach to ptvsd at this IP address and port.
ptvsd.enable_attach(address=('10.0.0.27', 22), redirect_output=True)

# Pause the program until a remote debugger is attached
ptvsd.wait_for_attach()

print('hello')
