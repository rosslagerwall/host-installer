#!/usr/bin/env python
###
# XEN CLEAN INSTALLER
# Main script
#
# written by Mark Nijmeijer
# Copyright XenSource Inc. 2006

from snack import *
import commands
import sys
import os
import p2v

screen = None

def run_command(cmd):
    rc, out = commands.getstatusoutput(cmd)
    return (rc, out)

def main():
    global screen
    
    #disable all kernel printing
    run_command("echo 1 > /proc/sys/kernel/printk")
    
    try:
        
        while True:
            screen = SnackScreen()
            screen.drawRootText(0, 0, "Welcome to the Xen Enterprise Installer")
    
            entries = [ 
                    ' * XenEnterprise Install (clean install)',
#                    ' * P2V (existing OS install)',
                    ' * Reboot machine'
                     ]
            (button, entry) = ListboxChoiceWindow(screen,
                            "Make a choice",
                            """Select the install you want to perform:""",
                            entries,
                            ['Ok', 'Exit'], width=60)
            if button == 'ok' or button == None:
                if entry == 0:
                     rc = os.system("/opt/xensource/clean-installer/clean-installer")
                     if rc == 0: 
                         os.system("reboot")
##                elif entry == 1:
 ##                   os.system("/opt/xensource/clean-installer/p2v.py")
                elif entry == 1:
                    button = ButtonChoiceWindow(screen,
                           "Confirm",
                           """Do you really want to reboot?""",
                           ['Ok', 'Cancel'], width=50)
                    if button == 'ok':
                        screen.finish()
                        os.system("eject")
                        os.system("reboot")
            else:
                screen.finish()
                sys.exit(0)
    except Exception, e:
        screen.finish()
        raise
        
if __name__ == "__main__":
    main()
    
