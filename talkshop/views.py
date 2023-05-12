from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from talkshop.serializers import UserSerializer, GroupSerializer, CommentReadSerializer, CommentWriteSerializer, BusinessReadSerializer, BusinessWriteSerializer, CategoryReadSerializer, CategoryWriteSerializer, RegisterUserSerializer
from talkshop.models import Comment, Business, Category
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import RetrieveAPIView, CreateAPIView



class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	permission_classes = [permissions.AllowAny]

	def get_serializer_class(self):
		if self.request.method == 'PUT' or self.request.method == 'POST':
			return CommentWriteSerializer
		else:
			return CommentReadSerializer

class BusinessViewSet(viewsets.ModelViewSet):
	queryset = Business.objects.all()
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def get_serializer_class(self):
		if self.request.method == 'PUT' or self.request.method == 'POST':
			return BusinessWriteSerializer
		else:
			return BusinessReadSerializer

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['slug']

	def get_serializer_class(self):
		if self.request.method == 'PUT' or self.request.method == 'POST':
			return CategoryWriteSerializer
		else:
			return CategoryReadSerializer

class UserAPIView(RetrieveAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = UserSerializer

	def get_object(self):
		return self.request.user

class RegisterUserAPIView(CreateAPIView):
	permission_classes = [permissions.AllowAny]
	serializer_class = RegisterUserSerializer