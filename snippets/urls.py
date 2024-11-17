from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>', views.snippet_detail),
    path('snippets2/', views.list_snippets),
    path('snippets2/<int:pk>/', views.detail_snip),
]

urlpatterns = format_suffix_patterns(urlpatterns)