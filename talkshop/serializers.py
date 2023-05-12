from django.contrib.auth.models import User, Group
from rest_framework import serializers
from talkshop.models import Comment, Business, Category

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'username', 'email', 'groups']

class RegisterUserSerializer(serializers.HyperlinkedModelSerializer):
	def create(self, validated_data):
		user = User.objects.create_user(
			email=validated_data['email'],
			username = validated_data['username'],
			password = validated_data['password']
		)

		return user

	class Meta:
		model = User
		fields = ['url', 'username', 'password', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ['url', 'name']

class CommentReadSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		depth = 1
		fields = '__all__'

class CommentWriteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = ['url', 'content', 'business']

class BusinessReadSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Business
		depth = 1
		fields = [
			'url',
			'title',
			'slug',
			'description',
			'tag',
			'street_address',
			'city',
			'region',
			'postal_code',
			'country',
			'website',
			'infosource',
			'hours',
			'comments',
		]

class BusinessWriteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Business
		fields = [
			'url',
			'title',
			'slug',
			'description',
			'tag',
			'street_address',
			'city',
			'region',
			'postal_code',
			'country',
			'website',
			'infosource',
			'hours',
			'comments',
		]

class CategoryReadSerializer(serializers.HyperlinkedModelSerializer):
	business = BusinessReadSerializer(many=True)
	class Meta:
		model = Category
		depth = 1
		fields = [
			'url',
			'name',
			'slug',
			'ordinal',
			'business'
		]

class CategoryWriteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = [
			'url',
			'name',
			'slug',
			'ordinal',
			'business'
		]