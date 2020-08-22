from django.urls import path
from . import views

urlpatterns = [
    path('process_barcode/<int:pk>', views.process_barcode),
    path('join_shower_queue/<int:pk>/lounge/<int:lounge_id>', views.join_shower_queue),
    path('check_out_lounge/<int:pk>', views.check_out_lounge),
    path('check_out_shower/<int:pk>/lounge/<int:lounge_id>', views.check_out_shower),
]