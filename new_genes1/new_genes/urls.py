<<<<<<< HEAD
"""new_genes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Gene.views import CustomPasswordChangeView

urlpatterns = [
    # admin Url 패턴
    path('admin/', admin.site.urls),

    #Gene applicatiion Url 패턴
    path('', include('Gene.urls')),


    
    # password change Url패턴
    path("password/change/", CustomPasswordChangeView.as_view(), name="account_change_password"),

    path('', include('allauth.urls')),
]

=======
"""new_genes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Gene.views import CustomPasswordChangeView

urlpatterns = [
    # admin Url 패턴
    path('admin/', admin.site.urls),

    #Gene applicatiion Url 패턴
    path('', include('Gene.urls')),


    
    # password change Url패턴
    path("password/change/", CustomPasswordChangeView.as_view(), name="account_change_password"),

    path('', include('allauth.urls')),
]
                        #MEDIA에대한 요청이 들어오면...       MEDIA_ROOT안에 있는 media파일을 돌려주어라...
>>>>>>> 4ca6192e24e793c4a9b51441f48dee89750917f2
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)