from django.forms import ModelForm

from .models import Group, Shirt


class GroupForm(ModelForm):
      class Meta:
            model = Group
            fields = ['name']


class ShirtForm(ModelForm):
	class Meta:
		model = Shirt
		fields = [
            'title',
            'group',
            'is_group_title',
            'price',
            'color',
            'material',
            'size',
            'description',
            'image'
		]
