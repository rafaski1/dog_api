# from fastapi import Request
# from dotenv import load_dotenv
# from os import getenv
#
# from dog_api.main import app_error_handler
#
# load_dotenv()
#
# API_KEY = getenv("API_KEY")
#
#
# def verify_api_key(request: Request):
#     headers = dict(request.headers)
#     if headers.get("api-key") == API_KEY:
#         return headers.get("api-key")
#     raise app_error_handler
#
