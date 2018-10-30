from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

#分类___________________________________________________________________________________________________________________
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        medle = Category
        fields = '__all__'


class CategoryStringSerializer(serializers.ModelSerializer):
    # 用__str__方法表示只读关系 items 为外键关系中的related_name
    items = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        #fields = ('id','title','items')
        fields = '__all__'


class CategoryPrimaryKeySerializer(serializers.ModelSerializer):
    # 用主键表示关系
    items = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    class Meta:
        model = Category
        # fields = ('id','title','items.id')
        fields = '__all__'

class CategorySlugSerializer(serializers.ModelSerializer):
    # 选取关系对象中任意一个字段（唯一标识）表示关系
    items = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')

    class Meta:
        model = Category
        # fields = ('id','title','items.title')
        fields = '__all__'

#子栏目_________________________________________________________________________________________________________________
class ItemSerializer(serializers.ModelSerializer):
    categorys = CategorySerializer()

    class Meta:
        model = Item
        fields = '__all__'