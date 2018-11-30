# [Experimental] New OSKAR website

Experimental Flask based website for the OSKAR simulator.

## Quickstart Guide

### Local development

**Create a virtualenv and install dependencies:**
```bash
virtualenv -p python3 venv
. venv/bin/activate
pip install -r oskar_web/requirements.txt
```

**Start the Website in a flask development server:**

```bash
./start_dev.sh
```

Once started, the local development website can be viewed at 
<http://localhost:8080>.

***Note**: As this has been started in development mode, changes to the code 
will be automatically loaded without the need to restart the website.*

## Testing with [Gunicorn](https://gunicorn.org/)

```bash
./start_gunicorn.sh
```

Once started, this can also be viewed at <http://localhost:8080>.

## Testing with Docker containers

__TODO__


## (Potentially) Useful links!

- <https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-centos-7>
- <https://www.digitalocean.com/community/tutorials/how-to-deploy-python-wsgi-apps-using-gunicorn-http-server-behind-nginx>
- <https://stackoverflow.com/questions/49296539/nginx-permission-issues-on-centos-7-with-gunicorn-socket-in-systemd>
- <https://serverfault.com/questions/331256/why-do-i-need-nginx-and-something-like-gunicorn>
