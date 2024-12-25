from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    tours = models.TextField(
        verbose_name="туры",
        help_text='туры'
    )

    tickets = models.TextField(
        verbose_name="билеты",
        help_text='билеты'
    )

    rent_of_auto = models.TextField(
        verbose_name="аренда авто",
        help_text='аренда авто'
    )

    vills = models.TextField(
        verbose_name="виллы",
        help_text='виллы'
    )

    yachts_and_regats = models.TextField(
        verbose_name="яхты&регаты",
        help_text='яхты&регаты'
    )

    excursions = models.TextField(
        verbose_name="Экскурсии",
        help_text='Экскурсии'
    )

    insurance = models.TextField(
        verbose_name="Страхование",
        help_text='Страхование'
    )

