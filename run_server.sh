# run_server.sh
xsudo pkill gunicorn
gunicorn -b 127.0.0.1:8000 wsgi:app \
         --reload \
         --certfile ./fullcert.pem \
         --keyfile ./privkey.pem

