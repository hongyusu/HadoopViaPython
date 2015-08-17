#!/usr/bin/env python
import sys
def main():
  curword = None
  curcount = 0
  for line in sys.stdin:
    word,count=line.strip().split('\t')
    if curword == None:
      curword = word
      curcount = 1
      continue
    if curword == word:
      curword = word
      curcount += 1
    else:
      print "%s\t%d" %(curword,curcount)
      curword = word
      curcount = eval(count)
  print "%s\t%d" %(curword,curcount)
if __name__=='__main__':
  main()