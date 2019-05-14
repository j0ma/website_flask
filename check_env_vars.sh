ERROR_MSG="Make sure both CERTBOT_KEYFILE and CERTBOT_CERTFILE exist as environment variables!"
if [ -z $CERTBOT_KEYFILE ]; then
  echo $ERROR_MSG
  exit 0
elif [ -z $CERTBOT_CERTFILE ]; then
  echo $ERROR_MSG
  exit 0
else
  exit 1
fi
