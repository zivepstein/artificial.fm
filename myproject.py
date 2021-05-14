from flask import Flask, render_template, request, redirect,url_for, jsonify,copy_current_request_context, send_from_directory, Markup, session
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import random, string

app = Flask(__name__)
app.config['DEBUG'] = False  # if True, server reloads on any code change

app.config['SECRET_KEY'] = '7ae0ef9e033b5fa5er53aa4876t'

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

client = gspread.authorize(creds)
sheet = client.open('jukebox pipeline')
sheet_instance = sheet.get_worksheet(1)
records_data = sheet_instance.get_all_records()
records_df = pd.DataFrame.from_dict(records_data)

records_df = records_df.sample(frac=1).sort_values(['item'])
songs = list(records_df['url'].values)

@app.route('/', methods=['GET', 'POST'])
def bonjour():
    if not 'session_id' in session:
        session['session_id'] = ''.join(random.choice('0123456789ABCDEF') for i in range(16))  # TODO what's this?
    return render_template("index.html", songs = songs)

@app.route('/user_response', methods=['GET', 'POST'])
def click():
    user_agent = request.user_agent.string
    param_data = request.values.to_dict()
    # write2database(conn, add_stimulus, stim_data)
    print(param_data)
    return("worked!")

if __name__=='__main__':
    app.run('0.0.0.0', threaded=True)



