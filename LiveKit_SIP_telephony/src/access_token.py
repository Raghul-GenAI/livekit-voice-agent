# token_generator.py
from livekit import AccessToken

api_key = "devkey"
api_secret = "secret"

token = AccessToken(api_key, api_secret)
token.identity = "bot"
token.add_grant(room_join=True, room="test-room")

jwt = token.to_jwt()
print(jwt)
