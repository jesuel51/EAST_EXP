#-*-Python-*-
# Created by xiangjian at 2015/9/10 15:02
# here, we will run ONETWO in conventional time-dependent evolution mode to get the beam-driven current and heating profile

# For the input files
inputs=[(root['INPUTS']['ONETWO']['inone'],'inone'),
        (root['INPUTS']['ONETWO']['gfile'],'gfile'),
        (root['INPUTS']['ONETWO']['gafit.in'],'gafit.in'),
        (root['INPUTS']['ONETWO']['toray.in'],'toray.in'),
        (root['INPUTS']['ONETWO']['job12.pbs'],'job12.pbs'),
        (root['INPUTS']['ONETWO']['monitePBS12.sh'],'monitePBS12.sh')
	]
##----------------------
### output
##----------------------
outputs=['statefile.nc','trpltout.nc','outone','summary','toray_6.000000E+00_2_.nc']
#if root['SETTINGS']['PHYSICS']['iSS']==0:
#    gfile='g0.06010'
#else:
#    gfile='g0.99999'
if root['SETTINGS']['PHYSICS']['iSS']==1:
    root['INPUTS']['ONETWO']['inone']['NAMELIS1']['bctime'][1]=1.e6
    root['INPUTS']['ONETWO']['inone']['NAMELIS1']['timmax']=1.e6
    root['INPUTS']['ONETWO']['inone']['NAMELIS1']['dtmax']=1.e6
    root['INPUTS']['ONETWO']['inone']['NAMELIS1']['dt']=1.e6
    root['INPUTS']['ONETWO']['inone']['NAMELIS1']['dtmin']=1.e6
    root['INPUTS']['ONETWO']['inone']['NAMELIS1']['steady_state']=0.
    root['INPUTS']['ONETWO']['inone']['NAMELIS1']['diffeq_methd']=2
    root['INPUTS']['ONETWO']['inone']['NAMELIS1']['non_lin_method']=2
    gfile='g0.99999'
else:
    root['INPUTS']['ONETWO']['inone']['NAMELIS1']['bctime'][1]=6.001
    root['INPUTS']['ONETWO']['inone']['NAMELIS1']['timmax']=6.001
    root['INPUTS']['ONETWO']['inone']['NAMELIS1']['dtmax']=0.001
    root['INPUTS']['ONETWO']['inone']['NAMELIS1']['dt']=0.001
    root['INPUTS']['ONETWO']['inone']['NAMELIS1']['dtmin']=1.e-6
    root['INPUTS']['ONETWO']['inone']['NAMELIS1']['steady_state']=1.
    gfile='g0.06001'
outputs.append(gfile);
#executable = 'chmod 777 monitePBS12.sh ; ./monitePBS12.sh'
executable = 'pbsMonitor -jq parallel11 -jn 2 -cn 4 -exe onetwo_cfetr -np 8 '
#-----------------------
# Execute ONETWO
#-----------------------
ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable)
#-----------------------
# load the results
#-----------------------
#root['OUTPUTS']['ONETWO']['iterdb']=OMFITascii('iterdb')
root['OUTPUTS']['ONETWO']['statefile.nc']=OMFITnc('statefile.nc')
root['OUTPUTS']['ONETWO']['toray.nc']=OMFITnc('toray_6.000000E+00_2_.nc')
root['OUTPUTS']['ONETWO']['trpltout.nc']=OMFITnc('trpltout.nc')
root['OUTPUTS']['ONETWO']['gfile']=OMFITeqdsk(gfile)
root['OUTPUTS']['ONETWO']['outone']=OMFIToutone('outone')
root['OUTPUTS']['ONETWO']['summary']=OMFIToutone('summary')
