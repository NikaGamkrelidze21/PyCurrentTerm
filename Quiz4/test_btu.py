import requests
from requests_oauthlib import OAuth2Session

# OAuth2 credentials
client_id = '954344362278-6tpr697u6i56msc4ts9jumnia982jimo.apps.googleusercontent.com'
client_secret = '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'
redirect_uri = 'https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?response_type=code&access_type=online&client_id=419171919769-4imdmtddn608c101qk0v7jpqvj5tu9m3.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fclassroom.btu.edu.ge%2Fge%2Flogin%2Foauth%2F&state&scope=email%20profile&approval_prompt=auto&service=lso&o2v=1&flowName=GeneralOAuthFlow'

# Authorization endpoint
authorization_url = 'https://example.com/oauth2/authorize'
token_url = 'https://example.com/oauth2/token'

# Create an OAuth2 session
oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)

# Fetch the authorization URL and user authorization
authorization_url, state = oauth.authorization_url(authorization_url)
print('Please go to this URL to authorize the application:', authorization_url)
authorization_response = input('Enter the full callback URL: ')

# Exchange the authorization code for access token
oauth.fetch_token(
    token_url,
    authorization_response=authorization_response,
    client_secret=client_secret
)

# Make authenticated requests
response = oauth.get('https://example.com/api/resource')
if response.status_code == 200:
    # Process the response or perform scraping operations
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)

