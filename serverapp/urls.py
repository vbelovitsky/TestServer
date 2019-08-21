from django.urls import path
from serverapp import views

app_name = "articles"

urlpatterns = [
    path('papers/', views.get_all_papers),  # get all papers
    path('paper/<int:pk>', views.get_paper),   # get paper by id
    path('paper/create', views.create_paper),    # create new paper
    path('paper/update/<int:pk>', views.update_paper),    # update paper by id
    path('paper/delete/<int:pk>', views.delete_paper),    # delete paper by id

]