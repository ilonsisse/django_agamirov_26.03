import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST']):
        def create_place(request):
            try:
                data = json.loads(request.body.decode("utf-8"))

                if Place.objects.filter(name=data['name']).exists():
                    return Response(status=status.HTTP_404_NOT_FOUND, data={
                        'ok': False,
                        'message': 'A place with that name already exists'
                    })

                new_place = Place(
                    name = data['name'],
                    population = int(data['population'])
                )

                new_place.save()

                return Response(status=status.HTTP_200_OK, data={
                    'ok': True,
                    'message': 'Place successfully created.',
                    'id': new_place.id
                })

            except KeyError as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={
                    'ok': False,
                    'message': f'Field {e} is required'
                })

            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={
                    'ok': False,
                    'message': 'unexpected error'
                })