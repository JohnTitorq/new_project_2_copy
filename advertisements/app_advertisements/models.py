from django.db import models


class Advertisement(models.Model):
    # назначение имение таблицы:
    class Meta:
        db_table="advertisements"
    # строковое представление:
    def __str__(self) -> str:
        return f"<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>"
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