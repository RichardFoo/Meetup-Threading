# Meetup-Threading

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