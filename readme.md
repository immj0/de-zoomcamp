
### Instructions for running locally
Note that these depend on a number of pre-requisites such as Docker Desktop, Anaconda (for Python and Jupyter), Terraform, gcloud CLI.
In addition I also use Git Bash.
For GCP, there must be a Project created, a Service Account, and the gcloud CLI must be authenticated.

## Start Postgres and PGAdmin locally
* Start docker desktop
* Start a git bash terminal in the folder containing the docker-compose file
* Use the command "docker-compose up -d" to start the containers and volumes described in docker-compose.yml
* In browser open http://localhost:8080/browser/
* Log in using the credentials in the docker-compose file
* Register the server through the pgadmin interface, also using credentials in the docker-compose file

## Open the jupyter notebook for data ingestion
* Open an Anaconda Prompt and cd to the folder containing ingestion-notebook.ipynb
* Use the command "jupyter notebook"
* Browser should automatically open http://localhost:8888/tree
* Select ingestion-notebook.ipynb to open it in a new tab: http://localhost:8888/notebooks/ingestion-notebook.ipynb
* In the menu at the top of the page, select Cell > Run All 
* Wait until all cells have been run. At this point, the data should have been loaded into the ny_taxi database

## View ingested data in Posgres DB and run queries for homework questions
* In pgadmin interface, refresh ny_taxi database in the left hand pane
* Expand ny_taxi > Schemas > public > Tables to observe the two tables of data
* In the pgadmin interface open Tools > Query Tool to open an interface that will execute SQL against the database
* Copy the text from homework-questions-sql-script.txt into the Query tool SQL editor, then run to get the answers 

## Use Terraform to provision cloud infrastructure
* Start a git bash terminal in the folder and cd into the terraform folder
* Use the command "terraform init"
* Use the command "terraform plan", entering the GCP project id when prompted
* Use the command "terraform apply", entering the GCP project id when prompted. This sets up the infrastructure defined in the file main.tf
