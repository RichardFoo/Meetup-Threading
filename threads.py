#!/usr/bin/env python3

"""
Module:         threads.py

Description:    Example script for multi-threading

Notes:          This script demonstrates very simple multi-threading using a set of
                class objects that operate independently / don't interact with each other.
                
                This example uses the thread library directly - some frameworks
                (e.g., Flask) may require using the gevent wrapper for threading instead.
                gevent is included below, but commented out.
                
                Not shown are semaphores, which should be used for thread-safe access of
                shared variables.

History:        24Sep2019 - initial version

Next Steps:     Add thread health-checking watchdog.
                Demonstrate semaphores for thread-safe variables.

Notices:        https://github.com/RichardFoo/threading
                Richard@Hornbaker.com
"""

#If using something like Flask, the gevent/greenlet wrapper may be needed for threads instead
# import gevent                                     #Asynchronous event engine
# import gevent.monkey
# gevent.monkey.patch_all()
# # **** Important - Monkey Patch must execute before loading other modules ****
# #https://github.com/gevent/gevent/issues/1016


import _thread as thread
import time

objList = []                                        #Objects (and their threads)
params = [                                          #Output strings and interval values
        ("111", 1),
        ("   222", 2),
        ("      333", 3),
        ("         444", 4),
        ("            555", 5)
    ]



class screenWriter():
    """
    This is a self-contained object that runs independently in its own thread.
    """

    def __init__(self, text, interval):
        """
        Take the setup parameters when the object is created, then automatically launch
        our own thread to run independently.
        """
        self.text = text
        self.interval = interval
        self.thread = thread.start_new_thread( self.doStuff, () )   #Launch a new thread natively
#         self.thread = gevent.spawn(self.doStuff)                    #Launch a new thread via gevent


    def doStuff( self ):
#         """
#         This is a stub method that posts a one-time message then calls the infinite loop.
#         """
#         print("[%f] %s thread started" % (time.time(), self.text))
#         self.runForever()
# 
# 
#     def runForever( self ):
        """
        This is the main loop for the object.  It runs indefinitely, printing a message
        to the console along with a timestamp, then it sleeps for the configured interval.
        Calling sleep() is the friendly way to relinquish control of the CPU, because it
        consumes almost no CPU.
        time.sleep() is close but not high-precision.  Some small adjustments are made to
        improve the precision of each loop's execution, just to show it can be done.
        time.sleep() seems to have higher precision for small values.
        """
        print("[%f] %s thread started" % (time.time(), self.text))

        adjust = 0                                  #Set initial values
        desiredWakeTime = time.time()

        while True:
            wakeTime = time.time()
            jitter = wakeTime                       #Calc the jitter
            jitter -= desiredWakeTime               #How much we missed the mark
            adjust += jitter                        #Fine-tune the sleep duration
            desiredWakeTime += self.interval        #When the next wakeup should happen

            print("[%f] %s" % (wakeTime, self.text))
#             print("[%f] Jitter = %f\tAdjust = %f" % (wakeTime, jitter, adjust))

            time.sleep(self.interval - adjust)      #Release CPU control



    #Create all the worker objects, and launch their threads
for (text, interval) in params:
    classObj = screenWriter(text, interval)
    objList.append(classObj)                        #Save a pointer so we can check health

while True:                                         #Keep the main thread alive
    time.sleep(1)

    #We can do other useful stuff here (like check health), but if we exit here then
    #all the threads will be terminated
    #To check thread health, scan the list of objects and fetch their classObj.thread pointers
