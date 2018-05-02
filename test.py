from elpigraph import computeElasticPrincipalCurve
from elpigraph import PlotPG
import numpy as np

curve_data = np.genfromtxt('elpigraph/data/curve_data.csv', delimiter=',')
EPCurve = computeElasticPrincipalCurve(curve_data, 10)

print(curve_data)

PlotPG(curve_data,EPCurve)