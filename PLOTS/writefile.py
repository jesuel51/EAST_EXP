# this script is used to write out output of this project in a stardard format
# before running this scrip, the script root['PLOTS'] ['cmp.py'] and root['PLOTS']['cmp_grad.py'] must be run.
# so that matlab can handle those files more convinently
# the rotation profile is not writen out
fileout=root['SETTINGS']['DEPENDENCIES']['fileout'] # the name of the fileout
# first write the raw data
raw=root['INPUTS']['ONETWO']['raw']
fid=open(fileout,'w')
# ne raw data, format : rho, ne, ne_errbar
namelist=raw['ne']['namelist']
n_raw=len(namelist['raw_data'])
line=str(n_raw)
fid.write(line)
fid.write('\n')
for k in range(n_raw):
    line=str(namelist['raw_rho'][k])+'    '+\
	 str(namelist['raw_data'][k])+'    '
    if namelist.has_key('raw_data_errbar'):
        line=line+str(namelist['raw_data_errbar'][k])
    else:
        line=line+'0'
    fid.write(line)
    fid.write('\n')
# Te raw data, format: rho, Te, Te_errbar
namelist=raw['Te']['namelist']
n_raw=len(namelist['raw_data'])
line=str(n_raw)
fid.write(line)
fid.write('\n')
for k in range(n_raw):
    line=str(namelist['raw_rho'][k])+'    '+\
         str(namelist['raw_data'][k])+'    '
    if namelist.has_key('raw_data_errbar'):
        line=line+str(namelist['raw_data_errbar'][k])
    else:
        line=line+'0'
    fid.write(line)
    fid.write('\n')
# Ti raw data, format: rho, Ti, Ti_errbar
namelist=raw['Ti']['namelist']
n_raw=len(namelist['raw_data'])
line=str(n_raw)
fid.write(line)
fid.write('\n')
for k in range(n_raw):
    line=str(namelist['raw_rho'][k])+'    '+\
         str(namelist['raw_data'][k])+'    '
    if namelist.has_key('raw_data_errbar'):
        line=line+str(namelist['raw_data_errbar'][k])
    else:
        line=line+'0'
    fid.write(line)
    fid.write('\n')
# fitted data, from input.profiles
inputpro=root['INPUTS']['TGYRO']['input.profiles']
n_exp=inputpro['N_EXP']
line=str(n_exp)
fid.write(line)
fid.write('\n')
for k in range(n_exp):
    line=str(inputpro['rho'][k])+'    '+str(inputpro['ne'][k])+'    '+str(inputpro['Te'][k])+'    '+str(inputpro['Ti_1'][k])
    fid.write(line)
    fid.write('\n')
# the profile data calculated by TGYRO
temp=root['SETTINGS']['TEMP']
n_sim=len(temp['rho'])
line=str(n_sim)
fid.write(line)
fid.write('\n')
for k in range(n_sim):
    line=str(temp['rho'][k])+'    '+str(temp['ne_sim'][k])+'    '+str(temp['Te_sim'][k])+'    '+str(temp['Ti_sim'][k])
    fid.write(line)
    fid.write('\n')
#fid.close()
# the gradient of experimental profile
for k in range(n_sim):
    line=str(temp['rho'][k])+'    '+str(temp['aLne_exp'][k])+'    '+str(temp['aLTe_exp'][k])+'    '+str(temp['aLTi_exp'][k])
    fid.write(line)
    fid.write('\n')
# the gradient of simulation profiles
for k in range(n_sim):
    line=str(temp['rho'][k])+'    '+str(temp['aLne_sim'][k])+'    '+str(temp['aLTe_sim'][k])+'    '+str(temp['aLTi_sim'][k])
    fid.write(line)
    fid.write('\n')
fid.close()
