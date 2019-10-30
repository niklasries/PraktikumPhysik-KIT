# -*- coding: iso-8859-15 -*-
import kafe
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


# Initialize the Dataset and load data from a file
my_dataset = kafe.Dataset(title="Example dataset",
                          axis_labels=['t', 'A'])
my_dataset.read_from_file(input_file='dataset.dat')

# Perform a Fit
my_fit = Fit(my_dataset, exponential)
my_fit.do_fit()

# Plot the results
my_plot = Plot(my_fit)
my_plot.plot_all()


# Create plots of the contours and profile chi-squared
contour = my_fit.plot_contour(0, 1, dchi2=[1.0, 2.3])
profile1 = my_fit.plot_profile(0)
profile2 = my_fit.plot_profile(1)

# Show the plots
my_plot.show()
