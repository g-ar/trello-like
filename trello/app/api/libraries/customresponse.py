from rest_framework.response import Response
from rest_framework.status import is_success, HTTP_200_OK


class CustomResponse(Response):
	def __init__(self, message=None, code=HTTP_200_OK, payload=None, etype=None,
				 template_name=None, headers=None,
				 exception=False, content_type=None):
		data = {
			"success": True,
			"payload": payload,
			"message": message
			}

		if not is_success(code=code):
			data["success"] = False
			error_data = {
			"code" : code,
			}
			data["error"] = error_data
		super(CustomResponse, self).__init__(data=data, status=code, template_name=template_name, headers=headers, exception=exception, content_type=content_type)