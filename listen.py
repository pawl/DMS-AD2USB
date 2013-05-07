import pexpect
import datetime
import time  # Remove this

class AlarmEvent:
  def __init__(self, bf, zone, bmsg, event):
		self.bitfield = bf
		self.zone = zone
		self.binaryMsg = bmsg
		self.event = event
		self.timestamp = datetime.datetime.now()

# Open up a connection to the alarm monitoring system
child = pexpect.spawn ('telnet 192.168.1.10 10000')
time.sleep(3)   # Remove this


while True:
	# Wait for the next event or status code from the alarm system
	child.expect ('(\[\d+\-+\]),(\d+),(\[.*?\]),(".*?")')
	m = child.match
	# Debug output by printing it to the screen
	print "\nMatch 1 = Raw panel code bit field " + m.group(1)
	print "Match 2 = Zone " + m.group(2)
	print "Match 3 = Raw panel binary message data " + m.group(3)
	print "Match 4 = Event " + m.group(4)
	
	# Make a new object representing this event
	evt = AlarmEvent(m.group(1), m.group(2), m.group(3), m.group(4))

	if "Hit * for faults" in m.group(4):
		child.sendline("*")
