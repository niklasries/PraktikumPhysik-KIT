# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import PhyPraKit as ppk
import kafe

from kafe.function_library import exp_3par2

from kafe.function_tools import FitFunction, LaTeX, ASCII
from numpy import exp, sqrt, pi
from scipy.special import gamma, wofz

##################################
# Definition of the fit function #
##################################
# Set an ASCII expression for this function
@ASCII(x_name="t", expression="A0*exp(-t/tau)")
# Set some LaTeX-related parameters for this function
@LaTeX(name='A', x_name="t",
   parameter_names=('A_0', '\\tau{}'),
   expression="A_0\\,\\exp(\\frac{-t}{\\tau})")
@FitFunction
def exponential(t, A0=1, tau=1):
   return A0 * exp(-t/tau)


hlines, data1 = ppk.readCSV("Daempfung.csv",nlhead=1)
print(hlines)

time, dF = data1

my_dataset = kafe.Dataset(data=data1,title = "Daempfungskurve",axis_labels=['Zeit t','Winkelgeschwindigkeit'],axis_units=['$min$','$Hz$'])

my_dataset.add_error_source('y','simple',0.01)

#my_dataset=kafe.Dataset(data=data1)

my_fits = [ kafe.Fit(my_dataset, exponential)]

for fit in my_fits:
    fit.do_fit()

my_plot=kafe.Plot(my_fits[0])
my_plot.plot_all()
my_plot.save('kafe_daempfungskurve.pdf')
my_plot.show()




#plt.plot(time,dF,'r+',label = "Messung der Daempfung")
#plt.xlabel("t(min)")
#plt.ylabel("Drehfrequenz(Hz)")
#plt.grid()
#plt.show()




