# python-example
Python Flask Framework example for OKD/Openshift S2I demo.

It can be used in some scenerios as follow:
 - Showing S2I mechanism:
    - How s2i isolates us from building source code, building image itself and pushing it to image registry.
    - It also provides *releated kubernetes objects* such as deployment/deployment config, build config, service, route etc.. So there is no need to write YAMLs anymore.
    - You can pick a diffrent version.

- It can be also used for having a zero-downtime example. 
  - Python code contains 15s initial delay.
  - That's why i put a simple tester shell script, which polls given url every 500ms period.

- You can show service loadbalancer's default behavior(round robin). 

Enjoy it..
