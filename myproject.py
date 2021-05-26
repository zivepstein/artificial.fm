from flask import Flask, render_template, request, redirect,url_for, jsonify,copy_current_request_context, send_from_directory, Markup, session
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import random, string
import psycopg2
import time
from creds import rds_username, rds_password, rds_url
from creds import rds_port, rds_db
import pandas.io.sql as sqlio

conn = psycopg2.connect(
    host=rds_url,
    port=rds_port,
    dbname=rds_db,
    user=rds_username,
    password=rds_password)

app = Flask(__name__)
app.config['DEBUG'] = False  # if True, server reloads on any code change

app.config['SECRET_KEY'] = '7ae0ef9e033b5fa5er53aa4876t'
add_rating = """ INSERT INTO afm_ratings VALUES (now(), %s, %s, %s, %s, %s)"""

def write2database(conn, table, data):
	cur = conn.cursor()
	cur.execute(table, (data))
	conn.commit()
	cur.close()

def get_songs(conn):
	dat = sqlio.read_sql_query("select * from afm_songs", conn)
	dat['cumcount'] = dat.sample(frac=1).groupby(['dna_artist', 'dna']).cumcount()+1
	songs = dat.sort_values(['cumcount'])[['url', 'song_id']]
	return songs.to_dict('records')

@app.route('/', methods=['GET', 'POST'])
def bonjour():
    if not 'session_id' in session:
        session['session_id'] = ''.join(random.choice('0123456789ABCDEF') for i in range(16))  # TODO what's this?
    songs = get_songs(conn)
    print(songs)
    return render_template("index.html", songs = songs)

@app.route('/user_response', methods=['GET', 'POST'])
def click():
    user_agent = request.user_agent.string
    param_data = request.values.to_dict()
    rating_data = (param_data['song_id'], session['session_id'], param_data['question'],param_data['response'], "batch1")
    print(rating_data)
    write2database(conn, add_rating, rating_data)
    return("worked!")

if __name__=='__main__':
    app.run('0.0.0.0', threaded=True)