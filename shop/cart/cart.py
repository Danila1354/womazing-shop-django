from catalog.models import ProductVariant
from decimal import Decimal


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

        products = ProductVariant.objects.filter(id__in=product_ids).prefetch_related(
            "product"
        )

        for product in products:
            item = self.cart[str(product.id)].copy()
            item["product"] = product
            item["price"] = float(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
        )
