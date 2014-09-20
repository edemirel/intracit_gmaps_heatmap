from flask import Flask
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    return app

if __name__ == '__main__':
    t = create_app()
    t.run(host='0.0.0.0', port=8080, debug=True)
