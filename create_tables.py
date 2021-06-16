import psycopg2
import time
from creds import rds_username, rds_password, rds_url
from creds import rds_port, rds_db


conn = psycopg2.connect(
    host=rds_url,
    port=rds_port,
    dbname=rds_db,
    user=rds_username,
    password=rds_password)

conn.set_session(autocommit=True)

songs = """
    CREATE TABLE afm_songs_prod (
        time_stamp      timestamp,
        song_id         varchar(256),
        run_id          varchar(256),
        genre           varchar(256),
        artist          varchar(256),
        dna             varchar(256),
        dna_artist      varchar(256),
        url             varchar(256),
        meta            varchar(256)
    );
    """

ratings = """
    CREATE TABLE afm_ratings_prod (
        time_stamp      timestamp,
        song_id         varchar(256),
        user_id         varchar(256),
        question        varchar(256),
        answer          varchar(256),
        sequence        varchar(256),
        elapsed         float(10),
        meta            varchar(256)
    );
    """

path = """
    CREATE TABLE afm_path (
        time_stamp      timestamp,
        song_id         varchar(256),
        user_id         varchar(256),
        song_order      float(10),
        pref_novelty    varchar(256),
        pref_happy      varchar(256),
        pref_danceable  varchar(256),
        pref_artifical  float(10),
        pref_upbeat     varchar(256)
    );
    """

songs_cov = """
    CREATE TABLE afm_songs_cov_prod (
        time_stamp      timestamp,
        song_id         varchar(256),
        run_id          varchar(256),
        genre           varchar(256),
        artist          varchar(256),
        dna             varchar(256),
        dna_artist      varchar(256),
        url             varchar(256),
        meta            varchar(256),
        danceability_genre            float(10),
        energy_genre            float(10),
        key_genre            float(10),
        loudness_genre            float(10),
        speechiness_genre            float(10),
        acousticness_genre            float(10),
        instrumentalness_genre            float(10),
        liveness_genre            float(10),
        valence_genre            float(10), 
        danceability_artist            float(10),
        energy_artist            float(10),
        key_artist            float(10),
        loudness_artist            float(10),
        speechiness_artist            float(10),
        acousticness_artist            float(10),
        instrumentalness_artist            varchar(256),
        liveness_artist            float(10),
        valence_artist            float(10),
        danceability_dna_artist            float(10),
        energy_dna_artist            float(10),
        key_dna_artist            float(10),
        loudness_dna_artist            float(10),
        speechiness_dna_artist            float(10),
        acousticness_dna_artist            float(10),
        instrumentalness_dna_artist            float(10),
        liveness_dna_artist            float(10),
        valence_dna_artist            float(10)
    );
    """

if __name__ == '__main__':
    cur = conn.cursor()
    # cur.execute("DROP TABLE afm_songs;")

    cur.execute(songs_cov)
    #cur.execute(ratings)
    # cur.execute(path)
    
    conn.commit()
    cur.close()
    conn.close()