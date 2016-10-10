
** DEPS **

sudo apt-get install libpq-dev python-dev libffi-dev

pip install -r python/requirements.txt


** Check **

# cd python
# python backend.py --instance-meta-dir /home/ab/git/openslides_ansible/tmp/meta --versions-meta-dir /home/ab/git/openslides_ansible/tmp/meta
# curl -H 'Content-Type: application/vnd.api+json' http://127.0.0.1:5000/api/versions | json_pp
# curl -X POST --data-binary @example_instance.json -H 'Content-Type: application/vnd.api+json' http://127.0.0.1:5000/api/instances | json_pp


** Host System Setup **

# sudo aptitude install postgresql nginx
# sudo mkdir /etc/nginx/locations

CREATE USER openslides_admin WITH PASSWORD 'asdf';
ALTER USER openslides_admin WITH SUPERUSER;
