import matplotlib.pyplot as plt
import matplotlib
from io import StringIO
import numpy as np

# matplotlib's backend | https://matplotlib.org/stable/users/explain/figure/backends.html
matplotlib.use('agg')

def return_graph():

    x = np.arange(0,np.pi*3,.1)
    y = np.sin(x)

    fig = plt.figure()
    plt.plot(x,y)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data

