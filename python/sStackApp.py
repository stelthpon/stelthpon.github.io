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

from sStack import Queue

q = Queue()
q.push(1)
q.push(3)
q.push(9)
q.push(1)
q.push(8)
q.rev()
print(q.pop())
print(q.pop())
q.rev()
q.push(0)
q.rev()
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
q.rev()