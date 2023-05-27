from flask import Flask, Response, render_template, request
from flask_cors import CORS, cross_origin
import requests


app = Flask(__name__)


CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
api_url = "https://api.deezer.com/search/artist?q=eminem&limit=1"


@app.route("/", methods=['POST', 'GET'])
# @cross_origin
def home():
   
    if request.method == 'POST':
        request_data = request.form
        #get artist name from front-end/ templates  
        artist_name = request_data['artist_name']
        #the deezer api
        api_url = f"https://api.deezer.com/search/artist?q={artist_name}&limit=1"
        artist_data = requests.get(api_url).json()
         #create an empty dict to store our result object - artist_info
        artist_info = {}

        #include a new key for top 5 artist track in artist info
        artist_info['top_5_tracks'] = {}

        #confirms there is a result before attempting to retrieve anything
        if artist_data['data'] != []:
          #print(artist_data) you will understand previous line better
          #you would also get insight to next line : working with list and dictonary
            artist_details = artist_data['data'][0]
            #print(artist_details) to get familiar with what you working with


            #include copy some needed items from api object i.e artist_info to the artist_details we would return/render in the front-end/templates
            artist_info['artist_image'] = artist_details['picture_medium']
            artist_info['artist_link'] = artist_details['link']
            artist_info['artist_name'] = artist_name
            artist_id = artist_details['id']
            top_5_tracks = requests.get(
                f'https://api.deezer.com/artist/{artist_id}/top?limit=5').json()['data']
            # print(top_5_tracks)

            top_5_tracks_info = []

            track = {'title': "", 'preview': "", "cover":""}

            for each_track_data in top_5_tracks:
                track = {'title': "", 'preview': ""}
                track['title'] = each_track_data['title']
                track['preview'] = each_track_data['preview']
                track['cover'] = each_track_data['album']['cover']
                top_5_tracks_info.append(track)

            artist_info['top_5_tracks'] = top_5_tracks_info

            return render_template('index.html', artist_info=artist_info)
        else:
            artist_info['artist_name'] = f"{artist_name} : Artist not found"

            return render_template('index.html', artist_info=artist_info)
    return render_template('index.html', artist_info=artist_info)


if __name__=="__main__":
    app.run(debug=True)

