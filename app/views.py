from django.shortcuts import render
import csv

def inflation_view(request):
    template_name = 'inflation.html'
    with open('inflation_russia.csv') as data:
        reader = csv.DictReader(data)
        inflation_list = []
        headers = []
        for row in reader:
            for key, value in row.items():
                if 'Суммарная' not in headers:
                    headers.append(key)
                if value == '':
                    row[key] = '-'
                else:
                    if type(value) is str and key != 'Год':
                        row[key] = float(value)
            inflation_list.append(row)
    # чтение csv-файла и заполнение контекста
    context = {
        'inflation': inflation_list,
        'headers': headers
    }

    return render(request, template_name,
                  context)