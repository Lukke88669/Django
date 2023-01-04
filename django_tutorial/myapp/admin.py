from django.contrib import admin
# from myapp.models import product
from myapp import models

# 第一種方式，未加入 ModelAdmin 類別
# admin.site.register(student)

# 第二種方式，加入 ModelAdmin 類別，定義顯示欄位
# class studentAdmin(admin.ModelAdmin):
# 	list_display=('id','cName','cSex','cBirthday','cEmail','cPhone','cAddr')
# admin.site.register(student,studentAdmin)

# 第三種方式，加入 ModelAdmin 類別，定義顯示欄位、欄位過濾資料、搜尋和排序

class productAdmin(admin.ModelAdmin):
	admin.site.register(models.ProductModel)
	admin.site.register(models.OrdersModel)
	admin.site.register(models.DetailModel)
	admin.site.register(models.MiceModel)
	admin.site.register(models.HeadestModel)

# 	list_display = ('product_Name', 'product_Price')
# admin.site.register(product,productAdmin)


