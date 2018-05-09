# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"

  config.vm.hostname = 'oskar-web-1'
  config.vm.network :private_network, ip: "192.168.199.100"

  config.vm.provider :virtualbox do |vb|
    vb.name = 'oskar-web-1'
    vb.memory = "2048"
    vb.cpus = 2
    # vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  end
end
