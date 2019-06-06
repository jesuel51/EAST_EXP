#-*-Python-*-
# Created by xiangjian at 2015/05/04 16:20

#-*-Python-*-
# Created by xiangjian at 2015/05/03 15:02
# run the scaletglfinput.py , if needed to change some parameters, such as the gradients,etc
#root['SCRIPTS']['assist']['scaletglfinput.py'].run()
# prepare the input.tglf
p_tgyro=len(root['INPUTS']['TGYRO']['input.tgyro']['DIR'])
#root['INPUTS']['TGYRO']['input.tgyro']['inputtglf']=OMFITtree()
#inputtglf=root['INPUTS']['TGYRO']['input.tgyro']['inputtglf']
#for k in range(1,p_tgyro+1):
#    inputtglf['input.tglf'+str(k)]=OMFITnamelist()

# What are the input files

inputs=[(root['INPUTS']['TGYRO']['input.profiles'],'input.profiles'),
#        (root['INPUTS']['TGYRO']['input.profiles.geo'],'input.profiles.geo'),
        (root['INPUTS']['TGYRO']['input.tgyro'],'input.tgyro'),
        (root['INPUTS']['TGYRO']['jobtgyro.pbs'],'jobtgyro.pbs'),
        (root['INPUTS']['TGYRO']['monitePBStgyro.sh'],'monitePBStgyro.sh')
	]
inputtgyro=root['INPUTS']['TGYRO']
if inputtgyro.has_key('input.profiles.geo'):
     inputs.append(inputtgyro['input.profiles.geo'])
for k in range(1,p_tgyro+1):
    inputs.append((root['INPUTS']['TGYRO']['inputtglf']['input.tglf'+str(k)],'input.tglf'+str(k)))
##----------------------
### output
##----------------------
outputs=['out.tgyro.alpha',
         'out.tgyro.flux_e','out.tgyro.flux_i1','out.tgyro.flux_i2',
#'out.tgyro.flux_target',
         'out.tgyro.evo_ne','out.tgyro.evo_te','out.tgyro.evo_ti','out.tgyro.evo_er',
         'out.tgyro.evo_n1','out.tgyro.evo_n2',
         'out.tgyro.power_e','out.tgyro.power_i',
         'out.tgyro.profile','out.tgyro.profile_e','out.tgyro.profile_i1','out.tgyro.profile_i2',
#	 'out.tgyro.mflux_e','out.tgyro.mflux_i','out.tgyro.mflux_i2',
	 'out.tgyro.gyrobohm','out.tgyro.gradient',
	 'out.tgyro.geometry.1','out.tgyro.nu_rho',
         'out.tgyro.residual','out.tgyro.control',
	 'out.tgyro.geometry.2','out.tgyro.run',
	 'input.profiles.gen','input.tgyro.gen'
         ]
if root['INPUTS']['TGYRO']['input.tgyro']['LOC_N_ION'] == 3:
    outputs.append('out.tgyro.flux_i3')
    outputs.append('out.tgyro.profile3')
    outputs.append('out.tgyro.mflux_i3')
    outputs.append('out.tgyro.evo_n3')
for k in range(1,p_tgyro+1):
#    root['INPUTS']['TGYRO']['input.tgyro']['DIR']['TGLF'+str(k)]=int(root['SETTINGS']['SETUP']['num_nodes']*root['SETTINGS']['SETUP']['num_cores']/p_tgyro)
    outputs.append('TGLF'+str(k)+'/out.tglf.localdump')
for k in range(1,p_tgyro+1):
    outputs.append('TGLF'+str(k)+'/out.neo.localdump')
executable ='chmod 777 monitePBStgyro.sh ; ./monitePBStgyro.sh;'
#executable =executable + 'pbsMonitor -jq parallel11 -jn 2 -cn 6 -exe tgyro_cfetr -e . -n 12'
#executable =executable + 'pbsMonitor -jn 2 -cn 24 -exe tgyro -e . -n 48'
executable =executable + 'pbsMonitor '\
            +' -jq '+str(root['SETTINGS']['SETUP']['pbs_queue']) \
            +' -jn '+str(root['SETTINGS']['SETUP']['num_nodes']) \
            +' -cn '+str(root['SETTINGS']['SETUP']['num_cores']) \
            +' -wt '+str(root['SETTINGS']['SETUP']['wall_time']) \
            +' -exe '+' tgyro -e . -n ' + str(root['SETTINGS']['SETUP']['num_nodes']*root['SETTINGS']['SETUP']['num_cores'])

#-----------------------
# Execute ONETWO
#-----------------------
ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable)

#-----------------------
# load the results
#-----------------------
for item in outputs[0:-p_tgyro*2]:
    root['OUTPUTS']['TGYRO'][item]=OMFITasciitable(item)
count=1
for item in outputs[-p_tgyro*2:-p_tgyro]:
    root['OUTPUTS']['TGYRO']['out.tglf.localdump_'+str(count)]=OMFITgaCode(item)
    count=count+1
count=1
for item in outputs[-p_tgyro:]:
    root['OUTPUTS']['TGYRO']['out.neo.localdump_'+str(count)]=OMFITgaCode(item)
    count=count+1
