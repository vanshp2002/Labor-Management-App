
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name="index"),
    path('showDetails',views.showDetails, name="showDetails"),
    path('showRunQuery',views.showRunQuery,name = "showRunQuery"),
    path('RunQuery',views.RunQuery,name = "RunQuery"),
    path('insertLaborer',views.insertLaborer,name = "insertLaborer"),
    path('sortLaborer',views.sortLaborer,name="sortLaborer"),
    path('editLaborer/<int:id>',views.editLaborer,name="editLaborer"),
    path('updateLaborer/<int:id>',views.updateLaborer,name="updateLaborer"),
    path('delLaborer/<int:id>',views.delLaborer,name="delLaborer"),
    path('deletedLaborer/<int:id>',views.deletedLaborer,name="deletedLaborer"),

]
