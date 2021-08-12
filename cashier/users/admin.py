from django.contrib import admin
from cashier.households.models import HouseholdProfile
from cashier.news.models import News, Comment
from cashier.payments.models import PaymentsAdmin, IndividualPayment, TaxesPerMonth, SalariesPerMonth, \
    IndividualTaxesPayed, SalariesPayment, SalariesPayedPerMonth
from cashier.profiles.models import UserProfile
from cashier.users.models import cashierUser

class CashierUserAdmin(admin.ModelAdmin):
    exclude = ('password','username')

class UserProfileAdmin(admin.ModelAdmin):
    exclude = ('user',)

admin.site.register(cashierUser, CashierUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(HouseholdProfile)
admin.site.register(PaymentsAdmin)
admin.site.register(TaxesPerMonth)
admin.site.register(IndividualPayment)
admin.site.register(IndividualTaxesPayed)
admin.site.register(SalariesPerMonth)
admin.site.register(SalariesPayment)
admin.site.register(SalariesPayedPerMonth)
admin.site.register(News)
admin.site.register(Comment)
