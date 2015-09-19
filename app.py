from flask import Flask, session, request, redirect, render_template
import dropbox
from dropbox.client import DropboxOAuth2Flow, DropboxClient


app = Flask(__name__)

APP_KEY = '82767lp1t5oh8ee'
APP_SECRET = '41lwxzid1jdlfbq'

def get_dropbox_auth_flow(web_app_session):
    redirect_uri = "http://localhost:5000/authenticated"
    return DropboxOAuth2Flow(APP_KEY, APP_SECRET, redirect_uri, web_app_session, "dropbox-auth-csrf-token")

# URL handler for /dropbox-auth-start
def dropbox_auth_url(web_app_session, request):
    return get_dropbox_auth_flow(web_app_session).start()

# URL handler for /dropbox-auth-finish
def dropbox_auth_finish(web_app_session, request):
    try:
        access_token, user_id, url_state = \
                get_dropbox_auth_flow(web_app_session).finish(request.query_params)
    except DropboxOAuth2Flow.BadRequestException, e:
        http_status(400)
    except DropboxOAuth2Flow.BadStateException, e:
        # Start the auth flow again.
        redirect("/dropbox-auth-start")
    except DropboxOAuth2Flow.CsrfException, e:
        http_status(403)
    except DropboxOAuth2Flow.NotApprovedException, e:
        flash('Not approved?  Why not?')
        return redirect("/home")
    except DropboxOAuth2Flow.ProviderException, e:
        logger.log("Auth error: %s" % (e,))
        http_status(403)

# code = raw_input("Enter the authorization code here: ").strip()
# 
# access_token, user_id = flow.finish(code)
# client = dropbox.client.DropboxClient(access_token)
# print 'linked account: ', client.account_info()

@app.route('/')
def authenticate():
	return redirect(dropbox_auth_url(session, request))

@app.route('/authenticated/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
	app.run(debug=True)
