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
        array = []
        def push(self, e) :
            self.array.append(e)
        def pop(self) :
            return self.array.pop()
        def rev(self) :
            return self.array.reverse()