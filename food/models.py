from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator, FileExtensionValidator
from account.models import Account
# For Admin Panel Interface
from django.utils.html import format_html
from django.utils.functional import cached_property


# Create your views here.
class Food(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(3), ], unique=True)
    description = models.CharField(max_length=200, validators=[MinLengthValidator(5),], unique=True, null= True)
    recipe = models.CharField(max_length=500, validators=[MinLengthValidator(10), ], unique=True)
    slug = models.SlugField(validators=[MinLengthValidator(10), ])
    image = models.ImageField(
        upload_to='image/category/', validators=[
            FileExtensionValidator(
                ['jpg', 'jpeg', 'png'],
                "Only jpg and jpeg along with png are allowed.",
            )
        ], null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_nonveg = models.BooleanField('is Non veg', default=False)
    is_veg = models.BooleanField('is Veg', default=True)
    account = models.ForeignKey(Account, on_delete=models.RESTRICT)


    @cached_property
    def thumbnail(self):
        html = '<img src="{img}" height="20px" width="20px" style="border-radius: 50%">'
        if self.image:
            return format_html(html, img=self.image.url)
        return (
            format_html('<strong>There is no image for this entry.<strong>'))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name,self.created_at)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'food'
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'
