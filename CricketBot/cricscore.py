import requests
from datetime import datetime

class ScoreGet:
    def __init__(self):
        self.url_get_all_matches = "https://cricapi.com/api/matches"
        self.get_score = "https://cricapi.com/api/cricketScore"
        self.apikey = "2iXIKphQcZPADzA9XillEXDvxf63"
        self.uniqueid = ""

    def get_unique_id(self):
        uri_params = {"apikey":self.apikey}
        resp = requests.get(self.url_get_all_matches, params=uri_params)
        resp_dict = resp.json()
        uid_found = 0

        for i in resp_dict['matches']:
            if(i['team-1']=="Kabul Eagles" or i['team-2']=="Kabul Eagles" and i['matchstarted']):
                today_date = datetime.today().strftime('%Y-%M-%D')
                if(today_date == i['date'].split("T")[0]):
                    self.uniqueid = i['uniqueid']
                    uid_found = 1
                    break

        if not uid_found:
            self.uniqueid = -1

        send_data = self.get_score_current(self.uniqueid)

    def get_score_current(self,uniqueid):
        data = ""
        if (uniqueid == -1):
            data = "No matches today"
        else:
            uri_params = {"apikey":self.apikey, "uniqueid":uniqueid}
            resp = requests.get(self.get_score, params=uri_params)
            data_json = resp.json()
            try:
                data="The score is : \n"+data_json['stat']+"\n"+data_json['score']
            except KeyError as ke:
                print(e)
        return data

if (__name__ == "__main__"):
    obj_score=ScoreGet()
    obj_score.get_unique_id()
