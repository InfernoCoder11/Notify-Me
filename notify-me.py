import sys
import subprocess as sub

if __name__ == "__main__":
	sub.call("notify-send {}".format(sys.argv[1]).split())