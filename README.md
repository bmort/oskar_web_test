# oskar_web_test

Experimental flask website for the OSKAR simulator

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
