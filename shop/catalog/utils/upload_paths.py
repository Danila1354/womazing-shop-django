import uuid
import os

def product_image_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    return f"products/{uuid.uuid4()}{ext}"
