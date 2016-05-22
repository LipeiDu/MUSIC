#! /usr/bin/env python

import sys
sys.path.insert(
        0, '/Users/chunshen/Dropbox/work_python_scripts/pythonPlotUtilities')

from numpy import *
import matplotlib.pyplot as plt
from os import path
from CSplottools import getPlotElements

plotfontsize = 20
plotLinewidth = 2
plotMarkerSize = 8

# analytic resutls
Analytic_tau1p2 = loadtxt('y=0_tau=1.2_SemiAnalytic.dat')
Analytic_tau1p5 = loadtxt('y=0_tau=1.5_SemiAnalytic.dat')
Analytic_tau2p0 = loadtxt('y=0_tau=2.0_SemiAnalytic.dat')

# numerical simulation resutls
numeric_tau_1p0 = loadtxt('../../Gubser_flow_check_tau_1.dat')
numeric_tau_1p2 = loadtxt('../../Gubser_flow_check_tau_1.2.dat')
numeric_tau_1p5 = loadtxt('../../Gubser_flow_check_tau_1.5.dat')
numeric_tau_2p0 = loadtxt('../../Gubser_flow_check_tau_2.dat')
idx = fabs(numeric_tau_1p2[:, 1]) < 1e-6


fig = plt.figure()
ax = plt.axes([0.14, 0.12, 0.81, 0.83])
iplot = 0

plotlinestyle, plotMarker, plotColor, plotshadowColor = getPlotElements(0)
plt.plot(numeric_tau_1p0[idx, 0], numeric_tau_1p0[idx, 3], color = plotColor,
         linestyle = '-', linewidth = plotLinewidth)
plt.plot(Analytic_tau1p2[:, 0], Analytic_tau1p2[:, 3], color = plotColor,
         linestyle = '-', linewidth = plotLinewidth, alpha = 0.2,
         label = r'$\tau = 1.2$ fm')
plt.plot(numeric_tau_1p2[idx, 0], numeric_tau_1p2[idx, 3], color = plotColor,
         linestyle = '--', linewidth = plotLinewidth)
plotlinestyle, plotMarker, plotColor, plotshadowColor = getPlotElements(1)
plt.plot(Analytic_tau1p5[:, 0], Analytic_tau1p5[:, 3], color = plotColor,
         linestyle = '-', linewidth = plotLinewidth,
         label = r'$\tau = 1.5$ fm')
plt.plot(numeric_tau_1p5[idx, 0], numeric_tau_1p5[idx, 3], color = plotColor,
         linestyle = '--', linewidth = plotLinewidth)
plotlinestyle, plotMarker, plotColor, plotshadowColor = getPlotElements(2)
plt.plot(Analytic_tau2p0[:, 0], Analytic_tau2p0[:, 3], color = plotColor,
         linestyle = '-', linewidth = plotLinewidth,
         label = r'$\tau = 2.0$ fm')
plt.plot(numeric_tau_2p0[idx, 0], numeric_tau_2p0[idx, 3], color = plotColor,
         linestyle = '--', linewidth = plotLinewidth)
         
hl = plt.legend(loc=(2), fontsize = 17)
hl.draw_frame(False)
plt.xlim(-5.0, 5.0)
plt.ylim(-2.0, 2.0)
plt.xticks(linspace(-5.0, 5.0, 5), color = 'k', size = plotfontsize)
plt.yticks(linspace(-2.0, 2.0, 5), color = 'k', size = plotfontsize)
plt.xlabel(r'$x$ (fm)', {'fontsize': plotfontsize})
plt.ylabel(r'$u^x$', fontsize = plotfontsize)
plt.savefig('/Users/chunshen/Desktop/Gubser_ux.pdf', format='pdf')

