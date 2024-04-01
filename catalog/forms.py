from django import forms
from django.forms import BaseInlineFormSet
from django.forms.fields import BooleanField
from catalog.models import Product, Version


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
        exclude = ('created_at', 'updated_at', )

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError("Один или несколько запрещенных терминов обнаружены в названии товара")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError("Один или несколько запрещенных терминов обнаружены в описании товара")
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'


class VersionFormSet(BaseInlineFormSet):
    """ VersionForm set"""
    def clean(self):
        super().clean()

        active_versions = [form.cleaned_data for form in self.forms if form.cleaned_data.get('is_active')
                           and not form.cleaned_data.get('DELETE', False)]

        if len(active_versions) > 1:
            raise forms.ValidationError('Может быть активна только одна версия продукта.')

        if self.has_changed():
            if len(active_versions) == 1:
                active_versions = active_versions[0]
                Version.objects.filter(product_id=self.instance.id, is_active=True).update(is_active=False)

        return active_versions


class ModeratorProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
