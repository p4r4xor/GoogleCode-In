import os
import sys
import geopandas
import matplotlib.pyplot as plt
import optparse
import glob

parser = optparse.OptionParser('usage: %s --map' % sys.argv[0])
parser.add_option('--map', dest='mapdir', type='string', help='map to be analyzed')
options,argvs = parser.parse_args()
if(options.mapdir==None):
	print(parser.usage)
	sys.exit(0)
elif(options.mapdir!=None):
	mapdir = options.mapdir
	print("Given Map directory: ", mapdir)
	plot1 = geopandas.read_file(mapdir+"natural.shp")
	plot2 = geopandas.read_file(mapdir+"landuse.shp")
	plot3 = geopandas.read_file(mapdir+"buildings.shp")
	plot4 = geopandas.read_file(mapdir+"roads.shp")
	plot5 = geopandas.read_file(mapdir+"railways.shp")
	plot6 = geopandas.read_file(mapdir+"waterways.shp")
	fig, ax = plt.subplots()
	plot1.plot(color='green',ax=ax)
	plot2.plot(color='slategray',ax=ax)
	plot3.plot(color='black',ax=ax)
	plot4.plot(color='orange',linewidth=0.3,ax=ax)
	plot5.plot(color='red',linewidth=0.5,ax=ax)
	plot6.plot(color='blue',linewidth=0.5,ax=ax)
	plt.show()
