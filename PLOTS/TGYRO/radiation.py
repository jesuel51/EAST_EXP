#-*-Python-*-
# Created by xiangjian at 2015/05/04 21:32
# this script is used to plot the result of all power conponent of electrons and ions
plt.close();
fs1=16;
fs2=24;
fs3=22;
p_tgyro=root['SETTINGS']['PHYSICS']['p_tgyro']
geometry1=root['OUTPUTS']['TGYRO']['out.tgyro.geometry.1']['data'];
geometry1=map(list,zip(*geometry1))
rho=geometry1[1]
power_e=root['OUTPUTS']['TGYRO']['out.tgyro.power_e']['data'];
power_e=map(list,zip(*power_e));
pow_e_aux=power_e[2][1:p_tgyro+2]
pow_e_brem=power_e[3][1:p_tgyro+2]
pow_e_sync=power_e[4][1:p_tgyro+2]
pow_e_line=power_e[5][1:p_tgyro+2]
pow_e_exch=power_e[6][1:p_tgyro+2]
pow_e_expwd=power_e[7][1:p_tgyro+2]
pow_e_tot=power_e[8][1:p_tgyro+2]
power_i=root['OUTPUTS']['TGYRO']['out.tgyro.power_i']['data'];
power_i=map(list,zip(*power_i));
pow_i_aux=power_i[2][1:p_tgyro+2]
pow_i_exch=power_i[3][1:p_tgyro+2]
pow_i_expwd=power_i[4][1:p_tgyro+2]
pow_i_tot=power_i[5][1:p_tgyro+2]

plt.figure('Power',figsize=[10,8])
subplot(3,2,1)
plot(rho,pow_e_aux,'-*k',linewidth=2,label='e-aux')
plot(rho,pow_i_aux,'-*r',linewidth=2,label='i-aux')
legend(loc='lower right',fontsize=fs1).draggable(True)
#text(0.1,1.e1,'(a) Ion Energy',fontsize=fs3,family='serif')
#ylim([1.e-3,1.e2])
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
subplot(3,2,2)
plot(rho,pow_e_tot,'-*k',linewidth=2,label='e-tot')
plot(rho,pow_i_tot,'-*r',linewidth=2,label='i-tot')
legend(loc='lower right',fontsize=fs1).draggable(True)
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
#ylim([1.e-3,1.e2])
#xlabel('$rho$',fontsize=fs2,family='serif')
#text(0.1,1.e1,'(b) Electron Energy',fontsize=fs3,family='serif')
#ylabel('$EFlux_e/GB$',fontsize=fs2,family='serif')
subplot(3,2,3)
plot(rho,pow_e_brem,'-*k',linewidth=2,label='bream')
plot(rho,pow_e_sync,'-*r',linewidth=2,label='sync')
plot(rho,pow_e_line,'-*m',linewidth=2,label='line')
legend(loc='lower right',fontsize=fs1).draggable(True)
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
#ylim([1.e-4,1.e0])
xlabel('$rho$',fontsize=fs2,family='serif')
#text(0.1,1.e-1,'(c) Particle',fontsize=fs3,family='serif')
#ylabel('$PFlux_e/GB$',fontsize=fs2,family='serif')
subplot(3,2,4)
plot(rho,pow_e_aux,'-*b',linewidth=2,label='aux-e')
plot(rho,pow_e_brem,'-*k',linewidth=2,label='bream')
plot(rho,pow_e_sync,'-*r',linewidth=2,label='sync')
plot(rho,pow_e_line,'-*m',linewidth=2,label='line')
plot(rho,pow_e_exch,'-ob',linewidth=2,label='exch-e')
plot(rho,pow_e_expwd,'-ok',linewidth=2,label='expwd-e')
plot(rho,pow_e_tot,'-or',linewidth=2,label='tot-e')
legend(loc='lower right',fontsize=fs1).draggable(True)
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
#ylim([1.e-3,1.e2])
xlabel('$rho$',fontsize=fs2,family='serif')
subplot(3,2,5)
plot(rho,pow_i_aux,'-*b',linewidth=2,label='aux-i')
plot(rho,pow_i_exch,'-ob',linewidth=2,label='exch-i')
plot(rho,pow_i_expwd,'-ob',linewidth=2,label='expwd-i')
plot(rho,pow_i_tot,'-or',linewidth=2,label='tot-e')
legend(loc='lower right',fontsize=fs1).draggable(True)
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
#ylim([1.e-3,1.e2])
xlabel('$rho$',fontsize=fs2,family='serif')

