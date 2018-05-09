# TODO

See: <https://github.com/paste/fvang>
<https://medium.com/ymedialabs-innovation/deploy-flask-app-with-nginx-using-gunicorn-and-supervisor-d7a93aa07c18>
<https://medium.com/@jgefroh/a-guide-to-using-nginx-for-static-websites-d96a9d034940>
- <https://www.linode.com/docs/web-servers/nginx/how-to-configure-nginx/>
- <https://www.nginx.com/blog/nginx-se-linux-changes-upgrading-rhel-6-6/>
- <https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-centos-7>

- [ ] add oskar.service systemd using ansible.
      see systemd service on vm and <http://docs.ansible.com/ansible/latest/modules/systemd_module.html>
      eg. <https://stackoverflow.com/questions/35984151/how-to-create-new-system-service-by-ansible-playbook>

- [ ] configure and start nginx using ansible
        - copy or copy using template nginx.conf to vm
        - restart nginx service
        <https://www.linode.com/docs/web-servers/nginx/how-to-configure-nginx/>

-