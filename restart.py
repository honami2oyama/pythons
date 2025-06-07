print ("Restarting...")

import os
import sys

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

restart_program()
