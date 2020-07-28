#!/usr/bin/env python3

# Wrapper for Arduino core / others that can call esptool.py possibly multiple times
# Adds pyserial to sys.path automatically based on the first argument passed to the script

import sys
import os
import tempfile

sys.argv.pop(0) # Remove executable name

toolspath = os.path.dirname(sys.argv.pop(0)).replace('\\', '/') # CWD in UNIX format

try:
    sys.path.insert(0, toolspath + "/tools/pyserial") # Add pyserial dir to search path
    sys.path.insert(0, toolspath + "/tools/esptool") # Add esptool dir to search path
    import esptool # If this fails, we can't continue and will bomb below
except:
    sys.stderr.write("pyserial or esptool directories not found next to this upload.py tool.\n")
    sys.exit(1)

cmdline = []

cmdline = cmdline + sys.argv

esptool.main(cmdline)
