from django import forms

from .models import ProductVariant, Color


class AddToCartForm(forms.Form):
    color = forms.ModelChoiceField(
        queryset=Color.objects.none(),
        widget=forms.RadioSelect
    )
    size = forms.ChoiceField(choices=[])
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
    )
    def __init__(self, *args, product=None, **kwargs):
        super().__init__(*args, **kwargs)

        if product:
            variants = ProductVariant.objects.filter(product=product)

            self.fields['size'].choices = [
                (v.size, v.size) for v in variants
            ]

            self.fields['color'].queryset = Color.objects.filter(
                product_variants__in=variants
            ).distinct()

