#! python3
# setting up racadm user with administrative priveledges.


import os, subprocess
import racadmbuilderclasses as rclasses


###############################
# executing the racadm string
def executeRacadmCommand(cmdstring):
    rprefix = rclasses.racadmprefix('remote')
    rcmd = rprefix + cmdstring
    print(rcmd)
    rStream=subprocess.Popen(rcmd, stdout=subprocess.PIPE, shell=True, text=True)
    communicateRes=rStream.communicate()
    stdOutvalue, stdErrValue = communicateRes
    print('\ncatpure_output stdout\n',stdOutvalue)
    return

###############################
# configuring users via RACADM
def processUserCommands(vIndex, *args):
    print('processUserCommands',vIndex, args)
    if vIndex <= 1:
        print(vIndex,'user Index <=1')
        return
    else:
        vIndex = str(vIndex)
    if len(args) <= 0:
        ###############################
        # executing the racadm get
        rprefix = rclasses.racadmprefix('remote')
        cmdstring = 'get idrac.Users.' + vIndex
        executeRacadmCommand(cmdstring)
    else:
        for element in args:
            print('element',element)
            ###############################
            # executing the racadm set
            rprefix = rclasses.racadmprefix('remote')
            cmdstring = 'set iDRAC.Users.' + vIndex + '.' + element
            executeRacadmCommand(cmdstring)
    print('processUserCommands')
    return

#processUserCommands(2)
#processUserCommands(3)
#processUserCommands(4)
#processUserCommands(0)
#processUserCommands(1)
#processUserCommands(-1)


###############################
# configuring admin users via RACADM
#TODO where do these come from user input??
vIndex = '3'
vRoot2List = ['UserName root2', 'password PCIeauto1234', 'IpmiSerialPrivilege 4', 'IpmiLanPrivilege 4', 'Privilege 0x1ff', 'SolEnable Enabled', 'enable 1']
print(vRoot2List)
for element in vRoot2List:
    print(element)
    processUserCommands(3,element)
