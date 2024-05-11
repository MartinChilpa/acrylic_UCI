import base64
from rest_framework import serializers, fields
from rest_registration.api.serializers import DefaultUserProfileSerializer, DefaultRegisterUserSerializer
from django.contrib.auth import get_user_model

from artist.models import Artist
from artist.serializers import ArtistSerializer


User = get_user_model()


class UserProfileSerializer(DefaultUserProfileSerializer):
    profile = fields.JSONField(write_only=True, default=dict, initial=dict)

    class Meta:
        model = User

    def get_profile_serializer(self):
        profile = user.get_profile()
        if not profile:
            return None
        profile_model = profile._meta.model.__name__
        profile_mapping = {
            'Artist': ArtistSerializer,
            'Buyer': None,
        }
        return profile_mapping[profile_model]

    def to_representation(self, instance):
        representation = super(UserProfileSerializer, self).to_representation(instance)
        ProfileSerializer = self.get_profile_serializer()
        representation['profile'] = ProfileSerializer(instance.profile, read_only=True).data
        return representation

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        user = super().update(instance, validated_data)
        # update profile
        profile = user.profile
        for attr, value in profile_data.items():
            setattr(profile, attr, value)
        profile.save()
        return user
