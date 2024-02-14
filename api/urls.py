from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.apps import ApiConfig
from api.views.views_blog import CategoryViewSet, PostViewSet, CommentViewSet, ReviewViewSet
from api.views.views_rh_kosmos import CompanyViewSet, ApplicantViewSet, RHViewSet, VacancyViewSet
from api.views.views_users import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, \
    UserDestroyAPIView

app_name = ApiConfig.name

router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='course')
router.register(r'post', PostViewSet, basename='post')
router.register(r'comment', CommentViewSet, basename='comment')
router.register(r'review', ReviewViewSet, basename='review')

router.register(r'company', CompanyViewSet, basename='company')
router.register(r'applicant', ApplicantViewSet, basename='applicant')
router.register(r'rh', RHViewSet, basename='rh')
router.register(r'vacancy', VacancyViewSet, basename='vacancy')

urlpatterns = [
                  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

                  path('user_create/', UserCreateAPIView.as_view(), name='user_create'),
                  path('user_list/', UserListAPIView.as_view(), name='user_list'),
                  path('user_detail/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_detail'),
                  path('user_update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
                  path('user_delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),
              ] + router.urls
