from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model


User=get_user_model()


class Advertisement(models.Model):
    
    user=models.ForeignKey(
        User,
        verbose_name='user',
        on_delete=models.CASCADE
    )

    image=models.ImageField(
        "image",
        upload_to="advertisements/"
    )
    
    # строковое поле для небольших размеров | 'Заголовок' = verbose_name = название поля извне
    title=models.CharField("Заголовок", max_length=128)
    
    # описание товара ( большое текстовое поле = TextField )
    description=models.TextField("Описание")

    # цена ( специальный тип данных с плавающей точкой )
    price=models.DecimalField("Цена", max_digits=10, decimal_places=2)

    # возможность торга ( True/False )
    auction=models.BooleanField("Торг", help_text="Отметьте, уместен ли торг.")

    # имя продавца + контакты

    # дата публикации ( Записывается при создании объявления )
    created_at=models.DateTimeField(auto_now_add=True)

    # дата изменения ( Записывается при каждом обновлении )
    updated_at=models.DateTimeField(auto_now=True)

    # актуальность

    # кол-во товара 

    # возможность обмена

    # БУ / новое

    # возможность взять в долг/рассрочку

    # назначение имение таблицы:
    class Meta:
        db_table="advertisements"
    
    # строковое представление:
    def __str__(self) -> str:
        return f"<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>"
    
    # отображенеие времени создания: 
    @admin.display(description="Дата Создания")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date()==timezone.now().date():
            created_date=self.created_at.strftime("%H:%M:%S")
            return format_html("<span style='color:green; font-weight:bold;'> Сегодня в {} </span>", created_date)
        return self.created_at.strftime("%d.%m.%Y at %H:%M:%S")
    
    # отображенеие времени изменения: 
    @admin.display(description="Дата Изменения")
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date()==timezone.now().date():
            updated_date=self.updated_at.strftime("%H:%M:%S")
            return format_html("<span style='color:yellow; font-weiht:bold;'> Сегодня в {} </span>", updated_date)
        return self.updated_at.strftime("%d.%m.%Y at %H:%M:%S")
    
    # отображение изображения
    @admin.display(description="Photo")
    def get_html_image(self):
        if self.image:
            return format_html(
                '<img src="{}" style="max-width:80px; max-height:80px">',
                self.image.url
            )