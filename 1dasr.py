import requests

class WebScrapingStudy:

    def __init__(self, url, token, chat_id):
        self.token=token
        self.chat_id=chat_id
        self.url = url

    @staticmethod
    def send_telegram_messenge(token, chat_id, messenge:str):
        url= f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": messenge}
        requests.post(url=url, data=data)
    @staticmethod
    def get_json_data(url):
        response = requests.get(url)
        return response.json().get("data")



    def run_scripit(self):
        responses = self.get_json_data(self.url)
        for response in responses:
            name=response.get("name")
            self.send_telegram_messenge(token=self.token, chat_id=self.chat_id,messenge=name)
        return responses
token ='7639005796:AAHU6moXHX_VtoR9AO-4WSAiqU12z0IDNiw'
chat_id=5652442685

url = "https://admin.soffstudy.uz/api/v1/gallery/?limit=9&offset=0"
wss1 = WebScrapingStudy(url=url, token=token,chat_id=chat_id)


x = wss1.run_scripit()

print(x)