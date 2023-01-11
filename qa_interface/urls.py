from django.urls import path
from qa_interface.views import detail_view,create_view,dynamic_view,delete_view

app_name='qa'

urlpatterns = [
    
    path("create/", create_view),
    path("elements/", detail_view),
    path("element/<int:id>", dynamic_view, name="qa_entity"),
    path("delete/<int:id>", delete_view),
]