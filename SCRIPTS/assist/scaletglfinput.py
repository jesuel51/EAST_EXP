# this script is used to scale the parameters in input.tglf,especially the gradients
# execulate the TGYRO
inputs=[(root['INPUTS']['TGYRO']['input.profiles'],'input.profiles'),
        (root['INPUTS']['TGYRO']['input.profiles.geo'],'input.profiles.geo'),
        (root['INPUTS']['TGYRO']['input.tgyro'],'input.tgyro'),
        (root['INPUTS']['TGYRO']['jobtgyro.pbs'],'jobtgyro.pbs'),
        (root['INPUTS']['TGYRO']['monitePBStgyro.sh'],'monitePBStgyro.sh')
        ]
for k in range(1,13):
    inputs.append((root['INPUTS']['TGYRO']['inputtglf']['input.tglf'+str(k)],'input.tglf'+str(k)))
# run TGYRO with 0 iteration to give input for TGLF
Iterations=root['INPUTS']['TGYRO']['input.tgyro']['TGYRO_RELAX_ITERATIONS']
root['INPUTS']['TGYRO']['input.tgyro']['TGYRO_RELAX_ITERATIONS']=0
##----------------------
### output
##----------------------
p_tgyro=root['SETTINGS']['PHYSICS']['p_tgyro']
outputs=['out.tgyro.gyrobohm']
for k in range(1,p_tgyro+1):
    root['INPUTS']['TGYRO']['input.tgyro']['DIR']['TGLF'+str(k)]=1
    outputs.append('TGLF'+str(k)+'/out.tglf.localdump')
#print(outputs)    
##executable = str(root['SETTINGS']['SETUP']['executable'])
#executable ='chmod 777 monitePBStgyro.sh; ./monitePBStgyro.sh'
executable ='chmod 777 monitePBStgyro.sh ; ./monitePBStgyro.sh ;'
executable =executable + 'pbsMonitor -cn 12 -exe tgyro_cfetr -e . -n 12'

ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable)
root['INPUTS']['TGYRO']['input.tgyro']['TGYRO_RELAX_ITERATIONS']=Iterations
#-----------------------
# load the results for TGYRO to map the plasma background to the TGLF
#-----------------------
root['OUTPUTS']['TGYRO']['out.tgyro.gyrobohm']=OMFITasciitable('out.tgyro.gyrobohm')
for k in range(1,p_tgyro+1):
#    print(k)
    root['OUTPUTS']['TGYRO'][k]=OMFITgaCode(outputs[k])
# get the parameters which is required to be scaled
# determine whether to do some scale to the out.tglf.localdump
if root['SETTINGS']['SETUP'].has_key('TGLFinputscale'):
    for key in root['SETTINGS']['SETUP']['TGLFinputscale']:
        if key in root['OUTPUTS']['TGYRO'][1].keys():
            for k in range(1,p_tgyro+1):
                print(key)
#                root['OUTPUTS']['TGYRO'][k][key]=root['OUTPUTS']['TGYRO'][k][key]*root['SETTINGS']['SETUP']['TGLFinputscale'][key]
#                root['INPUTS']['TGYRO']['inputtglf']['input.tglf'+str(k)][key]=root['OUTPUTS']['TGYRO'][k][key]
                root['INPUTS']['TGYRO']['inputtglf']['input.tglf'+str(k)][key]=root['OUTPUTS']['TGYRO'][k][key]*root['SETTINGS']['SETUP']['TGLFinputscale'][key]
#root['OUTPUTS']['TGYRO']=OMFITtree()
# give back the iteration number to input.tgyro
root['INPUTS']['TGYRO']['input.tgyro']['TGYRO_RELAX_ITERATIONS']=Iterations
