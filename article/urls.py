from django.urls import path
from .views import (
        # ArticleFormView, 
        ArticleCreateModelView,
        ArticleCreateView,
        ArticleDeleteView,
        ArticleListView, 
        ArticleDetailView,
        ArticleUpdateModel,
        ArticleUpdateView
    )

app_name = 'article'
urlpatterns = [
    path('<int:page>', ArticleListView.as_view(), name='index'),
    path('detail/<slug:slug>',ArticleDetailView.as_view(), name='detail'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('create-model/', ArticleCreateModelView.as_view(), name='create-model'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('update-model/<int:pk>', ArticleUpdateModel.as_view(), name='update-model'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
]
# pk = primary key (id)