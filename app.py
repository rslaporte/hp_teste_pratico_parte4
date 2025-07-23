import requests
import pandas as pd
from datetime import datetime, timedelta

#Classe para gerenciar a Open-Meteo API. Esta API pode ser encontrada em https://open-meteo.com/en/docs
class OpenMeteo:
    def __init__(self):
        self.url = "https://archive-api.open-meteo.com/v1/archive"

    def get_data(self, lat, long, city, state):
        params = {
            "latitude": lat,
            "longitude": long,
            "end_date": datetime.today().date() - timedelta(days=2), #Fiz essa requisição em 23-07-2025. Neste dia, não haviam dados referentes aos dias 22 e 23 deste mesmo mês. Por este motivo, considerei 22-07-2025 como data final.
            "start_date": datetime.today().date() - timedelta(days=8), #7 dias antes da data final, incluindo esta última.
            "hourly": "temperature_2m,precipitation,cloudcover,relative_humidity_2m,rain,wind_speed_10m", #Métricas que aparecerão na tabela final, i.e. o dado que será extraído.
            "timezone": "America/Sao_Paulo" 
        }

        #Extraindo os dados usando uma requisição GET
        response = requests.get(self.url, params=params)

        #Formatando a resposta em no formato JSON
        data = response.json()

        #Transformando os dados em um DataFrame. É mais fácil manipular os dados dessa forma.
        df = pd.DataFrame(data['hourly']) #Extraindo todas as métricas
        df['time'] = pd.to_datetime(df['time']) # Formatando a coluna 'time'
        df['city'] = city #Setando uma dimensão para cidade
        df['state'] = state

        return df
    
    def save_data(self, df, file_name):
        df.to_excel(file_name, index=False)

#Algumas localizações escolhidas aleatoriamente para compor os dados
locations = [
    {
        "lat": -20.5386,
        "long": -47.4008,
        "city": "Franca",
        "state": "SP"
    },
    {
        "lat": -23.5475,
        "long": -46.6361,
        "city": "Sao Paulo",
        "state": "SP"
    },
    {
        "lat": -30.0328,
        "long": -51.2302,
        "city": "Porto Alegre",
        "state": "RS"
    },
    {
        "lat": -22.9064,
        "long": -43.1822,
        "city": "Rio de Janeiro",
        "state": "RJ"
    }
]

#Inicializando um DataFrame para receber todos os dados
df = pd.DataFrame({})

#Gerando o DataFrame final extraindo todos os dados de todas as localizações
for location in locations:
    df_location = OpenMeteo().get_data(**location)
    df = pd.concat([df, df_location]).reset_index(drop=True)

#Salvando os dados em formato .xlsx (planilha)
OpenMeteo().save_data(df, 'open_meteo_data.xlsx')


