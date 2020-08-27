import os
import urllib.parse
from flask import request, Blueprint
from flask_restx import Api, Resource

from main.service.token_service import create_jwt_token

webhook_blueprint = Blueprint('webhook_blueprint', __name__)

api = Api(webhook_blueprint,
          title='Webhook API',
          description='Webhook API',
          doc=False
          )


@api.route('/webhook')
class WebhookResource(Resource):

    @api.response(400, 'Validation error')
    def post(self):

        data = request.get_json(force=True)

        print(data)

        key_element = data.get('lead').get('email') if data.get('lead').get('email') else data.get('lead').get(
            'document')

        dict_to_sign = {
            'sub': key_element,
            'type': 'EMAIL' if data.get('lead').get('email') else 'DOCUMENT'
        }

        token_result = create_jwt_token(dict_to_sign)

        dict_result_document = {
            'om_response_data': {
                'redirect': urllib.parse.quote(f'{os.environ.get("OPTIN_MOSTER_CALLBACK")}?token={token_result}')
            }
        }

        return dict_result_document, 200
