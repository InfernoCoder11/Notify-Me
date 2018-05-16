import subprocess as sub
import argparse
import time
import threading

def Notify(heading, message, minutes = 0):
	seconds = minutes*60
	time.sleep (seconds)
	sub.call(["notify-send", args.heading, args.message])

def AltNotification(heading, message, minutes = 0):
	from PyQt5 import Qt
	import sys
	seconds = minutes*60
	app = Qt.QApplication(sys.argv)
	systemtray_icon = Qt.QSystemTrayIcon(app)
	systemtray_icon.show()
	time.sleep(seconds)
	systemtray_icon.showMessage(heading, message)

def ParserInit ():
	parser = argparse.ArgumentParser()
	parser.add_argument("heading", help = "Heading of the notification", type = str)
	parser.add_argument("message", help = "Message body of the notification", type = str)
	parser.add_argument("minutes", help = "Notify after how many minutes", type = float)
	parser.add_argument("-a", "--alternate", help = "Use if you wnat to use PyQt notification", action = "store_true")
	args = parser.parse_args()

	return args

if __name__ == "__main__":
	args = ParserInit()
	if args.alternate:
		AltNotification(args.heading, args.message, args.minutes, )

	else:
		Thread = threading.Thread(target = Notify, args = (args.heading, args.message, args.minutes, ))
		Thread.start()