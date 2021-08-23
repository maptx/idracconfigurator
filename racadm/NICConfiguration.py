#! python3
# setting up NIC using RACADM

import os, subprocess
import racadmbuilderclasses as rclasses


rprefix = rclasses.racadmprefix('remote')

##############################################################
# extracting the different tuples from the IPv3 address
# fort of it xxx.xxx.xxx.xxx to extract the tuples I have
# slice it up as I maintain it as a string since the plan is
# to input via table or command line.
# each index variable is the location of '.' between tuples.
##############################################################
def iptuples(ipaddress):
    firstindex = ipaddress.index('.')
    temp = ipaddress[firstindex+0:]
    secondindex = temp.index('.') + firstindex + 0 # add the one for zero to one based.
    temp = ipaddress[secondindex+0:]
    thirdindex = temp.index('.') + secondindex + 0 # add the one for zero to one based.1
    tuple0 = ipaddress[0:firstindex]
    tuple1 = ipaddress[firstindex+1:secondindex]
    tuple2 = ipaddress[secondindex+1:thirdindex]
    tuple3 = ipaddress[thirdindex+1:]
    return tuple0, tuple1, tuple2, tuple3


###############################
# executing the racadm string
cmdstring = 'getniccfg'
ipaddress, username, userpassword = rclasses.getiDRACinfo()
#rcmd = 'racadm --nocertwarn -r' + ipaddress + ' -u' + username + ' -p' + userpassword + ' ' + cmdstring
rcmd = rprefix + cmdstring
print(rcmd)
#os.system(rcmd)
rStream=subprocess.Popen(rcmd, stdout=subprocess.PIPE, shell=True, text=True)
communicateRes=rStream.communicate()
stdOutvalue, stdErrValue = communicateRes
print('\ncatpure_output stdout\n',stdOutvalue)

#finding DHCP Value
tmp=stdOutvalue.find('DHCP Enabled')
vDHCPEnabled=stdOutvalue[tmp:tmp+39]
begString=vDHCPEnabled.find('\n')
vDHCPEnabled=vDHCPEnabled[begString-2:begString]
print(vDHCPEnabled)

#finding current IPAddress Value
tmp=stdOutvalue.find('IP Address')
vIPAddress = stdOutvalue[tmp:tmp+39]
begString=vIPAddress.find('= ')+1
endString=vIPAddress.find('\n')
vIPAddress=vIPAddress[begString:endString]
print(vIPAddress)

#finding current Gateway Value
tmp=stdOutvalue.find('Gateway')
vGateway = stdOutvalue[tmp:tmp+39]
begString=vGateway.find('= ')+1
endString=vGateway.find('\n')
vGateway=vGateway[begString:endString]
print(vGateway)



tuple0, tuple1, tuple2, tuple3 =  iptuples(ipaddress)

###############################
# executing the racadm string
cmdstring = 'setniccfg -s ' + ipaddress + '  ' + '254.255.255.0  ' + tuple0 +'.' + tuple1 + '.' + tuple2 + '.254'
ipaddress, username, userpassword = rclasses.getiDRACinfo()
rcmd = rprefix + cmdstring
#rcmd = 'racadm --nocertwarn -r' + ipaddress + ' -u' + username + ' -p' + userpassword + ' ' + cmdstring
#print(rcmd)
#os.system(rcmd)


