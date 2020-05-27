from rest_framework import serializers, viewsets

from .models import Comments

class CommentsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comments
        fields = ('content')

class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()