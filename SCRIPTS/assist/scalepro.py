TeScale=root['SETTINGS']['PHYSICS']['TeScale']
TiScale=root['SETTINGS']['PHYSICS']['TiScale']
neScale=root['SETTINGS']['PHYSICS']['neScale']
dataroot=root['INPUTS']['ONETWO']['inone']['NAMELIS1']
dataroot['TEIN']=TeScale*dataroot['TEIN']
dataroot['TIIN']=TiScale*dataroot['TIIN']
dataroot['ENEIN']=neScale*dataroot['ENEIN']
