import requests
# For AuthToken
import datetime
import time
import app.Static
import json

requests.packages.urllib3.disable_warnings()

# class responsible for providing an interface with the server, using AuthTocken class
class RequestInterface:
    def __init__(self):

        self.server = app.Static.server
        self.key = app.Static.api_key
        self.headers = {
            "Origin": "https://developer.riotgames.com",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Riot-Token": self.key,
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
        }
        self.session = requests.session()

    #return the response from the post call
    def post(self, path, json_data):
        try:
            return self.session.post(self.server + path,data=json_data, headers=self.headers, verify=False)
        except:
            return None
    #return the response of the get call
    def get(self, path):
        try:
            return self.session.get(self.server + path, headers=self.headers, verify=False)
        except:
            # Return None if we could not connect - or something is wrong with getting/setting the token
            return None
    #return the response of the delete call
    def delete(self, path):
        try:
            return self.session.delete(self.server + path, headers=self.headers, verify=False)
        except:
            return None

    #return the response of the patch call
    def patch(self, path, json_data):
        try:
            return self.session.patch(self.server + path, data=json_data, headers=self.headers,verify=False)
        except:
            return None
    #return the response of the put call
    def put(self, path, json_data):
        try:
            return self.session.put(self.server + path, data=json_data, headers=self.headers, verify=False)
        except:
            return None
