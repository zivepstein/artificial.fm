import gspread
import urllib.request
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import random, string
import argparse 
import psycopg2
import time
import pandas.io.sql as sqlio
from creds import rds_username, rds_password, rds_url
from creds import rds_port, rds_db
from utils import apply_fadeout
import librosa
import numpy
import soundfile

parser = argparse.ArgumentParser()
parser.add_argument("--src", type=str, help="data source", default="afm_songs")
parser.add_argument("--fadeout", type=float, help="data source", default=2.0)
args = parser.parse_args()

if args.src == 'afm_songs':
	conn = psycopg2.connect(
	    host=rds_url,
	    port=rds_port,
	    dbname=rds_db,
	    user=rds_username,
	    password=rds_password)
	query = "select * from afm_songs_prod"
	dat = sqlio.read_sql_query(query, conn)
elif args.src == "csv":
	dat = pd.read_csv("path/to/afm_songs_prod.csv")
else:
	print("{} not supported".format(args.src))
for i,r in dat.iterrows():
	local_url = '/home/host/myproject/static/music/batch3/{}.wav'.format(r['song_id'])
	urllib.request.urlretrieve(r['url'], local_url) #todo: name songs as song_id instead of url
	orig, sr = librosa.load(local_url, duration=50.0)
	out = orig.copy()
	apply_fadeout(out, sr, duration=args.fadeout)
	#soundfile.write('original.wav', orig, samplerate=sr)
	soundfile.write(local_url, out, samplerate=sr)
	print("dumped and trimmed {}/{}: {}".format(i, dat.shape[0], r['song_id']))

