from rest_framework import serializers
from .models import *


class SnippetoverviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet
        fields = ['url','snippet']


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['url','tag_id', 'title']

class SnippetPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet
        fields = ['url','snip_id','title','snippet','time_stamp']


    def create(self, validated_data):
        print(validated_data)
        title = validated_data['title']
        is_title = Tag.objects.filter(title=title).first()
        print(is_title)
        if is_title:
            validated_data['tag'] = is_title
        else:
            tag_id = Tag.objects.create(title=validated_data['title'])
            print(tag_id)
            validated_data['tag'] = tag_id
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.snippet = validated_data.get('snippet', instance.snippet)
        instance.save()
        return instance