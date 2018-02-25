from django.shortcuts import render
from app.RequestInterface import RequestInterface
import json

interface = RequestInterface()

# Create your views here.
def index(request):
    body = ''

    summoner = getJsonSummonerByName('RedNinja2')
    if summoner:

        body += '<p>' + 'ID: ' + str(summoner['id']) + '</p>'
        body += '<p>' + 'Account ID: ' + str(summoner['accountId']) + '</p>'
        body += '<p>' + 'Name: ' + str(summoner['name']) + '</p>'
        body += '<p>' + 'Profile Icon ID: ' + str(summoner['profileIconId']) + '</p>'
        body += '<p>' + 'Revision Date: ' + str(summoner['revisionDate']) + '</p>'
        body += '<p>' + 'Summoner Level: ' + str(summoner['summonerLevel']) + '</p>'

        champions = getJsonSummonerChampionMasteries(str(summoner['id']))

        if champions:
            champ_data = getJsonAllChampions()
            if champ_data == None:
                return render(request, 'summoner/index.html', {'body':'Error retrieving all champion data!'})
            for champ in champions:
                champion = champ_data['data'][str(champ['championId'])]
                iconLink = "http://ddragon.leagueoflegends.com/cdn/" + champ_data['version'] + "/img/champion/" + champion['image']['full']
                body += '<div>'
                body += '<h4>' + champion['name'] + '</h4>'
                body += '<img src="' + iconLink + '" alt="' + champion['name'] + '">'
                body += '<p>Mastery level: ' + str(champ['championLevel']) + '</p>'
                body += '<p>Points earned: ' + str(champ['championPoints']) + '</p>'
                body += '</div>'
        else:
            print("Could not load the champions!")
    else:
        print("Could not find the requested summoner!")
    context = {
        'body': body
    }
    return render(request, 'summoner/index.html', context)

def getJsonAllChampions():
    from pathlib import Path
    champPath = Path('all_champions.txt')
    if champPath.is_file():
        with open('all_champions.txt') as f:
            return json.loads(f.read())
    else:
        return None

def getJsonSummonerChampionMasteries(summonerId):
    path = '/lol/champion-mastery/v3/champion-masteries/by-summoner/' + summonerId
    masteries = interface.get(path)

    if masteries.status_code == 200 and masteries.text:
        return json.loads(masteries.text)
    else:
        return None

def getJsonSummonerByName(summonerName):
    path = "/lol/summoner/v3/summoners/by-name/" + summonerName

    r = interface.get(path)
    if r.status_code == 200 and r.text:
        return json.loads(r.text)
    else:
        return None
