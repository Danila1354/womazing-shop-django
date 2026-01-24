from .models import Category

def footer_context(request):
    categories = Category.objects.all()
    current_category = request.GET.get("category", "")
    return {
        "categories": categories,
        "current_category": current_category
    }