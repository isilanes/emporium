from django.db import models


class Person(models.Model):
    """
    A Person may be a client (Resident) or myself.
    """
    TITLE_CHOICES = (
        ("Doña", "Doña"),
        ("Don", "Don"),
    )
    title = models.CharField("Título", choices=TITLE_CHOICES, max_length=25)
    name = models.CharField("Nombre", max_length=100)
    status = models.CharField("Estado", max_length=25)
    nationality = models.CharField("Nacionalidad", max_length=25)
    address = models.CharField("Dirección", max_length=200)
    id_card = models.CharField("DNI", max_length=9)
    email = models.CharField("email", max_length=50)
    telephone = models.CharField("Teléfono", max_length=13)

    def __str__(self):
        return self.name
