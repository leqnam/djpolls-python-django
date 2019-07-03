from django.urls import path
from djpolls import views as djpviews
from django_proj.urls import djpolls_app_name

app_name = djpolls_app_name

urlpatterns = [
    path('', djpviews.home, name='home'),
    path('/<int:question_id>/', djpviews.detail, name='detail'),
    path('/<int:question_id>/vote/', djpviews.vote, name='vote'),
    path('/<int:question_id>/result/', djpviews.results, name='results'),
    
]
