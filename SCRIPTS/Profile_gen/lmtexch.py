# this script is used to limit the exchange between the ions channel and electrons channel;
qdelten=root['OUTPUTS']['ONETWO']['trpltout.nc']['qdelten']['data'][-1];		# electron-ion power exchange
pdelten=root['OUTPUTS']['ONETWO']['trpltout.nc']['pdelten']['data'][-1];		# integrated power exchange
# note the exchange term means the power from the ions channels that transfers to the electrons
exchup=root['SETTINGS']['PHYSICS']['lmtexch']
if max(abs(pdelten))>exchup*1.e6:
    fct=1.e6*exchup/max(abs(pdelten))
    ad2ion=pdelten*(1.-fct)/1.e6
    root['OUTPUTS']['Profile_gen']['input.profiles']['pow_i']=root['OUTPUTS']['Profile_gen']['input.profiles']['pow_i']+ad2ion
    root['OUTPUTS']['Profile_gen']['input.profiles']['pow_e']=root['OUTPUTS']['Profile_gen']['input.profiles']['pow_e']-ad2ion
