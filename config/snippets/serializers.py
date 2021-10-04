from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

#TODO Serializers.py 에는 항상 create와 update 메소드가 있어야 한다.
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template' : 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default="python")
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default="friendly")

#     def create(self, validated_data):
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         #get(A, B) => A 에 해당하는 값이 없으면 B를 고른다.
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance



#ModelSerializer 사용하면 자동으로 만들어줌
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Snippet

        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']


class UserSerializer(serializers.ModelSerializer):
    
    # Snippets 는 User모델과 reverse 관계이므로 자동으로 include 되지 않음. 
    # Snippets 에서는 Owner이 있는데, Owner에는 Snippet이 꼭 생길지 않음.

    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']

