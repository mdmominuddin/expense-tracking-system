from django.contrib import admin
from .models import Member, ExpenseCategory, ExpenseItem, Contribution, ExpenseDetail
ExpenseItem


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info')

@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ExpenseItem)
class ExpenseItemAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('date', 'member', 'amount')
    list_filter = ('member',)
    search_fields = ('member__name',)

@admin.register(ExpenseDetail)
class SocietyBalanceAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'amount', 'category')
    list_filter = ('category',)
    list_filter = ('exitem',)
    search_fields = ('ExpenseDetail__exitem',)

admin.site.site_header = "Swapnoneer Society Admin"
admin.site.site_title = "Swapnoneer Society"
admin.site.index_title = "Welcome to Swapnoneer Society Administration"

