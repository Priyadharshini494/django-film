from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from actor import models as actor_models


class ActorCreateView(APIView):

    def post(self, request, format=None):
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        new_actor = actor_models.Actor.objects.create(
            first_name=first_name, last_name=last_name
        )
        names = [
            {
                "id": new_actor.id,
                "first name": new_actor.first_name,
                "last name": new_actor.last_name,
            }
            # for user in actor_models.Actor.objects.all()
        ]
        return Response(names)


class ActorListView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        names = [
            {"id": user.id, "first_name": user.first_name, "last_name": user.last_name}
            for user in actor_models.Actor.objects.all()
        ]
        return Response(names)


class ActorDetailView(APIView):

    def get(self, request, actor_id, format=None):
        user = actor_models.Actor.objects.get(id=actor_id)
        names = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
        return Response(names)


class ActorUpdateView(APIView):

    def put(self, request, pk, format=None):
        try:
            actor = actor_models.Actor.objects.get(pk=pk)
        except actor_models.Actor.DoesNotExist:
            return Response(
                {"error": "Actor not found"}, status=status.HTTP_404_NOT_FOUND
            )

        # Update actor fields with data from the request
        first_name = request.data.get("first_name", actor.first_name)
        last_name = request.data.get("last_name", actor.last_name)

        actor.first_name = first_name
        actor.last_name = last_name
        actor.save()

        names = {
            "first_name": actor.first_name,
            "last_name": actor.last_name,
        }

        return Response(names)
