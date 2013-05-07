import pexpect

# Open up a connection to the alarm monitoring system
child = pexpect.spawn ('telnet 192.168.1.10 10000')
time.sleep(3)   # Remove this
child.sendline ('12341')
child.expect ('Ready to Arm')
