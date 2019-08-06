

import os

TEMP_PATH='/root/Walkman/scratch/'


def createKickstartISO_ESXi67(ISOPath, KSPath):
    
    # Create a temp directory and mount the input ISO to that path
    mountpath = TEMP_PATH + 'abz121'
    cmd = 'mkdir ' + mountpath
    os.system(cmd)
    cmd = 'mount -o loop ' + ISOPath + ' ' + mountpath
    os.system(cmd)


if __name__ == '__main__':


    print('Main 0')
    createKickstartISO_ESXi67('/root/ISOs/VMware-ESXi-6.7.0-Update1-10302608-HPE-Gen9plus-670.U1.10.3.5.12-Oct2018.iso', '/root/Walkman/kickstarts/esxi67/ksvcf.cfg')


