from django import forms

from .models import ProductVariant, Color, Size


class AddToCartForm(forms.Form):
    color = forms.ModelChoiceField(
        queryset=Color.objects.none(), widget=forms.RadioSelect
    )
    size = forms.ModelChoiceField(queryset=Size.objects.none(), empty_label=None)
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
    )

    def __init__(self, *args, product=None, **kwargs):
        super().__init__(*args, **kwargs)

        if product:
            variants = ProductVariant.objects.filter(product=product)

            self.fields["size"].queryset = Size.objects.filter(
                productvariant__in=variants,
            ).distinct()

            self.fields["color"].queryset = Color.objects.filter(
                product_variants__in=variants
            ).distinct()
