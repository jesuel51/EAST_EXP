#-*-Python-*-
# Created by xiangjian at 2015/09/10 15:02

# What are the input files

inputs=[(root['INPUTS']['EFIT']['rtest'],'rtest'),
        (root['INPUTS']['EFIT']['g0file'],'g0file'),
        (root['INPUTS']['EFIT']['exeEFIT.sh'],'exeEFIT.sh'),
	]
##----------------------
### output
##----------------------
outputs=['g000000.00000','a000000.00000']
executable = 'chmod 777 exeEFIT.sh ; ./exeEFIT.sh'
#-----------------------
# Execute ONETWO
#-----------------------
ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable)
#-----------------------
# load the results
#-----------------------
root['OUTPUTS']['EFIT']['gfile']=OMFITeqdsk('g000000.00000')
root['OUTPUTS']['EFIT']['afile']=OMFITeqdsk('a000000.00000')
