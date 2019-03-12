from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
        response.data['success'] = response.status_code == 200
        response.data['message'] = response.data.pop('detail')

    return response


class CustomJsonRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if 'success' not in data:
            data['success'] = True
            data['message'] = ''
        return super(CustomJsonRenderer, self).render(data, accepted_media_type, renderer_context)
