import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Create a Basemap instance for geographic projection
bbox = [np.min(lats)-zoom_scale, np.max(lats)+zoom_scale,
        np.min(lons)-zoom_scale, np.max(lons)+zoom_scale]

m = Basemap(projection='merc', llcrnrlat=bbox[0], urcrnrlat=bbox[1],
            llcrnrlon=bbox[2], urcrnrlon=bbox[3], lat_ts=10, resolution='i')

# Load altitude data and reshape it
lon = np.linspace(-121.5, -116.9, 50)
lat = np.linspace(45, 48.2, 50)
altitude = np.loadtxt('is-g14.txt')
al = np.array(altitude).reshape(len(lon), len(lat)).T

# Create meshgrid for longitude and latitude
x, y = m(*np.meshgrid(lon, lat))

# Contour plot
clevs = np.linspace(np.min(al), np.max(al), 10)
cs = m.contourf(x, y, al, clevs, extend='both', cmap=plt.get_cmap('jet'))

# Draw map boundaries and countries
m.drawmapboundary()
m.drawcountries(linewidth=1, linestyle='solid', color='k')

# Draw meridians and parallels
m.drawmeridians(np.arange(bbox[2], bbox[3], (bbox[3]-bbox[2])/5), color='k', linewidth=0.5, 
                dashes=[4, 4], labels=[0, 0, 0, 1], fmt="%.1f", rotation=15, fontsize=11)
m.drawparallels(np.arange(bbox[0], bbox[1], (bbox[1]-bbox[0])/5), color='k', linewidth=0.5, 
                dashes=[4, 4], labels=[1, 0, 0, 0], fmt="%.1f", fontsize=11)

# Draw rivers
m.drawrivers(color='#0000ff')

# Add color bar
cbar = m.colorbar(cs, location='right', size=0.15, pad="3%")
cbar.set_label('PWV (mm)', fontsize=13)

# Show the plot
plt.show()
