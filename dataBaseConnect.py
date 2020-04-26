# import sqlalchemy.dialects.postgresql
import psycopg2


class ConnectDB:

    @staticmethod
    def connect():
        connection = psycopg2.connect(user = "postgres",
                                  host = "localhost",
                                  port = "5432",
                                  database = "postgres")
        return connection

    @staticmethod
    def executiv(date, weather1, weather2, weather3, weather4, weather5, weather6, weather7):
        return "INSERT INTO weather (date, temperature1, temperature2, temperature3, temperature4, temperature5, temperature6, temperature7) VALUES ('" + str(date) + "', " + str(
            weather1) + "," + str(weather2) + "," + str(weather3) + "," + str(weather4) + "," + str(
            weather5) + "," + str(weather6) + "," + str(weather7) + ")"
        
