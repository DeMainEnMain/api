#!/bin/bash
set -x
set -e

LOGIN_PASS="demainenmain:Tinda"
CYCLOS_URL="http://sauvagnon.acacs.org:8080/cyclos"


PASS=`echo -n $LOGIN_PASS | base64`

until [ `curl --silent --write-out '%{response_code}' -o /dev/null $CYCLOS_URL/global/` -eq 200 ];
do
  echo '--- waiting for Cyclos to be fully up (10 seconds)'
  sleep 10
done

if [ ! -f ./cyclos_constants.yml ]; then
    python3 setup.py --debug $CYCLOS_URL $PASS
    python3 init_test_data.py --debug $CYCLOS_URL $PASS
else
	echo "File present"
fi

exec "$@"


# This is how I launch this script (in dev):
# docker-compose exec api bash /cyclos/setup_cyclos.sh

# This cd will do this: cd /cyclos/
#~ cd "${0%/*}"
#~ 
#~ echo $PWD
#~ 
#~ rm -f cyclos_constants.yml
#~ 
#~ # Base64('admin:admin') = YWRtaW46YWRtaW4=
#~ python setup.py http://cyclos-app:8080/ YWRtaW46YWRtaW4=
#~ python init_static_data.py http://cyclos-app:8080/ YWRtaW46YWRtaW4=
