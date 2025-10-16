from django import forms
from django.core.exceptions import ValidationError
from django.forms import CheckboxInput
from PIL import Image

from .models import Product

EXCLUDE_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]
MAX_SIZE_MB = 4
max_size_bytes = MAX_SIZE_MB * 1024 * 1024


class StyleFormMixin:
    """Класс для стилизации форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            existing = field.widget.attrs.get("class", "")
            if isinstance(field, forms.BooleanField) or isinstance(field.widget, CheckboxInput):
                field.widget.attrs["class"] = (existing + " form-check-input").strip()
            else:
                field.widget.attrs["class"] = (existing + " form-control").strip()


class ProductForm(StyleFormMixin, forms.ModelForm):
    """Класс для создания и изменения товара"""

    class Meta:
        model = Product
        exclude = (
            "created_at",
            "updated_at",
            "owner",
        )

    def clean_price(self):
        """Метод валидации цены - не может быть отрицательной"""
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

    def clean_photo(self):
        """Метод валидации фото - соответствие размеру и формату"""
        photo = self.cleaned_data.get("photo")
        if not photo:
            return photo

        if photo.size > max_size_bytes:
            raise ValidationError(f"Размер файла не должен превышать {MAX_SIZE_MB} МБ.")

        try:
            photo.seek(0)
            image = Image.open(photo)
            image_format = image.format.upper()  # Убедитесь, что формат в верхнем регистре для сравнения
            if image_format not in ["JPEG", "PNG"]:
                raise ValidationError("Фото неправильного формата. Допустимые форматы: JPEG, PNG.")
            photo.seek(0)

        except Exception as e:
            raise ValidationError(f"Ошибка при обработке изображения: {e}")
        return photo

    def clean(self):
        """Метод валидации товара с исключением запрещенных слов"""
        cleaned_data = super().clean()
        name = cleaned_data.get("name").lower().split()
        description = cleaned_data.get("description").lower().split()

        for word in name:
            if word in EXCLUDE_WORDS:
                self.add_error("name", "Название продукта содержит запрещенные слова")
        for word in description:
            if word in EXCLUDE_WORDS:
                self.add_error("description", "Описание продукта содержит запрещенные слова")


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    """Класс для редактирования модератором"""

    class Meta:
        model = Product
        fields = ("is_published",)
