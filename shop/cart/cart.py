from catalog.models import ProductVariant
from decimal import ROUND_HALF_UP, Decimal
from django.shortcuts import get_object_or_404
from catalog.models import Coupon
from django.utils import timezone


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, product_variant, quantity=1, override_quantity=False):
        product_id = str(product_variant.id)
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 0, "price": str(product_variant.price)}
        if override_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product_variant):
        product_id = str(product_variant.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        del self.session["cart"]
        self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = ProductVariant.objects.filter(id__in=product_ids).prefetch_related("product")
        coupon = self.get_coupon()

        for product in products:
            item = self.cart[str(product.id)].copy()
            item["product"] = product
            item_price = Decimal(item["price"])
            if coupon:
                discount_amount = (item_price * coupon.discount_percentage) / 100
                item_price -= discount_amount
            # округляем до 2 знаков
            item_price = item_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            item["price"] = item_price
            item["total_price"] = (item_price * item["quantity"]).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        total = Decimal("0")
        coupon = self.get_coupon()
        for item in self.cart.values():
            item_price = Decimal(item["price"])
            if coupon:
                item_price -= item_price * coupon.discount_percentage / 100
            item_price = item_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            total += item_price * item["quantity"]
        total = total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        return total
    
    def get_coupon(self):
        code = self.session.get("coupon")
        if not code:
            return None
        try:
            coupon = Coupon.objects.get(code__iexact=code)
        except Coupon.DoesNotExist:
            return None

        if not coupon.active or not (coupon.valid_from <= timezone.now() <= coupon.valid_to):
            return None

        return coupon

    def apply_coupon(self, coupon):
        self.session['coupon'] = coupon.code
        self.save()
        
