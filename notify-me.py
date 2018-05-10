import sys
import subprocess as sub
import argparse
import time
import threading

def Notify(heading, message, minutes = 0):
	seconds = minutes*60
	time.sleep (seconds)
	sub.call(["notify-send", args.heading, args.message])

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("heading", help = "Heading of the notification", type = str)
	parser.add_argument("message", help = "Message body of the notification", type = str)
	parser.add_argument("-m", "--minutes", help = "Notify after how many minutes", type = float)
	args = parser.parse_args()
	Threads = []
	Thread = threading.Thread(target = Notify, args = (args.heading, args.message, args.minutes, ))
	Threads.append (Thread)
	Thread.start()