# Deploying the OSKAR website

## Requirements

[Ansible](http://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
- Can be installed with`pip install ansible`


## VirtualBox: Centos 7 VM

### Centos 7 VirtualBox VM

__Install dependencies:__

- <https://www.virtualbox.org/wiki/Downloads>
- <https://www.vagrantup.com/downloads.html>

__Create a Centos 7 VM and ssh into it:__

```bash
cd deploy
vagrant up
vagrant ssh
```

_Note is is also possible to ssh into the vm with the commands:_

```bash
ssh vagrant@192.168.199.100 -i .vagrant/machines/default/virtualbox/private_key
ssh vagrant@127.0.0.1 -p 2222 -i .vagrant/machines/default/virtualbox/private_key
```

__Set up the VM:__

```bash
ansible-playbook -i [inventory file] --private-key=[key file] site.yml
```

If using the VirtualBox Centos 7 VM the `[inventory file]` should be 
`hosts.vagrant` and the `[key file]` should be
`vagrant/machines/default/virtualbox/private_key`. For example:

```bash
ansible-playbook -i hosts.vagrant --private-key=.vagrant/machines/default/virtualbox/private_key site.yml
```

For more details on Ansible inventory files see
<http://docs.ansible.com/ansible/latest/intro_inventory.html>.

__To tear down and clean up the VM:__

```bash
vagrant destroy -f
```



### Stress testing with `ab`

`ab` is the Apache HTTP server benchmarking tool and can be used as follows:

```bash
ab -n 500 -c 100 http://192.168.199.100:8000/
```

Where:

* `-n` is the number of requests
* `-c` is the request concurrency



## Production VM

__TODO__
