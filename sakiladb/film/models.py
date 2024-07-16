from django.db import models
from django.utils import timezone
from sakiladb.models import BaseModel
from actor.models import Actor, Category


class Film(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_year = models.IntegerField()
    rental_duration = models.IntegerField()
    rental_rate = models.DecimalField(max_digits=5, decimal_places=2)
    length = models.IntegerField()
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    actor = models.ManyToManyField(Actor, through="FilmActor")

    # Choices for rating field
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"
    RATING_CHOICES = [
        (G, "G"),
        (PG, "PG"),
        (PG_13, "PG-13"),
        (R, "R"),
        (NC_17, "NC-17"),
    ]
    # rating = models.CharField(max_length=5, choices=RATING_CHOICES)
    rating = models.CharField(
        max_length=5,
        choices=RATING_CHOICES,
        default=G,
    )
    special_features=models.CharField(max_length=255)
    
    # New boolean field
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class FilmActor(BaseModel):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.film.title} - {self.actor.first_name} {self.actor.last_name}"


class FilmCategory(BaseModel):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.film.title} - {self.category.name}"


class FilmText(BaseModel):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()


class Language(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
