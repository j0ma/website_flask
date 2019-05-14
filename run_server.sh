# run_server.sh
xsudo pkill gunicorn
gunicorn -b 127.0.0.1:8000 wsgi:app \
         --reload \
         --certfile ./fullchain.pem \
         --keyfile ./privkey.pem

