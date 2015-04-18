#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      USER
#
# Created:     18/04/2015
# Copyright:   (c) USER 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding: UTF-8

from Queue import Queue

q = Queue()

while True :
    a = input('please input >')

    if a == 'end' :
        break

    if a == 'push' :
        b = input('please number input >')
        q.push(b)

    if a == 'pop' :
        q.rev()
        print(q.pop())
        q.rev()