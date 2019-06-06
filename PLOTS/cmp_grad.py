# plot the coparison of gradient
root['PLOTS']['TGYRO']['profile.py'].run()
# write it to the root['SETTINGS']['TEMP']
temp=root['SETTINGS']['TEMP']
rho=temp['rho']
aLne_exp=temp['aLne_exp']
aLTe_exp=temp['aLTe_exp']
aLTi_exp=temp['aLTi_exp']
aLw0_exp=temp['aLw0_exp']
aLne_sim=temp['aLne_sim']
aLTe_sim=temp['aLTe_sim']
aLTi_sim=temp['aLTi_sim']
aLw0_sim=temp['aLw0_sim']
# plot
figure(figsize=[10,10])
lw = 2
ms = 8
fs1 = 20
fs2 = 24
subplot(2,2,1)
plot(rho, aLTe_exp,'-bo',linewidth=lw,markersize=ms,label='exp')
plot(rho, aLTe_sim,'-ro',linewidth=lw,markersize=ms,label='sim')
title('$a/L_{Te}$',fontsize=fs2,family='serif')
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
#    ylim([0,10])
legend(loc=0,fontsize=fs1).draggable(True)
subplot(2,2,2)
plot(rho, aLTi_exp,'-bo',linewidth=lw,markersize=ms)
plot(rho, aLTi_sim,'-ro',linewidth=lw,markersize=ms)
#xlabel('$r_{min}$',fontsize=fs2,family='serif')
title('$a/L_{Ti}$',fontsize=fs2,family='serif')
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
#    ylim([0,10])
#text(xtext,9,'(e)',fontsize=fs3)
#legend(loc=0,fontsize=fs1).draggable(True)
subplot(2,2,3)
plot(rho, aLne_exp,'-bo',linewidth=lw,markersize=ms)
plot(rho, aLne_sim,'-ro',linewidth=lw,markersize=ms)
xlabel('$\\rho$',fontsize=fs2,family='serif')
title('$a/L_{ne}$',fontsize=fs2,family='serif')
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
#ylim([0,int(max(array(aLne_exp))+1)])
#text(xtext,9,'(e)',fontsize=fs3)
#legend(loc=0,fontsize=fs1).draggable(True)
subplot(2,2,4)
plot(rho, aLw0_exp,'-bo',linewidth=lw,markersize=ms)
plot(rho, aLw0_sim,'-ro',linewidth=lw,markersize=ms)
xlabel('$\\rho$',fontsize=fs2,family='serif')
title('$\gamma_E$',fontsize=fs2,family='serif')
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
#    ylim([0,10])
#ylim([0,int(max(array(aLw0_exp))+2)])
#text(xtext,9,'(e)',fontsize=fs3)
#legend(loc=0,fontsize=fs1).draggable(True)
