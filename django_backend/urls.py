from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from grades.views import StudentViewSet, SubjectViewSet, GradeViewSet

router = DefaultRouter()
router.register(r'stu', StudentViewSet)
router.register(r'sub', SubjectViewSet)
router.register(r'gra', GradeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] 