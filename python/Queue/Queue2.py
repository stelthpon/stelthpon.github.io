#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Owner
#
# Created:     20/04/2015
# Copyright:   (c) Owner 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding: UTF-8

class Queue2 :
        array = []
        def enque(self, e) :
            self.array.append(e)
        def deque(self) :
            return self.array.pop(0)