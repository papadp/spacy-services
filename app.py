from displacy_service.server import APP, get_model
import os

# Pre-load English model only, to save memory
get_model(os.environ['SPACY_NER_MODEL'])
# get_model('de')


if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('0.0.0.0', 8000, APP)
    httpd.serve_forever()
