from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Table, Tracker

def home(request):
    return render(request, 'home.html')

def tables(request):
    if request.method == 'POST':
        new_table = Table()
        new_table.user = request.POST.get('username')
        new_table.table_name = request.POST.get('table_name')
        new_table.save()
        return redirect('/tables')
    else:
        table = Table()

    tables = {
        'tables': Table.objects.all()
    }

    return render(request, 'tables.html', tables)   

def delete_tables(request):
    Table.objects.all().delete()
    return redirect('/tables') 

def delete_line(request):
    try:
        line_id = request.POST.get('line_id')
        row = get_object_or_404(Table, pk=line_id)
        row.delete()
        delete_line_message = "Line deleted."
    except:
        delete_line_message = "Enter a valid line id."
        print('error')

    return render(request, 'tables.html', {'tables': Table.objects.all(), 'error_message': delete_line_message})
    #return redirect('/tables', error_message)
    
def table(request, id):
    
    main_row = get_object_or_404(Table, pk=id)
    user = main_row.user
    table_name = main_row.table_name

    return render(request, 'table_data.html', {
        'id': id,
        'user': user,
        'table_name': table_name
        })
