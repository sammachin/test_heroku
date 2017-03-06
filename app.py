import os
import tornado.httpserver
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	def get(self):
        name = os.getenv('NAME')
        lvn = os.getenv('MY_LVN')
		self.content_type = 'text/plain'
		self.write("$name is {} \n $lvn is {}".format(name, lvn))
		self.finish()
		
class EnvHandler(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	def get(self):
        with open('.env') as f:
            data = f.read()
		self.content_type = 'text/plain'
		self.write(data)
		self.finish()
						
def main():
	static_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
	print static_path
	application = tornado.web.Application([(r"/", MainHandler),
                                            (r"/env", EnvHandler),
											(r'/static/(.*)', tornado.web.StaticFileHandler, {'path': static_path}),
											])
	http_server = tornado.httpserver.HTTPServer(application)
	port = int(os.environ.get("PORT", 5000))
	http_server.listen(port)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()
	
	

