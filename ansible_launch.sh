ansible-playbook instances_spawn.yml --private-key ~/.ssh/amichaud_xebia.pem -v && \
inventory/ec2.py --refresh-cache && \
ansible-playbook instances_config.yml --private-key ~/.ssh/amichaud_xebia.pem -i inventory/ec2.py -v
