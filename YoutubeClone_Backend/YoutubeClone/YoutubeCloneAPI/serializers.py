from rest_framework import fields, serializers
from .models import Comment, Reply

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'likes', 'dislikes', 'video']

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('comment', instance.comment)
        instance.likes = validated_data.get('likes', instance.likes)
        instance.dislikes = validated_data.get('dislikes', instance.dislikes)
        instance.video = validated_data.get('video', instance.video)
        
        instance.save()
        return instance

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'reply', 'comment']
    
    def create(self, validated_data):
        return Reply.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.reply = validated_data.get('reply', instance.reply)
        instance.comment = validated_data.get('comment', instance.comments)