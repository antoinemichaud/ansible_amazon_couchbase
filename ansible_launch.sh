ansible-playbook instances_spawn.yml --private-key ~/.ssh/amichaud_xebia.pem
ansible-playbook instances_config.yml --private-key ~/.ssh/amichaud_xebia.pem -i inventory/ec2.py
