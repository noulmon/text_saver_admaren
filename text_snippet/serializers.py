from django.db import transaction
from rest_framework import serializers

from text_snippet.models import TextSnippet, Tag


class TextSnippetOverviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = TextSnippet
        fields = ('id', 'title', 'url')


class TextSnippetSerializer(serializers.ModelSerializer):
    tag = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    timestamp = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = TextSnippet
        fields = ('id', 'title', 'content', 'created_by', 'tag', 'timestamp')
        read_only_fields = ('id', 'created_by',)

    @transaction.atomic()
    def create(self, validated_data):
        created_by = self.context.get('user')
        tag = (validated_data['tag']).lower()
        # checking whether the tag already exists or not. If tag title does not exits a new tag is created.
        text_tag = Tag.objects.get_or_create(title=tag)[0]
        text_snippet = TextSnippet.objects.create(title=validated_data['title'], content=validated_data['content'],
                                                  created_by=created_by, tag=text_tag)
        return text_snippet

    @transaction.atomic()
    def update(self, instance, validated_data):
        tag = (validated_data.pop('tag')).lower()
        # checking whether the tag already exists or not. If tag title does not exits a new tag is created.
        text_tag = Tag.objects.get_or_create(title=tag)[0]
        instance = TextSnippet.objects.filter(id=instance.id).update(tag=text_tag, **validated_data)
        return instance


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

    def to_representation(self, instance):
        def get_text_snippets():
            '''
            returns all the ACTIVE text snippets related to a particular tag
            '''
            texts = instance.texts.filter(is_deleted=False)
            return TextSnippetSerializer(texts, many=True).data

        return {
            'id': instance.id,
            'text_snippets': get_text_snippets()
        }
