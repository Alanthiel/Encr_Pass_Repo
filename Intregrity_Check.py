import json
import os
try:
    import curl
except ImportError:
    pack_req = input("\nPackage Dependency <PyCurl> Curl not met, Install Package? (y)?")
    if pack_req is not 'y':
        print("Exiting...")
    ping = os.system("pip install pycurl")
    if not ping:
        print("Unable to install PyCurl, Exiting....")
        exit()
