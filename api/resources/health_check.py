import falcon


class HealthCheck(object):

    def on_get(self, _, resp):
        resp.body = 'OK'
        resp.content_type = falcon.MEDIA_TEXT
        resp.status = falcon.HTTP_200
