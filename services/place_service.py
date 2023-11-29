import requests

class PlaceService:
    def __init__(self, url):
        self.url = url

    def send_data(self, data_to_send):
        response = requests.post(self.url, json=data_to_send)

        if response.status_code == 200:
            received_response = response.json()
            return received_response
        else:
            return f"Failed to send data. Status code: {response.status_code}"
        