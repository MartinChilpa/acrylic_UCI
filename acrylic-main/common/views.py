from django_countries.data import COUNTRIES
from rest_framework import viewsets, filters, permissions, status, serializers, response


class CountryViewSet(viewsets.ViewSet):
    permission_classes = []
    authentication_classes = []

    def list(self, request):
        choices = []
        choice_dict = dict(COUNTRIES)

        for k, v in choice_dict.items():
            value = {'key': k, 'value': v}
            choices.append(value)
        return response.Response(choices, status=status.HTTP_200_OK)
