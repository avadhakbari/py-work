from django.db import models
import uuid

class product_mst(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product_id}"
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.product_id = uuid.uuid4()
        super().save(*args, **kwargs)

class product_sub_cat(models.Model):
    Product_sub_cat_id = models.CharField(primary_key=True, max_length=255)
    product = models.ForeignKey(product_mst, on_delete=models.CASCADE)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='images/')
    product_model = models.CharField(max_length=255)
    product_ram = models.CharField(max_length=255)

    def get_image_url(self):
        return self.image.url

    def __str__(self):
        return f"{self.Product_sub_cat_id}"

    def save(self, *args, **kwargs):
        if not self.pk:
            PRIFIX = "PRO"
            self.Product_sub_cat_id = f'{PRIFIX}_{uuid.uuid4()}'
        super().save(*args, **kwargs)