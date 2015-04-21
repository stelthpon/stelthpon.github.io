#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      USER
#
# Created:     17/04/2015
# Copyright:   (c) USER 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding: UTF-8

class Queue :
        def __init__(self) :
                self.__array = []
        def enque(self, e) :
                self.__array.append(e)
        def deque(self) :
            return self.__array.pop()
        def head(self) :
                return self.__array[0]
        def consoleOut(self) :
                print("[tail] > ", end="")
                for e in self.__array :
                        print(e, "", end="")
                print("< [head]", "", end="")
                print("(", len(self.__array), "elements", ")")