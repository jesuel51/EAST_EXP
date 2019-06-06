# this script is used to plot the n&T profile of inone file with adding the pedestal profile
# define a function that can find the index of the elecments which is satisfied an condition in an array
def larger(para,arr):
    ind=[]
    count=0
    for item in arr:
        if item > para:
            ind.append(count)
        count=count+1
    return ind
# define a function to read the data of the eped result
def readpeddata(fn,num):
# fn: name of the file
# num: lines in the file
#    fn=root['INPUTS']['ONETWO']['epedfile'].filename
    fid=open(fn,'r')
    lines=fid.readlines()
    rho=zeros(num)
    ne=zeros(num)
    Te=zeros(num)
    count=0
    for item in lines:
        line=item.split()
        rho[count]=line[0]
        ne[count]=line[1]
        Te[count]=line[2]
        count = count + 1
    return rho,ne,Te
# define a function to cat 2 section of profiles
def catpro(rho1,pro1,rho2,pro2,rholink):
    val1=spline(rho1,pro1,rholink)
    val2=spline(rho2,pro2,rholink)
    facdiff=val1/val2
#    print([val1,val2])
#    print(valdiff)
    pro2=pro2*facdiff
    ind1=larger(rholink,rho1)
    ind2=larger(rholink,rho2)
#    print([ind1,ind2])
    procat=concatenate((pro1[0:ind1[0]],pro2[ind2[0]:]))
    rhocat=concatenate((rho1[0:ind1[0]],rho2[ind2[0]:]))
    rho=linspace(rho1[0],rho2[-1],51)
    pronew=spline(rhocat,procat,rho)
    return rho,pronew
#ne channel
rho_ne_exp_fit=root['INPUTS']['ONETWO']['raw']['ne']['namelist']['fit_rho']
ne_exp_fit=root['INPUTS']['ONETWO']['raw']['ne']['namelist']['fit_data']
ne_exp_raw=root['INPUTS']['ONETWO']['raw']['ne']['namelist']['raw_data']
rho_ne_exp_raw=root['INPUTS']['ONETWO']['raw']['ne']['namelist']['raw_rho']
#rho_ne_exp_raw_exclude=root['INPUTS']['ONETWO']['raw']['ne']['namelist']['excluded_x']
#ne_exp_raw_exclude=root['INPUTS']['ONETWO']['raw']['ne']['namelist']['excluded_y']
#======================================================================
# Te channel
#Te_exp=root['INPUTS']['ONETWO']['inone']['NAMELIS1']['TEIN']
rho_Te_exp_fit=root['INPUTS']['ONETWO']['raw']['Te']['namelist']['fit_rho']
Te_exp_fit=root['INPUTS']['ONETWO']['raw']['Te']['namelist']['fit_data']
#Te_exp=root['INPUTS']['TGYRO']['input.profiles']['Te']
Te_exp_raw=root['INPUTS']['ONETWO']['raw']['Te']['namelist']['raw_data']
rho_Te_exp_raw=root['INPUTS']['ONETWO']['raw']['Te']['namelist']['raw_rho']
#rho_Te_exp_raw_exclude=root['INPUTS']['ONETWO']['raw']['Te']['namelist']['excluded_x']
#Te_exp_raw_exclude=root['INPUTS']['ONETWO']['raw']['Te']['namelist']['excluded_y']
if Te_exp_fit[0]>10:
    Te_exp_fit=array(Te_exp_fit)/1.e3
if Te_exp_raw[-1]>100:
    Te_exp_raw=array(Te_exp_raw)/1.e3
#if Te_exp_raw_exclude[-1]>100:
#    Te_exp_raw_exclude=array(Te_exp_raw_exclude)/1.e3
# ============================================================================
# Ti Channel
#Ti_exp=root['INPUTS']['ONETWO']['inone']['NAMELIS1']['TIIN']
rho_Ti_exp_fit=root['INPUTS']['ONETWO']['raw']['Ti']['namelist']['fit_rho']
Ti_exp_fit=root['INPUTS']['ONETWO']['raw']['Ti']['namelist']['fit_data']
Ti_exp=root['INPUTS']['TGYRO']['input.profiles']['Ti_1']
Ti_exp_raw=root['INPUTS']['ONETWO']['raw']['Ti']['namelist']['raw_data']
rho_Ti_exp_raw=root['INPUTS']['ONETWO']['raw']['Ti']['namelist']['raw_rho']
rho_Ti_exp_fit_12=root['INPUTS']['ONETWO']['inone']['NAMELIS1']['RTIIN']
Ti_exp_fit_12=root['INPUTS']['ONETWO']['inone']['NAMELIS1']['TIIN']
# rho_Ti_exp_raw_exclude=root['INPUTS']['ONETWO']['raw']['Ti']['namelist']['excluded_x']
# Ti_exp_raw_exclude=root['INPUTS']['ONETWO']['raw']['Ti']['namelist']['excluded_y']
if Ti_exp_fit[-1]>100:
    Ti_exp_fit=array(Ti_exp_fit)/1.e3
if Ti_exp_raw[-1]>100:
    Ti_exp_raw=array(Ti_exp_raw)/1.e3
#if Te_exp_raw_exclude>100:
#    Te_exp_raw_exclude=array(Te_exp_raw_exclude)/1.e3
#======================================================================
#ne_tgyro=root['SETTINGS']['TEMP']['ne']
#Te_tgyro=root['SETTINGS']['TEMP']['Te']
#Ti_tgyro=root['SETTINGS']['TEMP']['Ti']
#rho_tgyro=root['SETTINGS']['TEMP']['rho']
#
fs1=24
fs2=20
fn=root['INPUTS']['ONETWO']['epedfile'].filename
rhoeped,neeped,Teeped=readpeddata(fn,201)
rholink=0.7
figure('Profile Adding EPED result',figsize=[20,8])
subplot(1,3,1)
plot(rho_ne_exp_fit,array(ne_exp_fit)/1.e13,'-b',linewidth=2,label='exp-fit')
plot(rho_ne_exp_raw,array(ne_exp_raw)/1.e13,'b*',markersize=12,linewidth=2,label='exp-raw')
#plot(rho_ne_exp_raw_exclude,array(ne_exp_raw_exclude),'bd',linewidth=2,label='exp-raw_excluded')
#plot(rho_tgyro,array(ne_tgyro)/1.e13,'-ro',linewidth=2,label='simu')
#rhocat,necat=catpro(rho_ne_exp_fit,array(ne_exp_fit)/1.e13,rhoeped,neeped,rhocat)
rhocat,necat=catpro(rho_ne_exp_fit,ne_exp_fit/1.e13,rhoeped,neeped,rholink)
plot(rhocat,necat,'-r',markersize=12,linewidth=2,label='exp-fit-addped')
xticks(fontsize=fs2,family='serif')
yticks(fontsize=fs2,family='serif')
title('ne',fontsize=fs1,family='serif')
ylim([0,7.5])
xlim([0,1])
xlabel('$rho$',fontsize=fs2,family='serif')
ylabel('$10^{13}cm^{-3}$',fontsize=fs2,family='serif')
legend(loc=0,fontsize=fs2).draggable(True)
subplot(1,3,2)
plot(rho_Te_exp_fit,array(Te_exp_fit),'-b',linewidth=2,label='exp-fit')
plot(rho_Te_exp_raw,array(Te_exp_raw),'b*',markersize=12,linewidth=2,label='exp-raw')
#plot(rho_Te_exp_raw_exclude,array(Te_exp_raw_exclude),'bd',linewidth=2,label='exp-raw_excluded')
#plot(rho_tgyro,Te_tgyro,'-ro',linewidth=2,label='simu')
#rhocat,Tecat=catpro(rho_ne_exp_fit,array(Te_exp_fit),rhoeped,Teeped,rhocat)
rhocat,Tecat=catpro(rho_ne_exp_fit,Te_exp_fit,rhoeped,Teeped,rholink)
plot(rhocat,Tecat,'-r',markersize=12,linewidth=2,label='exp-fit-addped')
xticks(fontsize=fs2,family='serif')
yticks(fontsize=fs2,family='serif')
title('Te',fontsize=fs1,family='serif')
ylim([0,3])
xlabel('$rho$',fontsize=fs2,family='serif')
ylabel('$keV$',fontsize=fs2,family='serif')
legend(loc=0,fontsize=fs2).draggable(True)
iuseTeasTi=1  # decide whether to use the Te data outside rho=0.6 as Te data
subplot(1,3,3)
#plot(rho_Ti_exp_fit,array(Ti_exp_fit),'-b',linewidth=2,label='exp-fit')
plot(rho_Ti_exp_raw,array(Ti_exp_raw),'b*',markersize=12,linewidth=2,label='exp-raw')
if iuseTeasTi==1:
    ind=larger(0.6,rho_Te_exp_raw)
    indfit=larger(0.6,rho_Te_exp_fit)
    plot(rho_Te_exp_raw[ind],array(Te_exp_raw[ind]),'bd',markersize=12,linewidth=2,label='Te-raw')
#    plot(rho_Ti_exp_fit[0:indfit[0]],array(Ti_exp_fit[0:indfit[0]]),'-b',linewidth=2,label='exp-fit')
    plot(rho_Ti_exp_fit_12,Ti_exp_fit_12,'-b',linewidth=2,label='exp-fit')
#    rhocat,Ticat=catpro(rho_Ti_exp_fit,array(Ti_exp_fit)/1.e13,rhoeped,Teeped,0.9)
    rhocat,Ticat=catpro(rho_Ti_exp_fit_12,Ti_exp_fit_12,rhoeped,Teeped,rholink)
    plot(rhocat,Ticat,'-r',markersize=12,linewidth=2,label='exp-fit-addped')
else:
#    plot(rho_Ti_exp_fit,array(Ti_exp_fit),'-b',linewidth=2,label='exp-fit')
    plot(rho_Ti_exp_fit_12,Ti_exp_fit_12,'-b',linewidth=2,label='exp-fit')
#plot(rho_Ti_exp_raw_exclude,array(Ti_exp_raw_exclude)/1.e13,'-bo',linewidth=2,label='exp-raw_excluded')
#plot(rho_tgyro,Ti_tgyro,'-ro',linewidth=2,label='simu')
xticks(fontsize=fs2,family='serif')
yticks(fontsize=fs2,family='serif')
title('Ti',fontsize=fs1,family='serif')
ylim([0,3])
xlabel('$rho$',fontsize=fs2,family='serif')
ylabel('$keV$',fontsize=fs2,family='serif')
legend(loc=0,fontsize=fs2).draggable(True)
