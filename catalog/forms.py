from django import forms
from django.core.exceptions import ValidationError
from django.forms import BooleanField

from .models import Product

EXCLUDE_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
MAX_SIZE_MB = 4
max_size_bytes = MAX_SIZE_MB * 1024 * 1024


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if not photo:
            return photo

        if photo.size > max_size_bytes:
            raise ValidationError(f'Размер файла не должен превышать {MAX_SIZE_MB} МБ.')

        if photo.format not in ['JPEG', 'PNG']:
            raise ValidationError('Фото неправильного формата')
        return photo

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name').lower().split()
        description = cleaned_data.get('description').lower().split()

        for word in name:
            if word in EXCLUDE_WORDS:
                self.add_error('name', 'Название продукта содержит запрещенные слова')
        for word in description:
            if word in EXCLUDE_WORDS:
                self.add_error('description', 'Описание продукта содержит запрещенные слова')