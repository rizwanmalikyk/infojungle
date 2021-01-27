from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from post.views import (
    index, blog, post, search, IndexView, privacypolicy, blogprivacypolicy,
    post_create, post_update, post_delete, PostDetailView,)
from marketing.views import email_list_signup

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('', index),
    path('', IndexView.as_view(), name='home'),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='search'),
    path('privacypolicy/', privacypolicy, name='privacypolicy'),
    path('blog/privacypolicy/', blogprivacypolicy, name='blogprivacypolicy'),
    path('email-signup/', email_list_signup, name='email-list-signup'),
    path('create/', post_create, name='post-create'),
    path('post/<id>/', post, name='post-detail'),
    #path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),

    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, 
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)
                         
