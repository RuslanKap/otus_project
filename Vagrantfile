# Vagrantfile
Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-20.04"

  # nginx: Reverse-proxy (nginx)
  config.vm.define "nginx" do |nginx|
    nginx.vm.hostname = "nginx"
    nginx.vm.network "private_network", ip: "192.168.56.11"
#     nginx.vm.network "forwarded_port", guest: 80, host: 80
#     nginx.vm.network "forwarded_port", guest: 443, host: 443
    nginx.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
      vb.cpus = 1
    end
    nginx.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbooks/nginx.yml"
    end
  end

  # app: Frontend + Backend
  config.vm.define "app" do |app|
    app.vm.hostname = "app"
    app.vm.network "private_network", ip: "192.168.56.12"
#    app.vm.synced_folder "./app", "/vagrant/app"
    app.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
      vb.cpus = 1
    end
    app.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbooks/app.yml"
    end
  end

  # pgmaster: PostgreSQL Master
  config.vm.define "pgmaster" do |pgmaster|
    pgmaster.vm.hostname = "pgmaster"
    pgmaster.vm.network "private_network", ip: "192.168.56.13"
    pgmaster.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
      vb.cpus = 1
    end
    pgmaster.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbooks/pgmaster.yml"
    end
  end

  # pgslave: PostgreSQL Slave
  config.vm.define "pgslave" do |pgslave|
    pgslave.vm.hostname = "pgslave"
    pgslave.vm.network "private_network", ip: "192.168.56.14"
    pgslave.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
      vb.cpus = 1
    end
    pgslave.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbooks/pgmaster.yml"
    end
  end

  # barman
  config.vm.define "barman" do |barman|
    barman.vm.hostname = "barman"
    barman.vm.network "private_network", ip: "192.168.56.15"
    barman.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
      vb.cpus = 1
    end
    barman.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbooks/barman.yml"
    end
  end

  # elk: ELK
  config.vm.define "elk" do |elk|
    elk.vm.hostname = "elk"
    elk.vm.network "private_network", ip: "192.168.56.16"
    elk.vm.network "forwarded_port", guest: 5601, host: 5601  # Kibana
    elk.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
      vb.cpus = 2
    end
    elk.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbooks/elk.yml"
    end
  end

  # grafana: grafana
  config.vm.define "grafana" do |grafana|
    grafana.vm.hostname = "grafana"
    grafana.vm.network "private_network", ip: "192.168.56.17"
    grafana.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
      vb.cpus = 1
    end
    grafana.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbooks/grafana.yml"
    end
  end
end