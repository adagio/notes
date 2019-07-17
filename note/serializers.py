from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Note
        fields = ('id', 'title', 'description', 'created_at', 'created_by', 'priority')

