from flask import Flask, render_template, request, redirect,url_for, jsonify,copy_current_request_context, send_from_directory, Markup, session
import gspread
import urllib.request
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import random, string
import argparse 
import psycopg2
import time
from creds import rds_username, rds_password, rds_url
from creds import rds_port, rds_db

parser = argparse.ArgumentParser()
parser.add_argument("--src", type=str, help="data source", default="afm_songs")
args = parser.parse_args()

if args.src == 'afm_songs':
	conn = psycopg2.connect(
	    host=rds_url,
	    port=rds_port,
	    dbname=rds_db,
	    user=rds_username,
	    password=rds_password)
	query = "select * from afm_songs"
	dat = sqlio.read_sql_query(query, conn)
	for song in dat['url'].values:
		urllib.request.urlretrieve(song, '/home/host/myproject/static/music/batch1/{}_{}'.format(song.split("/")[-3], song.split('/')[-1]))
elif args.src == "sheets":
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
	client = gspread.authorize(creds)
	sheet = client.open('jukebox pipeline')
	sheet_instance = sheet.get_worksheet(1)
	records_data = sheet_instance.get_all_records()
	records_df = pd.DataFrame.from_dict(records_data)

	records_df = records_df.sample(frac=1).sort_values(['item'])
	songs = list(records_df['url'].values)

	for song in songs:
		try:
			urllib.request.urlretrieve(song, '/home/host/myproject/static/music/batch1/{}_{}'.format(song.split("/")[-3], song.split('/')[-1]))
		except:
			print("failed for song {}".format(song))
else:
	print("{} not supported".format(args.src))