from django.shortcuts import render, redirect
from django.db.models import Sum  # Import the Sum function from django.db.models
from .models import Member, ExpenseCategory, ExpenseItem, Contribution, ExpenseDetail
from .forms import ContributionForm, ExpenseDetailForm

def home(request):
    return render(request, 'home.html')

def enter_contribution(request):
    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContributionForm()
    return render(request, 'enter_contribution.html', {'form': form})

def enter_expense(request):
    if request.method == 'POST':
        form = ExpenseDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseDetailForm()
    return render(request, 'enter_expense.html', {'form': form})


def summary(request):
    categories = ExpenseCategory.objects.all()
    expenses = ExpenseDetail.objects.all()

    category_summaries = []
    item_summaries = []

    for category in categories:
        category_total = expenses.filter(category=category).aggregate(total=Sum('amount'))['total'] or 0.00
        category_summaries.append((category, category_total))

    for item in ExpenseItem.objects.all():
        item_total = expenses.filter(exitem=item).aggregate(total=Sum('amount'))['total'] or 0.00
        item_summaries.append((item, item_total))

    context = {
        'categories': category_summaries,
        'items': item_summaries,
    }
    return render(request, 'summary.html', context)




def month_wise_audit(request):
    # Get distinct months from the ExpenseItem and Contribution models
    expense_months = ExpenseDetail.objects.dates('date', 'month', order='DESC')
    contribution_months = Contribution.objects.dates('date', 'month', order='DESC')
    months = sorted(set(expense_months) | set(contribution_months), reverse=True)

    # Calculate totals for each month
    month_totals = []
    for month in months:
        expense_total = ExpenseDetail.objects.filter(date__month=month.month, date__year=month.year).aggregate(total=Sum('amount'))['total']
        contribution_total = Contribution.objects.filter(date__month=month.month, date__year=month.year).aggregate(total=Sum('amount'))['total']
        month_totals.append({'month': month, 'expense_total': expense_total or 0, 'contribution_total': contribution_total or 0})

    context = {
        'months': month_totals,
    }
    return render(request, 'month_wise_audit.html', context)

def category_wise_audit(request):
    categories = ExpenseCategory.objects.all()

    # Calculate totals for each category
    category_totals = []
    for category in categories:
        category_total = ExpenseDetail.objects.filter(category=category).aggregate(total=Sum('amount'))['total']
        category_totals.append({'category': category, 'total': category_total or 0})

    context = {
        'category_totals': category_totals,
    }
    return render(request, 'category_wise_audit.html', context)

def item_wise_audit(request):
    expenses = ExpenseDetail.objects.all()

    context = {
        'expenses': expenses,
    }
    return render(request, 'item_wise_audit.html', context)

