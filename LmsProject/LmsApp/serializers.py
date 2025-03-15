# serializers.py
from rest_framework import serializers
from .models import (
    Customer, Role, Permission, RolePermission, User, LeadSource, LeadStatus, Category,
    SubCategory, Lead, Template, Message, Interaction, CustomField, LeadCustomValue,
    APIToken, AuditLog, ChatbotData, ChatbotMetadata, CommunicationChannel, CommunicationLog,
    SuperAdminDashboard, ScheduledCommunication, ClickTracking, Report, Notification,
    Integration, Webhook, Analytics, Feedback, SupportTicket, KnowledgeBase, TrainingMaterial,
    Certification, LearningPath, LearningPathStep, UserProgress, Gamification, SocialLearning
)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LeadSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadSource
        fields = '__all__'

class LeadStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadStatus
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = '__all__'

class CustomFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomField
        fields = '__all__'

class LeadCustomValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadCustomValue
        fields = '__all__'

class APITokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIToken
        fields = '__all__'

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'

class ChatbotDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatbotData
        fields = '__all__'

class ChatbotMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatbotMetadata
        fields = '__all__'

class CommunicationChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationChannel
        fields = '__all__'

class CommunicationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationLog
        fields = '__all__'

class SuperAdminDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperAdminDashboard
        fields = '__all__'

class ScheduledCommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledCommunication
        fields = '__all__'

class ClickTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClickTracking
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class IntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integration
        fields = '__all__'

class WebhookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webhook
        fields = '__all__'

class AnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analytics
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class SupportTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportTicket
        fields = '__all__'

class KnowledgeBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeBase
        fields = '__all__'

class TrainingMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingMaterial
        fields = '__all__'

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

class LearningPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningPath
        fields = '__all__'

class LearningPathStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningPathStep
        fields = '__all__'

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = '__all__'

class GamificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamification
        fields = '__all__'

class SocialLearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLearning
        fields = '__all__'