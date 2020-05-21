# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:47:41 2020

@author: Silverxenfx
"""

import time
class StopWatch():
    def __init__(self):
        self.__StartTime=time.time()
    def start(self):
        self.__StartTime=time.time()
    def stop(self):
        self.__EndTime=time.time()
    def Start(self):
      return int(self.__StartTime)
    def EndTime(self):
      return int(self.__EndTime)
    def getElapsedTime(self):
        return int(1000*(self.__EndTime-self.__StartTime))


def main():
    size=100
    stopwatch=StopWatch()

    time.sleep(size)

    stopwatch.stop()
    print("Start Time:",stopwatch.Start())
    print("End Time:",stopwatch.EndTime())
    print("loop time",stopwatch.getElapsedTime(),"miliseconds")
main()
