from matplotlib import pyplot, cm
from matplotlib.colors import Normalize

ax = pyplot.figure()
norm = Normalize()
magnitude = numpy.sqrt(u[::2]**2 + v[::2]**2)
puyplot.quiver(u[::2],v[::2],norm(magnitude),scale=60,cmap=pyplot.cm.jet)
ax.savefig('frame'+str(i).zfill(5)+'.png',dpi=300)
ax.clear()


