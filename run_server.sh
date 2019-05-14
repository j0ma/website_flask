# run_server.sh
run_flask_server () {
  sudo pkill gunicorn
  gunicorn -b 127.0.0.1:8000 wsgi:app \
           --reload \
           --certfile $CERTBOT_CERTFILE \
           --keyfile $CERTBOT_KEYFILE
}

./check_env_vars.sh || run_flask_server
