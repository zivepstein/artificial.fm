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
    CREATE TABLE afm_songs (
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
    CREATE TABLE afm_ratings (
        time_stamp      timestamp,
        song_id         varchar(256),
        user_id         varchar(256),
        question        varchar(256),
        answer          varchar(256),
        meta            varchar(256)
    );
    """



if __name__ == '__main__':
    cur = conn.cursor()
    #cur.execute("DROP TABLE gg_view;")

    cur.execute(songs)
    cur.execute(ratings)
    
    conn.commit()
    cur.close()
    conn.close()