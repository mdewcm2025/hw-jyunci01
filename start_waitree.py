# pip install waitress
from waitress import serve
from cmsimde.flaskapp import app

if __name__ == "__main__":
    serve(app, host="::1", port=8080, threads=8)