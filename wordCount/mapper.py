#!/usr/bin/env python
import sys
def main():
  for line in sys.stdin:
    words = line.strip().split()
    for word in words:
      print "%s\t1" % word
if __name__ == "__main__":
  main()