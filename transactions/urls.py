"""codelnmain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from transactions.views import process_transaction, transaction, all_candidates, my_invites, sourcing

app_name = 'transactions'

urlpatterns = [
    # path('', project_categories, name='categories'),
    path('transaction/<int:id>', transaction, name='transaction'),
    path('process_transaction/<int:id>/', process_transaction, name='process_transaction'),
    path('my-invites/', my_invites, name='my-invites'),
    path('sourcing/', sourcing, name='sourcing'),
]
