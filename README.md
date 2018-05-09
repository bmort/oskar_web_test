# oskar_web_test

Experimental flask website for the OSKAR simulator

## References

- <https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-centos-7>
- <https://www.digitalocean.com/community/tutorials/how-to-deploy-python-wsgi-apps-using-gunicorn-http-server-behind-nginx>
- <https://stackoverflow.com/questions/49296539/nginx-permission-issues-on-centos-7-with-gunicorn-socket-in-systemd>
- <https://serverfault.com/questions/331256/why-do-i-need-nginx-and-something-like-gunicorn>

## Quickstart

### Deployment using a Centos 7 VirtualBox VM

##### Install dependencies:

- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](https://www.vagrantup.com/downloads.html)
- [Ansible](http://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) (`pip install ansible`)

#### Start a Centos 7 VM to host the website

```bash
vagrant up
```

#### SSH into the VM

```bash
vagrant ssh
```

or

```bash
ssh vagrant@192.168.199.100 -i .vagrant/machines/default/virtualbox/private_key
```

or

```bash
sss vagrant@127.0.0.1 -p 2222 -i .vagrant/machines/default/virtualbox/private_key
```

#### Provision the VM

```bash
ansible-playbook -i [inventory file] --private-key=[key file] site.yml
```

If using the VirtualBox Centos 7 VM the `[inventory file]` should be
`hosts.vagrant` and the `[key file]` should be
`vagrant/machines/default/virtualbox/private_key`.

For example:

```bash
ansible-playbook -i hosts.vagrant --private-key=.vagrant/machines/default/virtualbox/private_key site.yml
```

For more details on Ansible inventory files see
<http://docs.ansible.com/ansible/latest/intro_inventory.html>.

#### Destroy the VM

```bash
vagrant destroy -f
```


### Testing the flask app with the development server

SSH into the VM (see above) then:


```bash
cd oskar_web.git
export FLASK_APP=oskar_web/app.py
export FLASK_DEBUG=True
flask run --host 0.0.0.0
```

Then on the host machine, visit `192.168.199.100:5000` to connect to the Flask
app in the VM.

### Testing the flask app with gunicorn


SSH into the VM (see above) then:

```bash
cd oskar_web.git/oskar_web
gunicorn -c gunicorn.cfg.py wsgi
```

Then on the host machine, visit `192.168.199.100:8000` to connect to the Flask
app in the VM.


### Stress testing with `ab` (Apache HTTP server benchmarking tool)

```bash
ab -n 500 -c 100 http://192.168.199.100:8000/
```

* `-n` is the number of requests
* `-c` is the request concurrency