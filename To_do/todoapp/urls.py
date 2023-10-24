from django.urls import path
from todoapp import views

urlpatterns= [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('clvhome/',views.TaskListview.as_view(),name='clvhome'),
    path('cdvdetail/<int:pk>/',views.DetailListview.as_view(),name='cdvdetail'),
    path('cdvupdate/<int:pk>/',views.TaskUpdate.as_view(),name='cdvupdate'),
    path('cdvdelete/<int:pk>/',views.TaskDelete.as_view(),name='cdvdelete'),
    path('scraper/',views.web_scrap,name='scraper'),
]