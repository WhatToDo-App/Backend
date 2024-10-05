from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet, TaskListCreateView, TaskRetrieveUpdateDestroyView

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task-list'),  # Optional if you want a landing page
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include the router's URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]