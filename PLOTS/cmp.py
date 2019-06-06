# plot the experimental profile and TGYRO output profile
root['PLOTS']['TGYRO']['profile.py'].run()
# define a function that can find the index of the elecments which is satisfied an condition in an array
def larger(para,arr):
    ind=[]
    count=0
    for item in arr:
        if item > para:
            ind.append(count)
        count=count+1
    return ind
inputpro=root['INPUTS']['TGYRO']['input.profiles']
ne_exp=inputpro['ne']
Te_exp=inputpro['Te']
Ti_exp=inputpro['Ti_1']
w0_exp=inputpro['omega0']
rho_exp=inputpro['rho']
ne_sim=root['SETTINGS']['TEMP']['ne_sim']
Te_sim=root['SETTINGS']['TEMP']['Te_sim']
Ti_sim=root['SETTINGS']['TEMP']['Ti_sim']
w0_sim=root['SETTINGS']['TEMP']['w0_sim']
rho_sim=root['SETTINGS']['TEMP']['rho']
#
fs1=24
fs2=20
figure('Profile Comparison',figsize=[10,10])
T_max=ceil(max([Te_sim[0],Ti_sim[0],Ti_exp[0],Te_exp[0]]))
# Te
subplot(2,2,1)
plot(rho_exp,Te_exp,'-b',linewidth=2,label='exp')
plot(rho_sim,Te_sim,'-ro',linewidth=2,label='simu')
legend(loc=0,fontsize=fs2).draggable(True)
xticks(fontsize=fs2,family='serif')
yticks(fontsize=fs2,family='serif')
title('Te',fontsize=fs1,family='serif')
ylim([0,T_max])
ylabel('$keV$',fontsize=fs2,family='serif')
# Ti profile
subplot(2,2,2)
plot(rho_sim,Ti_sim,'-ro',linewidth=2)
plot(rho_exp,Ti_exp,'-b',linewidth=2)
xticks(fontsize=fs2,family='serif')
yticks(fontsize=fs2,family='serif')
title('Ti',fontsize=fs1,family='serif')
ylim([0,T_max])
ylabel('$keV$',fontsize=fs2,family='serif')
# density
subplot(2,2,3)
plot(rho_exp,ne_exp,'-b',linewidth=2)
plot(rho_sim,array(ne_sim)/1.e13,'-ro',linewidth=2)
xticks(fontsize=fs2,family='serif')
yticks(fontsize=fs2,family='serif')
title('ne',fontsize=fs1,family='serif')
ylim([0,ceil(1.2*max(ne_exp[0]/1.e13,ne_sim[0]/1.e13))])
xlim([0,1])
xlabel('$rho$',fontsize=fs2,family='serif')
ylabel('$10^{13}cm^{-3}$',fontsize=fs2,family='serif')
# rotation
subplot(2,2,4)
plot(rho_exp,w0_exp/1.e3,'-b',linewidth=2)
plot(rho_sim,w0_sim/1.e3,'-ro',linewidth=2)
xticks(fontsize=fs2,family='serif')
yticks(fontsize=fs2,family='serif')
title('$\omega0$',fontsize=fs1,family='serif')
xlim([0,1])
xlabel('$rho$',fontsize=fs2,family='serif')
ylabel('$krads^{-1}$',fontsize=fs2,family='serif')
