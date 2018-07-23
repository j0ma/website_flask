# run_service.sh
# Quick bash script for running the document retrieval service
#python src/endpoint.py --corpus_path='./data/enron_corpora_final.pkl'
pkill gunicorn
#git pull
gunicorn -b 0.0.0.0:8000 wsgi:app --reload
