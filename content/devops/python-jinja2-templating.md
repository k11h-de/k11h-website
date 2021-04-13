Title: Simple Jinja2 templating script
Date: 2021-01-14 08:12
Tags: python, jinja2
slug: python-jinja2-templating

### motivation

What I really love about Ansible is it's powerful templating capabilities.   
It all boils down to the jinja2 templating engine, so I wrote a small script for just that part.

In this example I am using Jinja2 templating to generate a `.ssh/config` file from a yaml dict


```python
#!/usr/bin/python3 

# run.py example/vars.yaml example/ssh_config.j2 [out.txt]

from jinja2 import Template
import yaml, sys
# load yaml vars file
yaml = yaml.safe_load(open(str(sys.argv[1]), 'r'))
# load jinja2 template file
template = Template(open(str(sys.argv[2])).read())
# if no out file was provided
if len(sys.argv) == 3:
    # print to stdout
    print(template.render(yaml))
# if outfile was provided
elif len(sys.argv) == 4:
    # write result to output file
    with open(str(sys.argv[3]), 'w') as f:
        print(template.render(yaml), file=f)
```

#### source

the sources, documentation and examples are located [here](https://github.com/k11h-de/jinja2-templating){:target="_blank"}