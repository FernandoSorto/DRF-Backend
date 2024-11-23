from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    # DEPRECATED
    path('snippets/', views.snippet_list),
    # DEPRECATED
    path('snippets/<int:pk>', views.snippet_detail),
    # DEPRECATED
    path('snippets2/', views.list_snippets),
    # DEPRECATED
    path('snippets2/<int:pk>/', views.detail_snip),
    # DEPRECATED
    path('snippets3/', views.SnippetList.as_view()),
    # DEPRECATED
    path('snippets3/<int:pk>/', views.SnippetDetail.as_view()),
    # DEPRECATED
    path('snippets4/', views.SnippetList2.as_view()),
    # DEPRECATED
    path('snippets4/<int:pk>/', views.SnippetDetail2.as_view()),



    path('snippets5/', views.SnippetList3.as_view()),
    path('snippets5/<int:pk>/', views.SnippetDetail3.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)