import matplotlib.pyplot as plt
import matplotlib
from io import StringIO
import numpy as np
from .models import Table, Tracker
import locale

# matplotlib's backend | https://matplotlib.org/stable/users/explain/figure/backends.html
matplotlib.use('agg')

locale.setlocale(locale.LC_ALL, 'C')
def format_currency(amount):
    return '${:,.2f}'.format(amount)

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

    sum = 0
    for amount in sizes:
        sum += amount

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Income Distribution - ' + str(format_currency(sum)))
    fig.set_size_inches(7, 7)
    

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    if len(labels) == 0:
        return "No data"
    else:
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

    sum = 0
    for amount in sizes:
        sum += amount

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Expenses Distribution - ' + str(format_currency(sum)))
    fig.set_size_inches(7, 7)
    

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    if len(labels) == 0:
        return "No data"
    else:
        return data