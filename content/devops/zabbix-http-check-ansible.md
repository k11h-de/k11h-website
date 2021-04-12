Title: zabbix http/s checks from yaml dict
Date: 2021-04-11 14:12
Tags: ansible, zabbix, gitlab, monitoring
slug: zabbix-http-check-ansible

# why

to maintain the principle of configuration-as-code this tools helps to bulk create and update http/s checks from your zabbix server

imagine you need to monitor many different http/s microservice endpoints      
you can create them using the zabbix gui, or note them down in a simple yaml dict.
this automation uses ansible to utilize the zabbix api to create zabbix http/s checks with graphs and alert trigger

```yaml
health_checks:
    - check_url:              "https://www.example.com/blog/"
    - check_url:              "https://api.example.com/endpoint/search?query=token"
      check_searchstring:     "Results for: token"
    - check_url:              "https://api.example.com/long/running/api"
      check_timeout:          "10s"
    - check_url:              "https://api.example.com/special/returncode"
      check_returncode:       "200,206"
    - check_url:              "https://static.example.com/images/"
```

# source

the sources, documentation and examples are located [here](https://github.com/k11h-de/zabbix-http-ansible){:target="_blank"}