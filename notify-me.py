import sys
import subprocess as sub
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("heading", help = "Heading of the notification", type = str)
parser.add_argument("message", help = "Message body of the notification", type = str)
parser.parse_args()

if __name__ == "__main__":
	#sub.call(["notify-send", sys.argv[1], sys.argv[2]])
	pass