#setup the running directly
case = root['SETTINGS']['SETUP']['case']
root['SETTINGS']['REMOTE_SETUP']['workDir'] = '/scratch/xiangjian/OMFIT/runs/EAST_EXP/'+case
# determine whether to run cql3d to update the LH powers
if root['SETTINGS']['PHYSICS']['iruncql3d']==1:
    if 'Cql3d' not in root.keys():
        root['Cql3d']=OMFITmodule('/scratch/xiangjian/OMFIT-source/modules/Cql3d/OMFITsave.txt')
    root['SCRIPTS']['assist']['prepdatforcql3d.py'].run()
    root['Cql3d']['SETTINGS']['SETUP']['case']=root['SETTINGS']['SETUP']['case']
    root['Cql3d']['SCRIPTS']['manage']['proctrl.py'].run()
    root['SCRIPTS']['assist']['backdatfromcql3d.py'].run()
# determine which g-file to choose,
# 0, g-file provided by experimental equilibrium reconstruction
# 1, g-file .. by equilibrium calculation based on ONETWO output
root['SCRIPTS']['assist']['scalepro.py'].run()
igfile=root['SETTINGS']['SETUP']['igfile']
root['SCRIPTS']['ONETWO']['run12.py'].run()
root['INPUTS']['EFIT']['g0file']=root['OUTPUTS']['ONETWO']['gfile']
root['INPUTS']['Profile_gen']['statefile.nc']=root['OUTPUTS']['ONETWO']['statefile.nc']
#root['SCRIPTS']['EFIT']['runEFIT.py'].run()
if igfile==0:
    root['INPUTS']['Profile_gen']['gfile']=root['INPUTS']['ONETWO']['gfile']
else:
    root['SCRIPTS']['EFIT']['runEFIT.py'].run()
    root['INPUTS']['Profile_gen']['gfile']=root['OUTPUTS']['EFIT']['gfile']
root['SCRIPTS']['Profile_gen']['runpg.py'].run()
#root['SCRIPTS']['Profile_gen']['lmtexch.py'].run()
root['INPUTS']['TGYRO']['input.profiles']=root['OUTPUTS']['Profile_gen']['input.profiles']
root['INPUTS']['TGYRO']['input.profiles.geo']=root['OUTPUTS']['Profile_gen']['input.profiles.geo']
root['SCRIPTS']['TGYRO']['runtgyro.py'].run()
