rm -rf env
virtualenv env
source env/bin/activate
pip install -r testproject/requirements.txt
python testproject/manage.py generate_swagger swagger.json
