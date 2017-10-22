import falcon

from api.resources import HealthCheck


api = falcon.API()
api.add_route('/_health', HealthCheck())
