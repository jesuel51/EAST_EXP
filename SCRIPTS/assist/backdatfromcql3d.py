# this script is used to give back the LH H&CD profile, outputed by cql3d to inone
inonecql=root['Cql3d']['OUTPUTS']['CQL3D']['inone']['NAMELIS2']
inone12=root['INPUTS']['ONETWO']['inone']['NAMELIS2']
precur='extcurrf';
preqe='extqerf'
paracur=['(2)','_amps(2)','_id(2)','_nj(2)','_rho(1,2)','_curr(1,2)']
paraqe=['(2)','_watts(2)','_id(2)','_nj(2)','_rho(1,2)','_qe(1,2)']
for item in paracur:
    inone12[precur+item]=inonecql[precur+item]
for item in paraqe:
    inone12[preqe+item]=inonecql[preqe+item]
