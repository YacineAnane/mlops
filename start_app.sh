pip install -r requirements.txt
python3 data/generate_random_data 5
python3 prediction.py &
streamlit run front.py
