from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getRoutes(request):
    routes = [
        
        {
            'Name' : "Dhaka Sub Area API",
            'Endpoint List' : [
                                    {
                                        'Endpoint': '/api/area/list',
                                        'method': 'GET',
                                        'body': None,
                                        'description': 'returns Dhaka Sub Area List including Latitude & Longitude'
                                    },
                                    {
                                        'Endpoint': '/api/area/{cityName}',
                                        'method': 'GET',
                                        'body': None,
                                        'description': 'returns specific Area including Latitude & Longitude'
                                    },
                                    {
                                        'Endpoint': '/api/area/list?search={word}',
                                        'method': 'GET',
                                        'body': None,
                                        'description': 'returns filter those specific Area including Latitude & Longitude'
                                    }
                                ]
        },
    ]
    return Response(routes)
