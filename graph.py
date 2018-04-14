import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

def chartGen(csvFile, graphTitle, xAxisLabel, yAxisLabel):
    style.use("ggplot")

    x,y = np.loadtxt(csvFile, dtype="str",unpack=True, delimiter=",")

    x = x.astype(str)
    y = y.astype(int)

    graph= plt.figure()

    plt.scatter(x,y)

    plt.ylim(0,50)
    plt.title(graphTitle)
    plt.xlabel(xAxisLabel)
    plt.xticks(rotation=90)
    plt.ylabel(yAxisLabel)

    graph.savefig("./files/graphs/chart.pdf", bbox_inches="tight")
