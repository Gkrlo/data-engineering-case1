# Aplazame Assignment

## Objectives
Extract a JSON file, apply some transformations and store the data in a RDB (PostGreSQL)
#### My approach
- Extract the JSON file and create 2 stage tables (payments and prepayments) with only "important" data (*Task 1*). 
- From those stage tables, create a some DW tables and also the summary tables (*task 2*) using a computing framework (Spark).
- Provide a playbook for created a "small" data platform (airflow, spark, porstgres) 
## How to run this?
1) Install Vagrant
You can install vagrant from this link [here](https://www.vagrantup.com/downloads.html)
2) Install VirtualBox
Same fron this link [here](https://www.virtualbox.org/wiki/Downloads)
3) Install Vagrant host Manager
```bash
$ vagrant plugin install vagrant-hostmanager
```
4) Install ansible
```bash
sudo apt update
sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible
```
5) Run the playbook
```bash
$ cd aplazame_playbook
$ vagrant up
```
6) Go for a coffee. You deserve it!  ;)
7) Go to http://aplazame1.vm:8080/admin/ to see the airflow UI

## Pipeline
The Pipeline is inside de folder `aplazame_dags` (image in images/pipeline.png)

![aplazame_pipeline](../blob/master/images/pipeline.png?raw=true)

## Python ETLS
The are just simple scripts inside the folder `aplazame_etls`. 
```bash
$ cd aplazame_etls
$ pipenv shell
$ pipenv install -r requirements.txt
```
## Apache Spark
The master is located at http://aplazame1.vm:9090  (image in `images/spark.png`)

![aplazame_spark](../blob/master/images/spark.png)


## PostgreSQL
For connecting to PostgresSQL.

![aplazame_postgres](../blob/master/images/postgres.png) (image in `images/postgres.png`)


## Technologies:
* [Apache Airflow](https://airflow.apache.org/)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
* [PostgreSQL](https://www.postgresql.org/)
* [Pandas](https://pandas.pydata.org)
* [SQLALchemy](https://www.sqlalchemy.org/)
* [Apache Spark](https://spark.apache.org/)


### Thanks :)