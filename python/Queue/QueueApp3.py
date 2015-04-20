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

from Queue2 import Queue2

q = Queue2()

while True :
    str([])
    print ("Array is %s" % q.array)
    a = input('%s please input >' % q.array)

    if a == 'end' :
        print("終了")
        break

    if a == 'push' :
        b = input('please number input >')
        q.enque(b)

    if a == 'pop' :
        try:
            print(q.deque())
        except:
            print("空のリストです")