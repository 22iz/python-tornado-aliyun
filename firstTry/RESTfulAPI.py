from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

# import tornado.autoreload
settings = {'debug' : True}
# define("debug",default=True,help="Debug Mode",type=bool)


class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        response = { 'version': '3.5.1',
                     'last_build':  date.today().isoformat(),
                     'API': listAPI() }
        self.write(response)

class CardByIdHandler(tornado.web.RequestHandler):
    def get(self, id):
        response = { 'id': int(id),
                     'name': 'CARDBOX',
                     'release_date': date.today().isoformat(),
                     'API': listAPI() }
        self.write(response)

def listAPI():
    msg = 'You can also try: '
    api_version = '120.24.224.48:8000/version'
    api_getgamebyid = '120.24.224.48:8000/cardbyid/random_integer'
    return msg + api_version + ", " + api_getgamebyid

application = tornado.web.Application([
    (r"/cardbyid/([0-9]+)", CardByIdHandler),
    (r"/version", VersionHandler)
], **settings)

if __name__ == "__main__":
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
