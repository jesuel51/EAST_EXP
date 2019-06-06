# this script is used to plot the turbulence and neoclassical part of particle and energy transport
#plt.close();

def readouttgyro(filename):
# return all the numerisim data in a format of [numrho*niter, ncol]
    f=open(filename,'Ur')
    fread=f.readlines()
    lis=[]
    for line in fread:
        lintemp=line.split()
        try:
            temp=float(lintemp[0])
            lis.append(line)
        except:
            continue
# turn the list to array so that it can be easily handled
    row=len(lis)
    col=len(lis[0].split())
    arr=zeros([row,col])
    for k in arange(row):
        arr[k]=[float(item) for item in lis[k].split()]
    arr=arr.T
    return arr
    f.close()

IonSp=array(['D','C','D'])
ipltpflux=0
outtgyro=root['OUTPUTS']['TGYRO']
# r/a, pflux_e_neo, pflux_e_tur, eflux_e_neo, eflux_e_tur ,mflux_e_neo, mflux_e)tur, expwd_e_tur
arr_flux_e=readouttgyro(outtgyro['out.tgyro.flux_e'].filename)
# r/a, pflux_i1-neo, pflux_i1_tur, eflux_i1_neo, eflux_i1_tur, mflux_i1_neo, mflux_i1_tur, expwd_i1_tur
arr_flux_i1=readouttgyro(outtgyro['out.tgyro.flux_i1'].filename)
arr_flux_i2=readouttgyro(outtgyro['out.tgyro.flux_i2'].filename)
ptgyro=len(root['INPUTS']['TGYRO']['input.tgyro']['DIR'])
arr_geometry1=readouttgyro(outtgyro['out.tgyro.geometry.1'].filename)
rho=arr_geometry1[1][-ptgyro-1:]
ipltflux=0 # determined whether to plot the particle flux
isemiplt=1
mksz=8      # markersize
fs1=20      # fontsize
fs2=24      # fontsize
fml='serif' # font famlily
lwd=2       # linewidth
figure(figsize=[12,8])
subplot(2,2,1)
if isemiplt==1:
    semilogy(rho,arr_flux_e[3][-ptgyro-1:],'-bo',linewidth=lwd,markersize=mksz,label='neo')
    semilogy(rho,arr_flux_e[4][-ptgyro-1:],'-ro',linewidth=lwd,markersize=mksz,label='tur')
else:
    semilogy(rho,arr_flux_e[3][-ptgyro-1:],'-bo',linewidth=lwd,markersize=mksz,label='neo')
    semilogy(rho,arr_flux_e[4][-ptgyro-1:],'-ro',linewidth=lwd,markersize=mksz,label='tur')
legend(loc=0,fontsize=fs1).draggable(True)
#xlabel('$\\rho$',fontsize=fs2,family='serif')
xticks(fontsize=fs1,family=fml)
yticks(fontsize=fs1,family=fml)
ylabel('Qe',fontsize=fs2,family=fml)
subplot(2,2,2)
if isemiplt==1:
    semilogy(rho,arr_flux_i1[3][-ptgyro-1:]+arr_flux_i2[3][-ptgyro-1],'-bo',linewidth=lwd,markersize=mksz,label='neo')
    semilogy(rho,arr_flux_i1[4][-ptgyro-1:]+arr_flux_i2[3][-ptgyro-1],'-ro',linewidth=lwd,markersize=mksz,label='tur')
else:
    semilogy(rho,arr_flux_i1[3][-ptgyro-1:]+arr_flux_i2[3][-ptgyro-1],'-bo',linewidth=lwd,markersize=mksz,label='neo')
    semilogy(rho,arr_flux_i1[4][-ptgyro-1:]+arr_flux_i2[3][-ptgyro-1],'-ro',linewidth=lwd,markersize=mksz,label='tur')
#legend(loc=0,fontsize=fs1).draggable(True)
#xlabel('$\\rho$',fontsize=fs2,family='serif')
xticks(fontsize=fs1,family=fml)
yticks(fontsize=fs1,family=fml)
ylabel('Qi',fontsize=fs2,family=fml)
subplot(2,2,3)
if isemiplt==1:
    semilogy(rho,arr_flux_e[1][-ptgyro-1:],'-bo',linewidth=lwd,markersize=mksz,label='neo')
    semilogy(rho,arr_flux_e[2][-ptgyro-1:],'-ro',linewidth=lwd,markersize=mksz,label='tur')
else:
    semilogy(rho,arr_flux_e[1][-ptgyro-1:],'-bo',linewidth=lwd,markersize=mksz,label='neo')
    semilogy(rho,arr_flux_e[2][-ptgyro-1:],'-ro',linewidth=lwd,markersize=mksz,label='tur')
#legend(loc=0,fontsize=fs1).draggable(True)
xlabel('$\\rho$',fontsize=fs2,family='serif')
xticks(fontsize=fs1,family=fml)
yticks(fontsize=fs1,family=fml)
ylabel('$\Gamma_e$',fontsize=fs2,family=fml)
subplot(2,2,4)
if isemiplt==1:
    semilogy(rho,arr_flux_i1[5][-ptgyro-1:]+arr_flux_i2[5][-ptgyro-1],'-bo',linewidth=lwd,markersize=mksz,label='neo')
    semilogy(rho,arr_flux_i1[6][-ptgyro-1:]+arr_flux_i2[6][-ptgyro-1],'-ro',linewidth=lwd,markersize=mksz,label='tur')
else:
    semilogy(rho,arr_flux_i1[5][-ptgyro-1:]+arr_flux_i2[5][-ptgyro-1],'-bo',linewidth=lwd,markersize=mksz,label='neo')
    semilogy(rho,arr_flux_i1[6][-ptgyro-1:]+arr_flux_i2[6][-ptgyro-1],'-ro',linewidth=lwd,markersize=mksz,label='tur')
#legend(loc=0,fontsize=fs1).draggable(True)
xlabel('$\\rho$',fontsize=fs2,family='serif')
xticks(fontsize=fs1,family=fml)
yticks(fontsize=fs1,family=fml)
ylabel('$\Pi$',fontsize=fs2,family=fml)

