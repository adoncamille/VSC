import sys, argparse, getopt

print("Argments numer : {} : ".format(len(sys.argv)))
print("Argments List : {}".format(sys.argv))

try:
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-n","--name",help="Name of the Person")
    argParser.add_argument("-i", "--int", type=int, help="Age of the Person ")
    argParser.add_argument("-w", "--weight", type=int, help="Weight of the Person")
    argParser.add_argument("-s", "--size", type=int, help="Size of the Person")
    args = argParser.parse_args()
except argparse.ArgumentError or argparse.ArgumentTypeError:
    print("Option Error")
    sys.exit(2)
else:
    print("Others errors")

print("args = {}".format(args))
# print("{}".format(args.name))
# print("{}".format(args.int))
# print("{}".format(args.weight))
# print("{}".format(args.size))
