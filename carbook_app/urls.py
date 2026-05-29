from django.urls import path,include
from carbook_app import views

urlpatterns = [

    path('',views.add_booking_view,name='add_booking_view'),
    path('list_booking_view/',views.list_booking_view,name='list_booking_view'),
    path('update_booking_view/<int:id>/',views.update_booking_view,name='update_booking_view'),
    path('delete_booking_view/<int:id>/',views.delete_booking_view,name='delete_booking_view'),

]