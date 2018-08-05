# run_service.sh
#python src/endpoint.py --corpus_path='./data/enron_corpora_final.pkl'
sudo pkill gunicorn
#git pull
gunicorn -b 127.0.0.1:8000  wsgi:app --reload
