import numpy as np
import re
import time as t
import matplotlib.pyplot as plt
from math import sin, cos, sqrt, atan2, radians
from os import listdir
from os.path import isfile, join

R = 6373.0

def distance(point1,point2):
    lat1,lon1 = point1
    lat2,lon2 = point2
    dlon = radians(lon2) - radians(lon1)
    dlat = radians(lat2) - radians(lat1)
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    
    return distance


if __name__=='__main__':
    directory = '.'
    print(listdir(directory))
    onlygpx = [f for f in listdir(directory) if isfile(join(directory, f)) and len(f)>3 and f[-4:] == '.gpx']
    for name in onlygpx:
        # name = 'track.gpx'
        print(name)
        f = open(directory+'/'+name,'r')
        ALL = f.read()
        f.close()
        lats = [float(i) for i in 
                re.findall(r'(?<=[<]trkpt lat=")-?[0-9]+\.[0-9]+',ALL)]
        lons = [float(i) for i in re.findall(r'(?<=" lon=")-?[0-9]+\.[0-9]+',ALL)]
        times= re.findall(r'(?<=[<]time[>]).*?(?=Z[<]/time[>])',ALL)

        eles = [float(i) for i in re.findall(r'(?<=[<]ele[>]).*?(?=[<]/ele[>])',ALL)]

        t0 = t.mktime(t.strptime(times[0],'%Y-%m-%dT%H:%M:%S'))
        secs = np.array([t.mktime(t.strptime(ti,'%Y-%m-%dT%H:%M:%S'))-t0 
                for ti in times])
        dist = [0]+[distance((lats[i],lons[i]),(lats[i+1],lons[i+1])) 
                for i in range(len(lats)-1)]
        dist = np.array(dist)
        vel = dist/np.array([1]+[secs[i+1]-secs[i] for i in range(secs.shape[0]-1)])

        w = 60
        vel_mediamovil = np.convolve(vel, np.ones(w), 'valid') / (w+1)

        # plot
        fig, ax = plt.subplots()

        ax.plot(secs, eles, linewidth=2.0)

        # plt.show()
        plt.savefig(fname = directory+'/'+name[:-4]+'_altitud.pdf',format = 'pdf',
                transparent = True,bbox_inches='tight')

        fig, ax = plt.subplots()

        ax.plot(np.array(secs)/3600, vel*3600, linewidth=1.0)
        ax.plot((np.array(secs)[:801-w]+secs[30])/3600, vel_mediamovil*3600, linewidth=2.0,color='red')

        # plt.show()
        plt.savefig(fname = directory+'/'+name[:-4]+'_velocidad.pdf',format = 'pdf',
                transparent = True,bbox_inches='tight')
        # print(np.array(secs)[:801-w]/3600+60/3600)
        # print(vel_mediamovil*3600)
        print(np.array(secs)/3600)
        print(vel*3600)
        print(min(vel),max(vel*3600))
