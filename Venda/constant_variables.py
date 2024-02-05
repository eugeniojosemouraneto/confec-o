from Venda.models import *
from datetime import date
from Venda.forms import *

def format_accurately_list(*values):
    return [
        float(f"{val:.2f}") for val in values
    ]

def table_values(sales, sale_value = 0.00, total_net_profit = 0.00, weave = 0.00, close = 0.00, fill = 0.00, embroider = 0.00, line = 0.00, box = 0.00, total = 0.00):

    for s in sales:

        total_net_profit += s.netProfit
        sale_value += s.grossProfit
        weave += s.spentWeaving
        close += s.spentClose
        fill += s.spentFiling
        embroider += s.spentEmbroider
        line += s.spentLine
        box += s.spentBox
        total += s.totalCost

    return format_accurately_list(total_net_profit, sale_value, weave, close, fill, embroider, line, box, total)


def profit_expense_six_months(current_month, current_year):

    list_month = []

    profit = []

    expense = []

    for i in range(6):
        
        current_month -=1

        if(current_month <= 0):
        
            current_month = 12

            current_year -= 1
        
    current_month += 1

    for i in range(6):

        list_month.append(months[current_month])

        assistant = Sale.objects.all().filter(month = current_month, year = current_year)

        prof = 0.00

        exp = 0.00

        for aux in assistant:

            prof += aux.netProfit

            exp += aux.totalCost

        profit.append(float(f'{prof:.2f}'))

        expense.append(float(f'{exp:.2f}'))
        
        current_month += 1

        if(current_month > 12):
        
            current_month = 1

            current_year += 1
    
    current_month -= 1

    print(profit, expense)

    return list_month, profit, expense


categories = "id", "Produto", 'Unidades', 'Lucro Bruto', 'Tescer', 'Fechar', 'Encher', 'Bordar', 'Linha', 'Caixinha', 'Gasto total', 'Lucro liquido'

data = date.today()

current_month = data.month
current_year = data.year

months = {
    1 : 'Jan',
    2 : 'Fev',
    3 : 'Mar',
    4 : 'Abr',
    5 : 'Mai',
    6 : 'Jun',
    7 : 'Jul',
    8 : 'Ago',
    9 : 'Out',
    10 : 'Set',
    11 : 'Nov',
    12 : 'Dez'
}