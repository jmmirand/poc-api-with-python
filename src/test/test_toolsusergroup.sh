SERVER_HOST=localhost
SERVER_PORT=5000

SERVER_URL="http://${SERVER_HOST}:${SERVER_PORT}"
HEADER_OPTION=" --header 'Content-Type: application/json' --header 'Accept: application/json'"
HEADER_OPTION_GET=" --header 'Accept: application/json'"


echo "LISTADO DE TOOLS GROUPS"

echo "${SERVER_URL}"
 
curl -X GET  "${SERVER_URL}/toolsusergroup/"

echo "CREO alm_basic GRUPO DE HERRAMIENTAS"

curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{ "toolsusergroupname": "alm_basic" }' "${SERVER_URL}/toolsusergroup/"

echo "CREO de nuevo alm_basic, DEIBER DAR ERROR"
curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{ "toolsusergroupname": "alm_basic" }' "${SERVER_URL}/toolsusergroup/"


echo "BORRAR el Grupo de Herrameintas alm_basic"
curl -X DELETE --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{ "toolsusergroupname": "alm_basic" }' "${SERVER_URL}/toolsusergroup/"


echo "CREO TOOL USER GRUPO PARA PRUEBAS"
curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{ "toolsusergroupname": "alm_basic" }' "${SERVER_URL}/toolsusergroup/"


