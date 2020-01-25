import falcon

class StaticResource(object):
    def on_get(self,req,resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.stream = open('index.html', 'rb')
        with resp.stream as f:
            resp.body = f.read()

app = falcon.API()
app.add_route('/', StaticResource())
