##--------------------------
# What are the input files
##--------------------------
inputs=[(root['INPUTS']['Profile_gen']['statefile.nc'],'statefile.nc'),
        (root['INPUTS']['Profile_gen']['gfile'],'g000000.00000'),
	]
##----------------------
### output
##----------------------
outputs=['input.profiles','input.profiles.geo']
#executable =' module load netcdf/4.1.3;export GACODE_ROOT=/project/gacode; . $GACODE_ROOT/shared/bin/gacode_setup; profiles_gen -i statefile.nc -g g000000.00000'
executable ='module load netcdf/4.1.3; profiles_gen -i statefile.nc -g g000000.00000'
#-----------------------
# Execute Profile_gen
#-----------------------
ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable)
#-----------------------
# load the results
#-----------------------
root['OUTPUTS']['Profile_gen']['input.profiles']=OMFITgaCode('input.profiles')
root['OUTPUTS']['Profile_gen']['input.profiles.geo']=OMFITgaCode('input.profiles.geo')
