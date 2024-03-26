import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from postgres_kr.example.models import Place, Shop


@api_view(['POST'])
def create_shop(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        places = Place.objects.filter(id=data['place'])
        if places.count() == 1:
            current_place = places.first()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data={
                'ok': False,
                'message': 'Place does not exist.'
            })

        if Shop.objects.filter(name=data['name']).exists():
            return Response(status=status.HTTP_404_NOT_FOUND, data={
                'ok': False,
                'message': 'A shop with that name already exists'
            })

        new_shop = Shop(
            name=data['name'],
            income_per_month =data['income_per_month'],
            supervisor=data.get('supervisor', None)
            place=current_place
        )

        new_shop.save()

        return Response(status=status.HTTP_200_OK, data={
            'ok': True,
            'message': 'Shop successfully created',
            'id': new_shop.id
        })

    except KeyError as e:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={
            'ok': False,
            'message': 'Unexpected error'
        })