from django.forms import ModelForm
from food.models import Food


class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'recipe','description','image','is_nonveg','is_veg']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mt-1'}
        )
        self.fields['recipe'].widget.attrs.update(
            {'class': 'form-control mt-1'}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control mt-1'}
        )
        self.fields['image'].widget.attrs.update(
            {'class': 'form-control mt-1'}
        )
        self.fields['is_nonveg'].widget.attrs.update(
            {'class': 'form-control mt-1'}
        )
        self.fields['is_veg'].widget.attrs.update(
            {'class': 'form-control mt-1'}
        )

