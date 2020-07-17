#pv versus p graph:

from matplotlib import pyplot

pyplot.plot([82,81,80,77.1,77.4,78.9,76],
[1189,1215,1184,1225.89,1354.5,1286.07,1254])

pyplot.title("PV vs P graph of our recent lab experiment")
pyplot.xlabel("P (cmHg)")
pyplot.ylabel("PV (cc x cmHg)")
pyplot.show()