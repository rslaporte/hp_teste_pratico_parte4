----------------------------------------
# House Performance - Teste Prático Parte 4
----------------------------------------

Este projeto faz parte da resolução da parte 4 do teste da House Performance. O script em Python consulta a API pública Open-Meteo (https://open-meteo.com/) e exporta alguns dados meteorológicos dos últimos 7 dias para um arquivo Excel (.xlsx) local. A seguir especifico as instruções para execução do mesmo.

----------------------------------------
REQUISITOS:
----------------------------------------
- Python 3.8 ou superior
- Acesso à internet

----------------------------------------
PASSO A PASSO PARA EXECUÇÃO:
----------------------------------------
1. Abra o terminal na pasta onde estão os arquivos.
2. Crie e ative um ambiente virtual:

   - Windows:
     
       python -m venv venv
     
       venv\Scripts\activate

   - macOS / Linux:
     
       python3 -m venv venv
     
       source venv/bin/activate

3. Instale as dependências:
   
       pip install -r requirements.txt

4. Execute o script:
   
       python app.py

----------------------------------------
RESULTADO:
----------------------------------------
O script criará um arquivo chamado "open_meteo_data.xlsx" contendo os dados climáticos horários dos últimos 7 dias para as localidades de Franca, Sâo Paulo, Porto Alegre e Rio de Janeiro.

----------------------------------------
OBSERVAÇÕES:
----------------------------------------
- O script já define as latitudes e longitudes das cidades especificadas;
- Os dados são todos obtidos diretamente da API pública do Open-Meteo https://open-meteo.com/, inclusive as coordenadas utilizadas;
- O arquivo de saída será salvo na mesma pasta do projeto.
