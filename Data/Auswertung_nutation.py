# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import PhyPraKit as ppk
import kafe

from kafe.function_library import linear_2par

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


hlines, data1 = ppk.readCSV("Nutationsfrequenz_ohneGewicht.csv",nlhead=1)
print(hlines)

hlines2, data2 = ppk.readCSV("Nutationsfrequenz_mitGewicht.csv",nlhead=1)

time1, dF1 = data1
time2,dF2 = data2


my_dataset= [kafe.Dataset(data=data1,title="Nutation ohne Gewicht",axis_label=['Drehfrequenz','Nutationsfrequenz'],data_label=" ohne Gewicht"),
             kafe.Dataset(data=data2,title="Nutation mit Gewicht",data_label="mit Gewicht")]

my_dataset[0].add_error_source('y','simple',0.01)
my_dataset[0].add_error_source('x','simple',0.01)


my_dataset[1].add_error_source('y','simple',0.01)
my_dataset[1].add_error_source('x','simple',0.01)


#my_dataset[0]=kafe.Dataset(data=data1)
#my_dataset[1]=kafe.Dataset(data=data2)

#my_dataset.add_error_source()


my_fits = [kafe.Fit(dataset,
                    linear_2par,
                    fit_label="Linear regression")
           for dataset in my_dataset]

for fit in my_fits:
    fit.do_fit()

my_plot=kafe.Plot(my_fits[0],my_fits[1])
my_plot.axis_labels = ['Drehfrequenz$[Hz]$', 'Nutationsfrequenz$[Hz]$']
my_plot.axis_units=['$Hz$','$Hz$']
my_plot.plot_all()

my_plot.save('kafe_nutation.pdf')
my_plot.show()




#plt.plot(time1,dF1,'r+',label = "Messung der Nutations")
#plt.plot(time2,dF2,'b+')
#plt.xlabel("Drehfrequenz(Hz)")
#plt.ylabel("Nutationsfrequenz(Hz)")
#plt.grid()
#plt.show()



