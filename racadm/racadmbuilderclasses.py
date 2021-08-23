#! python3
# running racadm commands from OS
# classes to support bulding the commands

##############################################################
# class racadprefix sets up the racadm local, or racadm remote#
# for the begining of the command string                     #
##############################################################
#class racadmprefix:
#    def __init__(self,*args):
#        if len(args) < 1:
#            self.rstring =  'racadm '
#        else:
#            self.rstring =  'racadm --nocertwarn -r ' + args[0] + ' -u ' + args[1] + ' -p' + args[2] + ' '


##############################################################
# function getiDRACinfo initially just uses hardcoded        #
# information for the information                            #
# looking at will likely use a pointer to a file to get the  #
# after I figure out how that part                           #
##############################################################

def getiDRACinfo():
# Todo table and other options to input addresses, username, user password
    ipaddress = '100.65.135.53'
    username = 'root'
    userpassword = 'Raidl@b'
    return ipaddress, username, userpassword


##############################################################
# function racadprefix sets up the racadm local, or remote   #
# for the beginning of the command string                    #
# looking at the variable being nothing for local,           #
# possible remote for remote or pointer to a file            #
##############################################################
def racadmprefix(*args):
        if len(args) < 1:
            rstring =  'racadm '
        else:
            ipaddress, username, userpassword = getiDRACinfo()
            rstring =  'racadm --nocertwarn -r ' + ipaddress + ' -u ' + username + ' -p' + userpassword + ' '
        return(rstring)


