from django.urls import path

from blog.apps import BlogConfig
from blog.views import ContactView, BlogListView, BlogDetail, BlogCreate, BlogUpdate, BlogDelete

app_name = BlogConfig.name


urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('blog/', BlogListView.as_view(), name='article_list'),
    path('blog/<int:pk>/', BlogDetail.as_view(), name='article_detail'),
    path('blog/<int:pk>/update', BlogUpdate.as_view(), name='article_update'),
    path('blog/create/', BlogCreate.as_view(), name='article_create'),
    path('blog/<int:pk>/delete', BlogDelete.as_view(), name='article_delete')
]