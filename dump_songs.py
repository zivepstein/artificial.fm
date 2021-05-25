from flask import Flask, render_template, request, redirect,url_for, jsonify,copy_current_request_context, send_from_directory, Markup, session
import gspread
import urllib.request
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import random, string
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
    urllib.request.urlretrieve(url, '/home/host/myproject/static/music/batch1/{}'.format(.url.split('/')[-1]))