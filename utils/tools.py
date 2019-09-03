# -*- coding: utf-8 -*
def response_err(code=999):
	"""make response msg format"""

	resp = {
		'status': 1,
		'code': code,
	}

	return resp
