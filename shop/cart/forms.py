from django import forms

from catalog.models import Coupon, ProductVariant, Color, Size


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


class UpdateCartForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput,
    )

class ApplyCouponForm(forms.Form):
    code = forms.CharField(
        max_length=50,
        label="Промокод",
        widget=forms.TextInput(attrs={"placeholder": " ", "class": "form-input"}),
    )
    def clean_code(self):
        code = self.cleaned_data.get("code", "").strip()
        try:
            coupon = Coupon.objects.get(code__iexact=code)
        except Coupon.DoesNotExist:
            raise forms.ValidationError("Такой купон не найден")

        if not coupon.is_valid():
            raise forms.ValidationError("Этот купон недействителен")

        return coupon 
