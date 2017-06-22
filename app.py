from displacy_service.server import APP, get_model
import os

get_model('en_core_web_md')

if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('0.0.0.0', 8000, APP)
    httpd.serve_forever()
