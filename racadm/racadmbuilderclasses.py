#! python3
# running racadm commands from OS
# classes to support bulding the commands

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

