from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from PIL import Image


User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    image = models.ImageField('Фото', upload_to='post_images', blank=True)
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; '
        'разрешены символы латиницы, цифры, дефис и подчёркивание.',
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    image = models.ImageField('Фото', upload_to='post_images', blank=True)
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; '
        'разрешены символы латиницы, цифры, дефис и подчёркивание.',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Категория',
        related_name='subcategories',
    )

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    image_small = models.ImageField(
        verbose_name="Изображение продукта 240 x 180.",
        upload_to='post_images/small/',
    )
    image_medium = models.ImageField(
        verbose_name="Изображение продукта 320 x 240.",
        upload_to='post_images/medium/',
    )
    image_large = models.ImageField(
        verbose_name="Изображение продукта 640 x 480.",
        upload_to='post_images/large/',
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; '
        'разрешены символы латиницы, цифры, дефис и подчёркивание.',
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Категория',
        related_name='products',
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Подкатегория',
        related_name='products',
    )
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        self.resize_image(self.image_small.path, (240, 180))
        self.resize_image(self.image_medium.path, (320, 240))
        self.resize_image(self.image_large.path, (640, 480))

    def resize_image(self, image_path, size):
        img = Image.open(image_path)
        img = img.resize(size, Image.Resampling.LANCZOS)
        img.save(image_path)


class Shopping(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='shopping',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='shopping_items',
        verbose_name='Продукт',
    )
    quantity = models.PositiveIntegerField(
        default=1, verbose_name='Количество'
    )

    class Meta:
        verbose_name = 'Позиция в корзине'
        verbose_name_plural = 'Позиции в корзине'

    def __str__(self):
        return f'{self.product.title} ({self.quantity})'


# Cart
# user


# CARTITEM
# product Product_item
# quanity
# cart cart_item

# CARTITEM.select_related(Product_item)
# cart.cart_item
