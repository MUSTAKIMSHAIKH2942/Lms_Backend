# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import (
#     CustomerViewSet, RoleViewSet, PermissionViewSet, RolePermissionViewSet, UserViewSet,
#     LeadSourceViewSet, LeadStatusViewSet, CategoryViewSet, SubCategoryViewSet, LeadViewSet,
#     TemplateViewSet, MessageViewSet, InteractionViewSet, CustomFieldViewSet, LeadCustomValueViewSet,
#     APITokenViewSet, AuditLogViewSet, ChatbotDataViewSet, ChatbotMetadataViewSet, CommunicationChannelViewSet,
#     CommunicationLogViewSet, SuperAdminDashboardViewSet, ScheduledCommunicationViewSet, ClickTrackingViewSet,
#     ReportViewSet, NotificationViewSet, IntegrationViewSet, WebhookViewSet, AnalyticsViewSet, FeedbackViewSet,
#     SupportTicketViewSet, KnowledgeBaseViewSet, TrainingMaterialViewSet, CertificationViewSet,
#     LearningPathViewSet, LearningPathStepViewSet, UserProgressViewSet, GamificationViewSet, SocialLearningViewSet
# )
from .views import *

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'role-permissions', RolePermissionViewSet)
router.register(r'users', UserViewSet)
router.register(r'lead-sources', LeadSourceViewSet)
router.register(r'lead-statuses', LeadStatusViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)
router.register(r'leads', LeadViewSet)
router.register(r'templates', TemplateViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'interactions', InteractionViewSet)
router.register(r'custom-fields', CustomFieldViewSet)
router.register(r'lead-custom-values', LeadCustomValueViewSet)
router.register(r'api-tokens', APITokenViewSet)
router.register(r'audit-logs', AuditLogViewSet)
router.register(r'chatbot-data', ChatbotDataViewSet)
router.register(r'chatbot-metadata', ChatbotMetadataViewSet)
router.register(r'communication-channels', CommunicationChannelViewSet)
router.register(r'communication-logs', CommunicationLogViewSet)
router.register(r'super-admin-dashboard', SuperAdminDashboardViewSet)
router.register(r'scheduled-communications', ScheduledCommunicationViewSet)
router.register(r'click-tracking', ClickTrackingViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'integrations', IntegrationViewSet)
router.register(r'webhooks', WebhookViewSet)
router.register(r'analytics', AnalyticsViewSet)
router.register(r'feedback', FeedbackViewSet)
router.register(r'support-tickets', SupportTicketViewSet)
router.register(r'knowledge-base', KnowledgeBaseViewSet)
router.register(r'training-materials', TrainingMaterialViewSet)
router.register(r'certifications', CertificationViewSet)
router.register(r'learning-paths', LearningPathViewSet)
router.register(r'learning-path-steps', LearningPathStepViewSet)
router.register(r'user-progress', UserProgressViewSet)
router.register(r'gamification', GamificationViewSet)
router.register(r'social-learning', SocialLearningViewSet)

# from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('', include(router.urls)),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Get JWT token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT token

]
