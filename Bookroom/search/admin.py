from django.contrib import admin
from search.models import RegUser,Author,Publisher,Book
# Register your models here.
# from huanji_model import TBreplace,TBReplaceMachine


class RegUser_admin(admin.ModelAdmin):
    list_display = ('username','last_name','first_name','email','phone_number',)
    search_fields = ('username','phone_number',)
admin.site.register(RegUser,RegUser_admin)


class Book_admin(admin.ModelAdmin):
    list_display = ('title','tab','author','update_time',)
    search_fields =  ('title',)

admin.site.register(Book,Book_admin)

class Author_admin(admin.ModelAdmin):
    list_display = ('last_name','first_name',)

admin.site.register(Author,Author_admin)


class Publsher_admin(admin.ModelAdmin):
    list_display = ('publisher',)

admin.site.register(Publisher,Publsher_admin)


# class TBReplaceMachine_stackinline(admin.StackedInline):
#     model = TBReplaceMachine
#
# class TBReplaceMachine_admin(admin.ModelAdmin):
#     list_display = ('machine','machine_model','machine_sn','replace',)
#     search_fields = ('machine_sn',)
# admin.site.register(TBReplaceMachine,TBReplaceMachine_admin)
#
#class TBrepalce_admin(admin.ModelAdmin):
#    list_display = ('order','date','region','seller','express',,'sender','mobile','address','machine_model','machine','machine_sn','sender_data','amount','prePrice','TotalPrice','Feedback','note','created_time','modified_time')
#    search_fields = ('order',)
#
#admin.site.register(TBreplace,TBrepalce_admin)






