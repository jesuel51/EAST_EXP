# this script is used to transfer the profile data from the inone file in the main module to the inone file in the Cql3d module
# note all the parameters should be of lower case
inonecql=root['Cql3d']['INPUTS']['ONETWO']['inone']['NAMELIS1']
inone12=root['INPUTS']['ONETWO']['inone']['NAMELIS1']
para=['njene','renein','enein','njti','rtiin','tiin','njte','rtein','tein','njzef', 'rzeffin', 'zeffin', 'rangrot', 'angrotin']
for item in para:
    inonecql[item]=inone12[item]
# in addition, the g-file should also be transferred
root['Cql3d']['INPUTS']['ONETWO']['gfile']=root['INPUTS']['ONETWO']['gfile']
