import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# have to remove commas from end of lines, liekly with a sed coommand
#done
onespec = np.loadtxt(fname='../data/assayedit.txt', delimiter=',', skiprows=2, max_rows=570)


#define arrays for use
Ex496x = onespec[0:570, 0:1]

Ex496y = onespec[0:570, 1:2]


# plotting funciton (maybe make b positive to start uphill plot?)
#DEFINE here
def optfunc(x, a, b, c):
   return a * np.exp(-b * x) + c


# simple plot of data (already done but testing documentation)
# b arg seems just colour of plot
plt.plot(Ex496x, Ex496y, 'b-', label='Ex496Em573_vs_t')


popt, pcov = curve_fit(optfunc, Ex496x, Ex496y)

#give popt random array of numbers
#DEFINE here (no dont, is just a name. popt (the vaqrriables will be defined by curve()))


#plot
#why is label indented, because it has to be below previous label?
plt.plot(Ex496x, optfunc(Ex496x, *popt), '-r',
        label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

#plot dimen
plt.xlabel('t')
plt.ylabel('Int')
plt.legend()
plt.show()
plt.savefig('FLoptPLT.png')