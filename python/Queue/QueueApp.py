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

from Queue import Queue

q = Queue()
q.enque(0)
q.enque(1)
q.enque(2)
q.enque(3)
q.rev()
print(q.deque())
print(q.deque())
q.rev()
q.enque(10)
q.rev()
print(q.deque())
print(q.deque())
print(q.deque())
q.rev()