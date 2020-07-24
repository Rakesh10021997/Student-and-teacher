from django.urls import *
from django.conf.urls import url,include
from . import views
from Volsko.settings import DEBUG, STATIC_URL, STATIC_DIR, MEDIA_DIR, MEDIA_URL
from django.conf.urls.static import static


urlpatterns = [
    url('', views.home, name='home'),
    url('books/',views.index, name='books'),
    url('upload/', views.upload, name = 'upload-book'),
    url('books/update/<int:book_id>', views.update_book),
    url('books/delete/<int:book_id>', views.delete_book),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_DIR)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_DIR)
