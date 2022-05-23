from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import FileResponse

def get_home(req):
  return FileResponse("home.html")

def get_product(req):
  return FileResponse("product.html")

def get_kvp(req):
  return FileResponse("kvp.html")

def get_info_arch(req):
  return FileResponse("info_arch.html")

def get_revenue(req):
  return FileResponse("revenew.html")

''' Route Configurations '''
if __name__ == '__main__':
  config = Configurator()

  config.add_route('get_home', '/')
  config.add_view(get_home, route_name='get_home')

  config.add_route('get_product', '/product')
  config.add_view(get_product, route_name='get_product')

  config.add_route('get_kvp', '/kvp')
  config.add_view(get_kvp, route_name='get_kvp')

  config.add_route('get_info_arch', '/info_arch')
  config.add_view(get_info_arch, route_name='get_info_arch')

  config.add_route('get_revenue', '/revenue')
  config.add_view(get_revenue, route_name='get_revenue')

  config.add_static_view(name='/', path='./public', cache_max_age=3600)

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 6000, app)
  server.serve_forever()
