from django.urls import path
from . import views





urlpatterns = [
path('AI/',views.admin,name="admin"),
path('addcategory/',views.add_category,name="add_category"),
path('viewcategory/',views.view_category,name="view_category"),
path('addproduct/',views.add_product,name="add_product"),
path('viewproduct/',views.view_product,name="view_product"),
path('productdata/',views.productdata,name="productdata"),
path('categorydata/',views.categorydata,name="categorydata"),
path('viewbookings/',views.view_booking,name="view_booking"),
path('deleteproduct/<int:id>',views.deleteproduct,name="deleteproduct"),
path('editproduct/<int:id>',views.editproduct,name="editproduct"),
path('updateproduct/<int:id>',views.updateproduct,name="updateproduct"),
path('deletecategory/<int:id>',views.deletecategory,name="deletecategory"),
path('editcategory/<int:id>',views.editcategory,name="editcategory"),
path('updatecategory/<int:id>',views.updatecategory,name="updatecategory"),
 path('registerlist/',views.registerlist,name="registerlist"),
 path('viewfeedback/',views.customerlist,name="customerlist"),
  path('complaintlist/',views.complaintlist,name="complaintlist"),
 path('delivered/',views.delivered,name="delivered"),
  path('delivereddata/<int:id>',views.delivereddata,name="delivereddata"),
 path('notdelivered/',views.notdelivered,name="notdelivered"),

]