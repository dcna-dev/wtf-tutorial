# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    config.vm.provider "virtualbox" do |virtualbox|
        virtualbox.customize [ "modifyvm", :id, "--cpus", "2" ]
        virtualbox.customize [ "modifyvm", :id, "--memory", "1024" ]
    end
    # node01
    config.vm.define "node01" do |node01|

        node01.vm.hostname = "node01.dcna.local"
        node01.vm.box = "centos/atomic-host"
        node01.vm.network "public_network", bridge: "wlan0", ip: "192.168.1.128", netmask: "255.255.255.0", gateway: "192.168.1.1", dns: "192.168.1.1" 
    end

    # node02
    config.vm.define "node02" do |node02|

        node02.vm.hostname = "node02.dcna.local"
        node02.vm.box = "centos/atomic-host"
        node02.vm.network "public_network", bridge: "wlan0", ip: "192.168.1.129", netmask: "255.255.255.0", gateway: "192.168.1.1", dns: "192.168.1.1" 
    end

    #node03
    config.vm.define "node03" do |node03|

        node03.vm.hostname = "node03.dcna.local"
        node03.vm.box = "centos/atomic-host"
        node03.vm.network "public_network", bridge: "wlan0", ip: "192.168.1.130", netmask: "255.255.255.0", gateway: "192.168.1.1", dns: "192.168.1.1" 
    end

    #node04
    config.vm.define "node04" do |node04|

        node04.vm.hostname = "node04.dcna.local"
        node04.vm.box = "centos/atomic-host"
        node04.vm.network "public_network", bridge: "wlan0", ip: "192.168.1.131", netmask: "255.255.255.0", gateway: "192.168.1.1", dns: "192.168.1.1" 
    end

    #node05
    config.vm.define "node05" do |node05|

        node05.vm.hostname = "node05.dcna.local"
        node05.vm.box = "centos/atomic-host"
        node05.vm.network "public_network", bridge: "wlan0", ip: "192.168.1.132", netmask: "255.255.255.0", gateway: "192.168.1.1", dns: "192.168.1.1" 
    end

    #node06
    config.vm.define "node06" do |node06|

        node06.vm.hostname = "node06.dcna.local"
        node06.vm.box = "centos/atomic-host"
        node06.vm.network "public_network", bridge: "wlan0", ip: "192.168.1.133", netmask: "255.255.255.0", gateway: "192.168.1.1", dns: "192.168.1.1" 
    end

    #node07
    config.vm.define "node07" do |node07|

        node07.vm.hostname = "node07.dcna.local"
        node07.vm.box = "centos/atomic-host"
        node07.vm.network "public_network", bridge: "wlan0", ip: "192.168.1.134", netmask: "255.255.255.0", gateway: "192.168.1.1", dns: "192.168.1.1" 
    end
end
