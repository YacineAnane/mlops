# mlops
Ceci est un document pour vous aider à lancer notre application:

# Partie Kafka
- Lancez votre zookeeper et les servers properties
- Tapez la commande"python3 prediction.py" pour lancer la partie prédictione qui sera utilisée par kafka
- Tapez "streamlit run front.py" pour lancer le front de l'application qui vous permettra de de prédire sur des .csv et de récuperer ces prédictions
- Sur le streamlit vous pourrez choisir de .csv directement depuis votre ordinateur pour faire des prédictions dessus

# Partie Airflow
- Lancez dans 2 terminaux différents "airflow webserver" et "airflow scheduler" pour lancer l'UI de airlfow et voir les dags. Si l'UI Airflow vous demande un nom d'utilisiateur et un mot de passe, veuillez entrer la commande "airflow users create" pour créer un nouvel utilisateur que vous permettra d'accèder à cette page.
