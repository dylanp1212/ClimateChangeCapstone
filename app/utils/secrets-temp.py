import os

def getSecrets():
    secrets = {
        'MONGO_HOST':'mongodb+srv://dylanpaltiel:<dpmongodb>@cluster0.k1ulez0.mongodb.net/CapstoneDB?retryWrites=true&w=majority',
        'MONGO_DB_NAME':'CapstoneDB',
        'GOOGLE_CLIENT_ID': '',
        'GOOGLE_CLIENT_SECRET':'',
        'GOOGLE_DISCOVERY_URL':"https://accounts.google.com/.well-known/openid-configuration",
        'MY_EMAIL_ADDRESS':''
        }
    return secrets