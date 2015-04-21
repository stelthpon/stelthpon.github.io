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

while True :
    a = input('please input >' )

    if a == 'end' :
        print("end")
        break

    if a == 'push' :
        b = input('please number input >')
        q.enque(b)

    if a == 'pop' :
        try:
            print(q.deque())
        except:
            print("empty")

    if a == 'head' :
        try:
            print(q.head())
        except:
            print("empty")

    q.consoleOut()