import matplotlib.pyplot as plt
import matplotlib
from io import StringIO
import numpy as np
from .models import Table, Tracker

# matplotlib's backend | https://matplotlib.org/stable/users/explain/figure/backends.html
matplotlib.use('agg')

def total_income_graph(id):
    labels = []
    sizes = []

    rows = Tracker.objects.filter(id=id)
    for row in rows:
        if row.type == 'Income':
            if row.category in labels:
                index = labels.index(row.category)
                sizes[index] += row.amount
            else:
                labels.append(row.category)
                sizes.append(row.amount)

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels)
    plt.title('Income Distribution')
    fig.set_size_inches(5, 5)
    

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data

def total_expenses_graph(id):
    labels = []
    sizes = []

    rows = Tracker.objects.filter(id=id)
    for row in rows:
        if row.type == 'Expense':
            if row.category in labels:
                index = labels.index(row.category)
                sizes[index] += row.amount
            else:
                labels.append(row.category)
                sizes.append(row.amount)

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels)
    plt.title('Expenses Distribution')
    fig.set_size_inches(5, 5)
    

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data