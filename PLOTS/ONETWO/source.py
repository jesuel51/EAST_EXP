nj=201
fs1=14
fs2=20
fs3=20
lw=3;  #linewidth
rho=linspace(0,1,nj);
figure(312,figsize=[28,11])
#	 electron part
qbeame=root['OUTPUTS']['ONETWO']['trpltout.nc']['qbeame']['data'][-1];	# beam on electrons
pwrbme=root['OUTPUTS']['ONETWO']['trpltout.nc']['pwrbme']['data'][-1];
qrfeiv=root['OUTPUTS']['ONETWO']['trpltout.nc']['qrfeiv']['data'][-1];	# rf on electrons
prfe=root['OUTPUTS']['ONETWO']['trpltout.nc']['prfe']['data'][-1];
qfusev=root['OUTPUTS']['ONETWO']['trpltout.nc']['qfusev']['data'][-1];	# fusion on electrons
pfuse=root['OUTPUTS']['ONETWO']['trpltout.nc']['pfuse']['data'][-1];
qrad=root['OUTPUTS']['ONETWO']['trpltout.nc']['qrad']['data'][-1];		# radiation on  electrons
prad=root['OUTPUTS']['ONETWO']['trpltout.nc']['prad']['data'][-1];
qohm=root['OUTPUTS']['ONETWO']['trpltout.nc']['qohm']['data'][-1];		# ohm heating on electrons
pohm=root['OUTPUTS']['ONETWO']['trpltout.nc']['pohm']['data'][-1];	
qdelten=root['OUTPUTS']['ONETWO']['trpltout.nc']['qdelten']['data'][-1];		# electron-ion power exchange
pdelten=root['OUTPUTS']['ONETWO']['trpltout.nc']['pdelten']['data'][-1];		
iexch=1  # determine whether to include the energy exchange between ion and electron channels
if iexch==1:
    qsume=qbeame+qrfeiv+qfusev+qohm+qrad-qdelten;
    psume=pwrbme+prfe+pfuse+pohm+prad+pdelten;
else:
    qsume=qbeame+qrfeiv+qfusev+qohm+qrad;
    psume=pwrbme+prfe+pfuse+pohm+prad;
#	ion part
qbeami=root['OUTPUTS']['ONETWO']['trpltout.nc']['qbeami']['data'][-1];	# beam on ions
pwrbmi=root['OUTPUTS']['ONETWO']['trpltout.nc']['pwrbmi']['data'][-1];
qrfiiv=root['OUTPUTS']['ONETWO']['trpltout.nc']['qrfiiv']['data'][-1];	# rf on ions
prfi=root['OUTPUTS']['ONETWO']['trpltout.nc']['prfi']['data'][-1];
qfusiv=root['OUTPUTS']['ONETWO']['trpltout.nc']['qfusiv']['data'][-1];	# fusion on electrons
pfusi=root['OUTPUTS']['ONETWO']['trpltout.nc']['pfusi']['data'][-1];
if iexch==1:
    qsumi=qbeami+qrfiiv+qfusiv+qdelten;
    psumi=pwrbmi+prfi+pfusi-pdelten;
else:
    qsumi=qbeami+qrfiiv+qfusiv;
    psumi=pwrbmi+prfi+pfusi;

storqueb=root['OUTPUTS']['ONETWO']['trpltout.nc']['storqueb']['data'][-1];
smagtorque=root['OUTPUTS']['ONETWO']['trpltout.nc']['smagtorque']['data'][-1];
finttorque=root['OUTPUTS']['Profile_gen']['input.profiles']['flow_mom']
h1=subplot(2,4,1)
get(h1)
#get(h1.position)
plot(rho,qbeame,'-g',label='beam',linewidth=lw)
plot(rho,qrfeiv,'-k',label='rf',linewidth=lw)
#plot(rho,qfusev,'-y',label='fusion',linewidth=lw)
plot(rho,-qrad,'-c',label='radiation',linewidth=lw)
plot(rho,qohm,'-r',label='ohm',linewidth=lw)
if iexch==1:
    plot(rho,-qdelten,'-b',label='exchange',linewidth=lw)
plot(rho,qsume,'-m',label='tot',linewidth=lw)
#ylim([-0.40,1.2])
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
title('Power on Electron',fontsize=fs2,family='serif')
ylabel('$MW.m^{-3}$',fontsize=fs2,family='serif')
text(0.5,0.45,'(a)',fontsize=fs3)
legend(loc=0,fontsize=fs1).draggable(True)
subplot(2,4,5)
plot(rho,pwrbme/1.e6,'-g',label='beam',linewidth=lw)
plot(rho,prfe/1.e6,'-k',label='rf',linewidth=lw)
#plot(rho,pfuse/1.e6,'-y',label='fusion',linewidth=lw)
plot(rho,prad/1.e6,'-c',label='radiation',linewidth=lw)
#plot(rho,pohm/1.e6,'-r',label='ohm',linewidth=lw)
if iexch==1:
    plot(rho,pdelten/1.e6,'-b',label='exchange',linewidth=lw)
plot(rho,psume/1.e6,'-m',label='tot',linewidth=lw)
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
#ylim([-1,3])
xlabel('$rho$',fontsize=fs2,family='serif')
ylabel('$MW$',fontsize=fs2,family='serif')
title('Integrated Power on Electron',fontsize=fs2,family='serif')
legend(loc=0,fontsize=fs1).draggable(True)
subplot(2,4,2)
plot(rho,qbeami,'-g',label='beam',linewidth=lw)
plot(rho,qrfiiv,'-k',label='rf',linewidth=lw)
#plot(rho,qfusiv,'-y',label='fusion',linewidth=lw)
if iexch==1:
    plot(rho,qdelten,'-b',label='exchange',linewidth=lw)
plot(rho,qsumi,'-m',label='tot',linewidth=lw)
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
#ylim([-0.40,1.2])
ylabel('$MW.m{-3}$',fontsize=fs2,family='serif')
title('Power on Ion',fontsize=fs2,family='serif')
text(0.5,0.45,'(b)',fontsize=fs3)
legend(loc=0,fontsize=fs1).draggable(True)
subplot(2,4,6)
plot(rho,pwrbmi/1.e6,'-g',label='beam',linewidth=lw)
plot(rho,prfi/1.e6,'-k',label='rf',linewidth=lw)
#plot(rho,pfusi/1.e6,'-y',label='fusion',linewidth=lw)
if iexch==1:
    plot(rho,-pdelten/1.e6,'-b',label='exchange',linewidth=lw)
plot(rho,psumi/1.e6,'-m',label='tot',linewidth=lw)
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
xlabel('$rho$',fontsize=fs2,family='serif')
ylabel('$MW$',fontsize=fs2,family='serif')
#ylim([-1,3])
title('Integrated Power on Ion',fontsize=fs2,family='serif')
legend(loc=0,fontsize=fs1).draggable(True)
subplot(2,4,3)
swall=root['OUTPUTS']['ONETWO']['statefile.nc']['sion']['data'][0]
sbeam=root['OUTPUTS']['ONETWO']['statefile.nc']['sbeam']['data'][-1]
semilogy(rho,swall,'-k',label='wall',linewidth=lw)
semilogy(rho,sbeam,'-g',label='beam',linewidth=lw)
semilogy(rho,swall+sbeam,'-m',label='tot',linewidth=lw)
#xlabel('$rho$',fontsize=fs2,family='serif')
ylabel('$m^{-3}s^{-1}$',fontsize=fs2,family='serif')
#ylim([1.e16,1.e21])
text(0.5,1e43**0.5,'(c)',fontsize=fs3)
title('Particle Source',fontsize=fs2,family='serif')
legend(loc=0,fontsize=fs1).draggable(True)
subplot(2,4,7)
flow_wall=root['OUTPUTS']['Profile_gen']['input.profiles']['flow_wall']
flow_beam=root['OUTPUTS']['Profile_gen']['input.profiles']['flow_beam']
semilogy(rho,flow_wall,'-k',label='wall',linewidth=lw)
semilogy(rho,flow_beam,'-g',label='beam',linewidth=lw)
semilogy(rho,flow_wall+flow_beam,'-m',label='total',linewidth=lw)
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
xlabel('$rho$',fontsize=fs2,family='serif')
ylabel('$MW.keV^{-1}$',fontsize=fs2,family='serif')
title('Integrated Particle Source',fontsize=fs2,family='serif')
legend(loc=0,fontsize=fs1).draggable(True)
subplot(2,4,4)
plot(rho,storqueb,'-g',label='beam',linewidth=lw)
#plot(rho,smagtorque,'-ok',label='magnetic breaking')
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
ylabel('$N.m^{-2}$',fontsize=fs2,family='serif')
title('Torque Density',fontsize=fs2,family='serif')
#ylim([0,0.5])
text(0.5,0.55,'(d)',fontsize=fs3)
legend(loc=0,fontsize=fs1).draggable(True)   
subplot(2,4,8)
plot(rho,finttorque,'-ob',label='beam',linewidth=lw)
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
xlabel('$rho$',fontsize=fs2)
title('Integrated Torque',fontsize=fs2,family='serif')
ylabel('$N.m$',fontsize=fs2,family='serif')
legend(loc=0,fontsize=fs1).draggable(True)
