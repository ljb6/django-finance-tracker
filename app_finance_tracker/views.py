from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Table, Tracker

import locale
from datetime import datetime
from .graphs import total_income_graph, total_expenses_graph

locale.setlocale(locale.LC_ALL, 'C')
def format_currency(amount):
    return '${:,.2f}'.format(amount)

def home(request):
    return render(request, "home.html")


def tables(request):
    if request.method == "POST":
        new_table = Table()
        new_table.user = request.POST.get("username")
        new_table.table_name = request.POST.get("table_name")
        new_table.save()
        return redirect("/tables")
    else:
        table = Table()

    tables = {"tables": Table.objects.all()}

    return render(request, "tables.html", tables)


def delete_tables(request):
    Table.objects.all().delete()
    Tracker.objects.all().delete()
    return redirect("/tables")


def delete_line(request):
    try:
        line_id = request.POST.get("line_id")
        row = get_object_or_404(Table, pk=line_id)
        row.delete()
        delete_line_message = "Line deleted."
    except:
        delete_line_message = "Enter a valid line id."
        print("error")

    return render(
        request,
        "tables.html",
        {"tables": Table.objects.all(), "error_message": delete_line_message},
    )


def table(request, id):

    main_row = get_object_or_404(Table, pk=id)
    user = main_row.user
    table_name = main_row.table_name

    total_income = 0
    total_expenses = 0

    try:
        extract = Tracker.objects.filter(id=id)
        print("success")

        for row in extract:
            if row.type == "Income":
                total_income += row.amount
            else:
                total_expenses += row.amount
    except:
        print("error")

    income_graph = total_income_graph(id)
    expenses_graph = total_expenses_graph(id)

    current_money = total_income - total_expenses

    return render(
        request,
        "table_data.html",
        {
            "id": id,
            "user": user,
            "table_name": table_name,
            "total_income": format_currency(total_income),
            "total_expenses": format_currency(total_expenses),
            "current_money": format_currency(current_money),
            "extract": extract,
            "income_graph": income_graph,
            "expenses_graph": expenses_graph
        },
    )


def add_transaction(request):
    id = request.POST.get("id")

    new_transaction = Tracker()
    new_transaction.id = id
    new_transaction.date = datetime.now()
    new_transaction.type = request.POST.get("type")
    new_transaction.category = request.POST.get("category")
    new_transaction.description = request.POST.get("description")
    new_transaction.amount = request.POST.get("amount")
    new_transaction.save()

    return redirect("/table/" + str(id))


def clear_transactions(request):
    id = request.POST.get("id")
    rows = Tracker.objects.filter(id=id)
    for row in rows:
        row.delete()

    return redirect("/table/" + str(id))


