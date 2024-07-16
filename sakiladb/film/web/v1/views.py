from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from film.models import Film
from actor import models as actor_models


class FilmListView(APIView):
    def get(self, request, format=None):
        # Fetch films and prefetch related FilmActor instances
        films = Film.objects.prefetch_related("filmactor_set").all()
        data = []

        for film in films:
            actors_data = []

            # Iterate over prefetched FilmActor instances
            for film_actor in film.filmactor_set.all():
                actor_data = {
                    "first_name": film_actor.actor.first_name,
                    "last_name": film_actor.actor.last_name,
                }
                actors_data.append(actor_data)

            names = {
                "id": film.id,
                "title": film.title,
                "description": film.description,
                "release_year": film.release_year,
                "rental_duration": film.rental_duration,
                "rental_rate": str(film.rental_rate),
                "length": film.length,
                "replacement_cost": str(film.replacement_cost),
                "rating": film.rating,
                "actors": actors_data,
            }
            data.append(names)

        return Response(data)


class FeaturedFilmListView(APIView):
    """
    View to list all featured films.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    # Uncomment the following lines if authentication and permission are required
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all featured films.
        """
        featured_films = Film.objects.filter(is_featured=True)
        film_data = [
            {
                "id": film.id,
                "title": film.title,
                "description": film.description,
                "release_year": film.release_year,
                "rental_duration": film.rental_duration,
                "rental_rate": film.rental_rate,
                "length": film.length,
                "replacement_cost": film.replacement_cost,
                "rating": film.rating,
            }
            for film in featured_films
        ]
        return Response(film_data)
