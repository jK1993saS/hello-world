import requests
#import postgresql
import schedule
import time
from requests.exceptions import HTTPError
import sqlalchemy.dialects.postgresql
import psycopg2
from psycopg2 import Error

weekWeather = []
date = []
url = 'https://api.weather.yandex.ru/v1/forecast?lat=55.75396&lon=37.620393&extra=true'

def job():
    print("I'm working...")
    #db = sqlalchemy.dialects.postgresql.open('pq://postgres:SaSOpen.@localhost:5432/db_value')

    # try:
    #     connection = psycopg2.connect(user = "postgres",
    #                                   password = "SaSOpen.",
    #                                   host = "localhost",
    #                                   port = "5432",
    #                                   database = "postgres")
    
    #     cursor = connection.cursor()
    #     # Print PostgreSQL Connection properties
    #     print ( connection.get_dsn_parameters(),"\n")
    
    #     # Print PostgreSQL version
    #     cursor.execute("SELECT version();")
    #     record = cursor.fetchone()
    #     print("You are connected to - ", record,"\n")

    # except (Exception, psycopg2.Error) as error :
    #     print ("Error while connecting to PostgreSQL", error)
    # finally:
    # #closing database connection.
    #     if(connection):
    #         cursor.close()
    #         connection.close()
    #         print("PostgreSQL connection is closed")

    connection = psycopg2.connect(user = "postgres",
                                  password = "SaSOpen.",
                                  host = "localhost",
                                  port = "5432",
                                  database = "postgres")
    
    try:
        response = requests.get(url, params={'X-Yandex-API-Key': '0d6a9c75-6d54-486f-9c6a-1644d58b4661'})
        json_response = response.json()
        forecasts = 'forecasts'

        for forecast in json_response[forecasts]:
            weekWeather.append(forecast['parts']['day']['temp_avg'])
            date.append(forecast['date'])

        response.raise_for_status()
        connection.execute("INSERT INTO weather (date, temperature1, temperature2, temperature3, temperature4, temperature5, temperature6, temperature7) VALUES ('" + date[0] + "', "+str(weekWeather[0])+","+str(weekWeather[1])+","+str(weekWeather[2])+","+str(weekWeather[3])+","+str(weekWeather[4])+","+str(weekWeather[5])+","+str(weekWeather[6])+")")

    except (Exception, psycopg2.Error) as error:
        print ("Error while connecting to PostgreSQL", error)
        
schedule.every().day.at("20:44").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
