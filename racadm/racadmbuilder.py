#! python3
# running racadm commands from OS

import os, subprocess
import racadmbuilderclasses as rclasses

##############################################################
# class racadprefix sets up the racadm local, or racadm remote#
# for the begining of the command string                     #
##############################################################
class racadmprefix:
    def __init__(self,*args):
        if len(args) < 1:
            self.rstring =  'racadm '
        else:
            self.rstring =  'racadm --nocertwarn -r ' + args[0] + ' -u ' + args[1] + ' -p' + args[2] + ' ' 

def getiDRACinfo():
# Todo table and other options to input addresses, username, user password
    ipaddress = '100.65.135.53'
    username = 'root'
    userpassword = 'Raidl@b'
    return ipaddress, username, userpassword

#Todo determine method for inputing multiple commands
#Todo create seperate files/objects(?) for each command

#setting up the beginning for remote racadm
ipaddress, username, userpassword = getiDRACinfo()
rprefix = rclasses.racadmprefix(ipaddress, username, userpassword)


##############################################################
# extracting the different tuples from the IPv4 address        
# fort of it xxx.xxx.xxx.xxx to extract the tuples I have
# slice it up as I maintain it as a string since the plan is
# to input via table or command line.
# each index variable is the location of '.' between tuples.
##############################################################
def iptuples(ipaddress):
    firstindex = ipaddress.index('.')
    temp = ipaddress[firstindex+1:]
    secondindex = temp.index('.') + firstindex + 1 # add the one for zero to one based.
    temp = ipaddress[secondindex+1:]
    thirdindex = temp.index('.') + secondindex + 1 # add the one for zero to one based.1
    tuple1 = ipaddress[0:firstindex]
    tuple2 = ipaddress[firstindex+1:secondindex]
    tuple3 = ipaddress[secondindex+1:thirdindex]
    tuple4 = ipaddress[thirdindex+1:]
    return tuple1, tuple2, tuple3, tuple4


###############################
# executing the racadm string
cmdstring = 'getniccfg'
ipaddress, username, userpassword = getiDRACinfo()
#rcmd = 'racadm --nocertwarn -r' + ipaddress + ' -u' + username + ' -p' + userpassword + ' ' + cmdstring
rcmd = rprefix.rstring + cmdstring
print(rcmd)
#os.system(rcmd)
rStream=subprocess.Popen(rcmd, stdout=subprocess.PIPE, shell=True, text=True)
communicateRes=rStream.communicate()
stdOutvalue, stdErrValue = communicateRes
print('\ncatpure_output stdout\n',stdOutvalue)

#finding DHCP Value
tmp=stdOutvalue.find('DHCP Enabled')
vDHCPEnabled=stdOutvalue[(tmp+23):(tmp+24)]
print(vDHCPEnabled)

#finding current IPAddress Value
tmp=stdOutvalue.find('IP Address           =')
vIPAddress=stdOutvalue[(tmp+23):(tmp+23+15)]
print(vIPAddress)

#finding current Gateway Value
tmp=stdOutvalue.find('Gateway              =')
vGateway=stdOutvalue[(tmp+23):(tmp+23+15)]
print(vGateway)


tuple1, tuple2, tuple3, tuple4 =  iptuples(ipaddress)

###############################
# executing the racadm string
cmdstring = 'setniccfg -s ' + ipaddress + '  ' + '255.255.255.0  ' + tuple1 +'.' + tuple2 + '.' + tuple3 + '.254'
ipaddress, username, userpassword = getiDRACinfo()
rcmd = rprefix.rstring + cmdstring
#rcmd = 'racadm --nocertwarn -r' + ipaddress + ' -u' + username + ' -p' + userpassword + ' ' + cmdstring
#print(rcmd)
#os.system(rcmd)



