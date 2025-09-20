#!/usr/bin/env python3
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--interface", required=True)
parser.add_argument("-m", "--mac", required=True)
args = parser.parse_args()

subprocess.call(["ifconfig", args.interface, "down"])
subprocess.call(["ifconfig", args.interface, "hw", "ether", args.mac])
subprocess.call(["ifconfig", args.interface, "up"])
