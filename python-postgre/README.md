# python-postgre example
This example covers to connect a Postgresql instance within the same namespace.
Some enviroment parameter configurations needed.

- Please provide the following params from env:
    - POSTGRE_HOSTNAME (**from configmap**)
    - POSTGRE_PORT (**from configmap**, default *5432*)
    - POSTGRE_DBNAME (**from configmap**)
    - POSTGRE_USERNAME (**from secret**)
    - POSTGRE_PASSWORD (**from secret**)

These parameters can be either provided from *Configmap*, *Secret* or directly injected from *Deploymentconfig* object.

