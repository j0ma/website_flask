# run_service.sh
#python src/endpoint.py --corpus_path='./data/enron_corpora_final.pkl'
pkill gunicorn
#git pull
gunicorn -b 0.0.0.0:80 wsgi:app --reload
