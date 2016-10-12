
** DEPS for backend.py **

# sudo apt-get install libpq-dev python-dev libffi-dev python3-gi
-> Create virtualenv with system-packages (e.g. mkvirtualenv backend --system-site-packages -p /usr/bin/python3). This is required for pydbus
# pip install  cached_property
# pip install -r python/requirements.txt

** DEPS for play.py **
pip install -r python/requirements-play.txt
** Check **

# cd python
# python backend.py --instance-meta-dir /home/ab/git/openslides_ansible/tmp/meta --versions-meta-dir /home/ab/git/openslides_ansible/tmp/meta
# curl -H 'Content-Type: application/vnd.api+json' http://127.0.0.1:5000/api/versions | json_pp
# curl -X POST --data-binary @example_instance.json -H 'Content-Type: application/vnd.api+json' http://127.0.0.1:5000/api/instances | json_pp


** Host System Setup **

- Install rkt

# sudo aptitude install postgresql nginx
# sudo mkdir /etc/nginx/locations

*** Add admin user in postgresql ***
CREATE USER openslides_admin WITH PASSWORD 'asdf';
ALTER USER openslides_admin WITH SUPERUSER;

*** Add generated locations to nginx ***

-> include /etc/nginx/locations/*.locations;


** Add OpenSlides version **

1. get docker image rkt --insecure-options=image fetch docker://openslides/openslides#2.1
2. copy sha512 hash
3. create file for version, e.g. /srv/multi-instance/meta/openslides_version_2_1.json
{
  "id": "2.1",
  "image": "sha512-<<HASH FOR STEP 2>>"
}
4. copy static files in /srv/openslides/static/2.1
