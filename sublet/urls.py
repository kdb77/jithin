from django.urls import path
from .import views
app_name='sublet'
urlpatterns = [
    path('',views.allProdCats,name='allProdCats'),
    path('<slug:c_slug>/',views.allProdCats,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatdetail'),
]
