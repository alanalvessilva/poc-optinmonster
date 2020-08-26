import os

import werkzeug
from werkzeug.middleware.proxy_fix import ProxyFix
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask
from main.resource.webhook_resource import webhook_blueprint

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

app.register_blueprint(webhook_blueprint)

if __name__ == '__main__':
    app.run(port=int(os.environ.get('HTTP_PORT')), host='0.0.0.0', threaded=True)