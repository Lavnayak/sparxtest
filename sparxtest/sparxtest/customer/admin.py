from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group
from .models import MyUser,TransactionUser
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from actions import export_as_csv_action
from django.utils.html import format_html
from django.conf.urls import url
from django.http import HttpResponseRedirect
# Register your models here.
class MyAdminSite(AdminSite):

    def custom_view(self, request):
        return HttpResponse("Test")

    def get_urls(self):
        from django.conf.urls import url
        urls = super(MyAdminSite, self).get_urls()
        urls += [
            url(r'^custom_view/$', self.admin_view(self.custom_view))
        ]
        return urls

admin_site = MyAdminSite()

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','account_no','is_active','Action')
    list_filter = ('is_active', )
    search_fields = ('account_no', )
    fieldsets = (
      ('Customer Information', {
          'fields': (('first_name','last_name'),('email','account_no'),('is_active','is_staff'))
      }),
      
   	)


    

    def Action(self, obj):
        view = '<a class="button view-icon" title="Enquiry" data-id="%s" href="view/%s/">Enquiry</a>&nbsp;' % (
        obj.id, obj.id)
        return format_html(view)
   	
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            url('^view', self.userDetailView),
        ]
        return my_urls + urls
    def userDetailView(self,request):
    	URL=request.get_full_path()
    	id=URL.split("/")[5]
    	acount_no=MyUser.objects.get(id=id)
    	amounts_w = TransactionUser.objects.filter(account_no=acount_no.account_no,status='Withdraw').values_list('amount', flat=True)
    	amounts_d = TransactionUser.objects.filter(account_no=acount_no.account_no,status='Deposit').values_list('amount', flat=True)
    	total = sum(amounts_d)-sum(amounts_w)
    	messages.error(request, 'Available amount in rupees is '+str(total))
    	return HttpResponseRedirect('/admin/customer/myuser/')
    	
    	



   	# return self.email if self.email else ''
    def get_queryset(self, request):
      qs = super(CustomUserAdmin, self).get_queryset(request)
      return qs.filter(is_superuser=False)
class TransactionUserAdmin(admin.ModelAdmin):
    search_fields = ('account_no', )
    list_display = ('name','account_no','amount','status',)
    
    actions = [export_as_csv_action("CSV Export", fields=['name', 'account_no','amount','status'])]
    
        

    
    fieldsets = (
      ('Payment Section', {
          'fields': (('name','account_no'),('amount','status'),)
      }),
      
   	)

   	# return self.email if self.email else ''
    def save_model(self, request, obj, form, change):
    	if change:
    		obj.save()

    		super(TransactionUserAdmin, self).save_model(request, obj, form, change)
    	if not change:
    		if str(obj.status) == 'Deposit':
    			obj.save()
    			send_mail('Deposit Amount', 'Hello '+str(obj.name)+'.Your transaction with deposit is '+str(obj.amount)+'Rs.', settings.EMAIL_HOST_USER,
			    ['lv.kr56@gmail.com'], fail_silently=False)
    			super(TransactionUserAdmin, self).save_model(request, obj, form, change)
    		if str(obj.status) == 'Withdraw':
    			depo_amt=[]
    			withdraw_amt=[]
    			amounts_w = TransactionUser.objects.filter(account_no=obj.account_no,status='Withdraw').values_list('amount', flat=True)
    			amounts_d = TransactionUser.objects.filter(account_no=obj.account_no,status='Deposit').values_list('amount', flat=True)
    			total = sum(amounts_d)-sum(amounts_w)
    			if total < 1:
    				messages.set_level(request, messages.ERROR)
    				messages.error(request, 'No amount is available for withdraw !')
    			else:
    				obj.save()
    				send_mail('Withdraw Amount', 'Hello '+str(obj.name)+'.Your transaction with withdraw is '+str(obj.amount)+'Rs.', settings.EMAIL_HOST_USER,
			    ['lv.kr56@gmail.com'], fail_silently=False)
    				super(TransactionUserAdmin, self).save_model(request, obj, form, change)
			

			   
    			
      




   	
admin.site.site_header = "Sparx Test"
admin.site.index_title = 'Sparx Test'                 
admin.site.site_title = 'Sparx Test'

admin.site.register(MyUser,CustomUserAdmin)
admin.site.register(TransactionUser,TransactionUserAdmin)
admin.site.unregister(Group)
