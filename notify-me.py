import sys
import subprocess as sub

def ParseSysArgv():
	args = sys.argv
	args.pop(0)

	return args

if __name__ == "__main__":
	#sub.call(["notify-send", sys.argv[1], sys.argv[2]])
	print (ParseSysArgv())