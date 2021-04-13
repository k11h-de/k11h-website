Title: Running Ansible inside Docker
Date: 2020-12-22 08:12
Tags: ansible, docker, bash
slug: ansible-in-docker

### why

Sometimes it is important to be independent from your local dev machines setup.    
I wrote a small wrapper script to run ansible tasks inside a docker container.

#### wrapper

```bash
#!/bin/bash
vault=~/.ansible-vault-pass
# check if argument was supplied
if [ $# -eq 0 ]
  then
    echo "No arguments supplied; usage: $0 'ansible-playbook playbook.yaml' # The QUOTES are important here! "
    exit 1
fi

if [ -f "$vault" ]; then
    docker container run -it --rm \
    -v $(pwd)/../:/data \
    -v $vault:/root/.ansible-vault-pass \
    -e ANSIBLE_VAULT_PASSWORD_FILE=/root/.ansible-vault-pass \
    cytopia/ansible:latest $1
else
    echo "$vault file does not exist."
fi
```
