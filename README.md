# IS 601 - Project 4

## Project Description
This project's goal to build a Flask Application by following [this tutorial](https://hackersandslackers.com/your-first-flask-application).

This repository contains many independent projects. There is one folder for each part of the tutorial and a `my-final-project` folder for modifying 
[Project 3](https://github.com/tomtom28/njit-is-601-project-3) to include authentication and `ENV` variables in the Dockerfiles.

Each project runs independently in its own Docker container and on its own port number, as provided in the `docker-compose.yml` file.


## Note to Graders
Most of the tutorials were completed, however, I ultimately decided to modify Project 3 and add user authentication.
So, please refer to [my_final_project](/my-final-project/my_final_project) folder and treat that as the final submission.


## Setup
The following prerequisites are needed to run this project:
   * Docker Desktop (available [here](https://www.docker.com/products/docker-desktop))
   * Pycharm Professional by Jetbrains (available [here](https://www.jetbrains.com/pycharm/download/))

After you clone down this repo, you should the following in Pycharm:
   * Open this repo as an existing project, and ensure Docker is running.
   * Configure the Python Interpreter using `Docker Compose` and by pointing to the `docker-compose.yml` file. 
     * You should select the `final` Docker configuration for the interpreter to use.
     * More information can be found [here](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#add_new_project_interpreter).
   * Create a Run Time Configuration using `Docker-Compose` and by pointing to the `docker-compose.yml` file. 
     * More information can be found [here](https://www.jetbrains.com/help/pycharm/run-debug-configuration.html)
   * Once the run time configuration, press the green play button. This will automatically seed the `my-final-project/my_final_project/db/init.sql` inside Project 4.
   * While the project is running PyCharm, you can navigate to `http://localhost:8080/signup` to create a user account and test the application.
