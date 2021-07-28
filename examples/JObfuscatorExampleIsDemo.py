#!/usr/bin/env python

###############################################################################
#
# JObfuscator WebApi interface usage example.
#
# In this example we will verify our activation key status.
#
# Version        : v1.01
# Language       : Python
# Author         : Bartosz Wójcik
# Web page       : https://www.pelock.com
#
###############################################################################

#
# include JObfuscator module
#
from jobfuscator import JObfuscator

#
# if you don't want to use Python module, you can import directly from the file
#
#from pelock.jobfuscator import JObfuscator

#
# create JObfuscator class instance (we are using our activation key)
#
myJObfuscator = JObfuscator("ABCD-ABCD-ABCD-ABCD")

#
# login to the service
#
result = myJObfuscator.login()

#
# result[] array holds the information about the license
#
# result["demo"]          - is it a demo mode (invalid or empty activation key was used)
# result["credits_left"]  - usage credits left after this operation
# result["credits_total"] - total number of credits for this activation code
# result["string_limit"]  - max. source code size allowed (it's 1500 bytes for demo mode)
#
if result:

    print(f'Demo version status - {"True" if result["demo"] else "False"}')
    print(f'Usage credits left - {result["credits_left"]}')
    print(f'Total usage credits - {result["credits_total"]}')
    print(f'Max. source code size - {result["string_limit"]}')

else:
    print("Something unexpected happen while trying to login to the service.")
