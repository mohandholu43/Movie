
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import json
from rest_framework import status

class Movie(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        """
        Return a list of all Movie.
        """
        try:
            movie_json_data = []
            with open("static/movie.json", 'r') as f:
                movie_json_data = json.load(f)
            return Response({"data":movie_json_data},status=status.HTTP_200_OK)
        except :
            return Response('no such Movie List', status=status.HTTP_200_OK)
