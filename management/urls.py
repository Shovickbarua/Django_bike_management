"""
URL configuration for management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Authentication import views as authenticate
from Bike import views as bike
from Bikesale import views as bikesale
from Bikeservice import views as bikeservice
from Category import views as category
from Income import views as income
from Expense import views as expense
from Product import views as product
from Sale import views as productsale


urlpatterns = [

    #authentication
    path('', authenticate.loginpage,name='loginpage'),
    path('sign_in', authenticate.sign_in,name='sign_in'),
    path('logout', authenticate.signout,name='signout'),

    path('dash/',category.dash,name='dash'),
    path('admin/', admin.site.urls),
    
    #catergory
    path('add_cat/', category.add,name='add_cat'),
    path('add_cat/store', category.store,name='cat_store'),
    path('cat_list/', category.index,name='cat_list'),
    path('cat_edit/<id>', category.edit,name='cat_edit'),
    path('cat_update/<id>', category.update,name='cat_update'),
    path('cat_delete/<id>', category.delete,name='cat_delete'),
    
    #product  
    path('add_pro/', product.add,name='add_pro'),
    path('add_pro/store', product.store,name='pro_store'),
    path('pro_list/', product.index,name='pro_list'),
    path('pro_edit/<id>', product.edit,name='pro_edit'),
    path('pro_update/<id>', product.update,name='pro_update'),
    path('pro_delete/<id>', product.delete,name='pro_delete'),
    
    #productsale  
    path('add_sale/<id>', productsale.add,name='add_sale'),
    path('add_prosale/store/<id>', productsale.sale_store,name='sale_store'),
    path('add_prosale/store/show', productsale.show_sale,name='show_sale'),
    path('sale_list/', productsale.index,name='sale_list'),

    
    #bike
    path('add_bike/', bike.add,name='add_bike'),
    path('add_bike/store', bike.store,name='bike_store'),
    path('bike_list/', bike.index,name='bike_list'),
    path('bike_edit/<id>', bike.edit,name='bike_edit'),
    path('bike_update/<id>', bike.update,name='bike_update'),
    path('bike_delete/<id>', bike.delete,name='bike_delete'),
    
    #bikesale
    path('add_bikesale/<id>', bikesale.add,name='add_bikesale'),
    path('add_bikesale/store/<id>', bikesale.store,name='bikesale_store'),
    path('bikesale_list/', bikesale.index,name='bikesale_list'),
    path('bikesale_edit/<id>', bikesale.edit,name='bikesale_edit'),
    path('bikesale_update/<id>', bikesale.update,name='bikesale_update'),
    path('bikesale_delete/<id>', bikesale.delete,name='bikesale_delete'),
    
    #Expense
    path('add_ex/', expense.add,name='add_ex'),
    path('add_ex/store', expense.store,name='ex_store'),
    path('ex_list/', expense.index,name='ex_list'),
    path('ex_edit/<id>', expense.edit,name='ex_edit'),
    path('ex_update/<id>', expense.update,name='ex_update'),
    path('ex_delete/<id>', expense.delete,name='ex_delete'), 
    path('search/', expense.search,name='search_ex'), 
    
    #Income
    path('add_in/', income.add,name='add_in'),
    path('add_in/store', income.store,name='in_store'),
    path('in_list/', income.index,name='in_list'),
    path('in_edit/<id>', income.edit,name='in_edit'),
    path('in_update/<id>', income.update,name='in_update'),
    path('in_delete/<id>', income.delete,name='in_delete'),
    path('search_income/', income.search,name='search_in'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
