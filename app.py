from flask import Flask,jsonify, Response, session, request, redirect, render_template
import flask
import requests
# import dropbox
import json
import pdb
import base64
# from dropbox.client import DropboxOAuth2Flow, DropboxClient
from base64 import decodestring
from ocr import *
import uuid

app = Flask(__name__, static_url_path='/static')
# APP_KEY = '82767lp1t5oh8ee'
# APP_SECRET = '41lwxzid1jdlfbq'
# REDIRECT_URI = "http://localhost:5000/authenticated"

# def get_dropbox_auth_flow(web_app_session):
    # return DropboxOAuth2Flow(APP_KEY, APP_SECRET, REDIRECT_URI, web_app_session, "dropbox-auth-csrf-token")

# # URL handler for /dropbox-auth-start
# def dropbox_auth_url(web_app_session, request):
    # return get_dropbox_auth_flow(web_app_session).start()

# # URL handler for /dropbox-auth-finish
# def dropbox_auth_finish(web_app_session, request):
    # try:
        # access_token, user_id, url_state = \
                # get_dropbox_auth_flow(web_app_session).finish(request.query_params)
    # except DropboxOAuth2Flow.BadRequestException, e:
        # http_status(400)
    # except DropboxOAuth2Flow.BadStateException, e:
        # # Start the auth flow again.
        # redirect("/dropbox-auth-start")
    # except DropboxOAuth2Flow.CsrfException, e:
        # http_status(403)
    # except DropboxOAuth2Flow.NotApprovedException, e:
        # flash('Not approved?  Why not?')
        # return redirect("/home")
    # except DropboxOAuth2Flow.ProviderException, e:
        # logger.log("Auth error: %s" % (e,))
        # http_status(403)

# code = raw_input("Enter the authorization code here: ").strip()
#
# access_token, user_id = flow.finish(code)
# client = dropbox.client.DropboxClient(access_token)

@app.route('/')
def authenticate():
    # return redirect(dropbox_auth_url(session, request))
    return redirect("/main")

# @app.route('/authenticated')
# def index():
    # if(request.args.get('code') is not None):
        # code = request.args.get('code')
        # state = request.args.get('state')
        # urlToGetToken = "https://api.dropboxapi.com/1/oauth2/token"
        # payload = { "code": code, "grant_type": "authorization_code", "client_id": APP_KEY, "client_secret": APP_SECRET, "redirect_uri": REDIRECT_URI}
        # userData = requests.post(urlToGetToken, params=payload)
        # accessToken = userData.json().get('access_token')
        # session['access_token'] = accessToken
    # return render_template('index.html')
# @app.route('/note')
# def serveNote():
    # return render_template('noteview.html')

@app.route('/main')
def mainView():
    # if("access_token" in session):
    return render_template('main.html')
    # else:
        # return redirect("/")

@app.route('/upload',methods=['POST'])
def spliceImage():
    if request.method =='POST':
        data = request.form['image']
        tempFileName = "static/temp/"+str(uuid.uuid4())
        decode64String(tempFileName,data);
        images=segmenter.getImages(tempFileName)
        return json.dumps(images)
        # dat = json.dumps([get64String(x) for x in images])
        # resp = Response(response=dat,
                            # status=200, \
                            # mimetype="application/json")
    return "fail"


def decode64String(filename,imagestr):
    with open(filename,"wb") as f:
        f.write(decodestring(imagestr))
    return filename

def get64String(filename):
    with open(filename, "rb") as image_file:
       encoded_string = base64.b64encode(image_file.read())
    return encoded_string

# @app.route('/files', methods=['POST'])
# def filesView():
    # if("access_token" in session):
        # return flask.jsonify(**{ "didstuff": True })

if __name__ == "__main__":
    # app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
    app.run(host='0.0.0.0', port=80)
