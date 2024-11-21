from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>', views.snippet_detail),
    path('snippets2/', views.list_snippets),
    path('snippets2/<int:pk>/', views.detail_snip),
    path('snippets3/', views.SnippetList.as_view()),
    path('snippets3/<int:pk>/', views.SnippetDetail.as_view()),
    path('snippets4/', views.SnippetList2.as_view()),
    path('snippets4/<int:pk>/', views.SnippetDetail2.as_view()),
    path('snippets5/', views.SnippetList3.as_view()),
    path('snippets5/<int:pk>/', views.SnippetDetail3.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)