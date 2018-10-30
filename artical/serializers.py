from .models import *
from rest_framework import serializers
from rest_framework.validators import UniqueValidator,UniqueTogetherValidator


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


#标签
class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100,required=True)
    slug = serializers.CharField(max_length=100,required=True)

    class Meta:
        model = Tag
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class ArticalSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    item = ItemSerializer()
    Tag = TagSerializer

    class Meta:
        model = Artical
        fields = '__all__'


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = UserFav
        validators = [
            UniqueTogetherValidator(
                queryset= UserFav.objects.all(),
                fields = ('articals','user'),
                message = '已经收藏'
            )
        ]
        fields = ('user','articals','id')