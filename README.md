# streaming-04-multiple-consumers
> Executed by: A. C. Coffin | Completed on: May 2024 | NW Missouri State University | CSIS: 44671-80| Dr. Case |
> Use RabbitMQ to distribute tasks to multiple workers

# Overview:

 The amount of data available to us is staggering, so much so that in many cases when we have a singular question about a smaller set within the data may become construed. Imagine sitting in a food court at lunch time in a busy mall, there are 15 restaurants to get food, we know each customer there will order food (Consumer) and that each shop (Producer) will make thier order. While all of these restaurants are in the food court, we are only interested in those that make a particular dish. So lets say we want to learn how many people purchase food at the food court, we can do that with a single producer and consumer combo - however, this process would be very slow. The reason being that there are 12 different menus to contend with - each of them serving food to customers. The challenge becomes keeping track of all the orders and how much food is produced. 
 
 When determining how much food is produced we can create several consumers to comb through the data, and process certain restaurants. For example we want to know how much Sushi is being sold, and how many burgers are being made by two different restaurants in the food court. We can do this by tasksing consumers with specific algorythems to retrieve the data. So the customer that orders sushi will get suish, while the customer who ordered a burger gets a burger - our code acts the same. 
 
 This project explores the use of multiple Consumers with a single Producer as it handled a csv file. Each of the tasks, is layed out within the file and is to be exicuted by multiple "workers" or consumer scripts that are consuming the producer's output. Unlike the example above these are not filtering through the data, but simply working through the streams. This project contains two sample scripts and thrid custom script designed to output to multiple consumers. 
 
 One process will create task messages. Multiple worker processes will share the work. 

# Table of Contents
1. [File List](File_List)
2. [Machine Specs & Terminal Information](Machine_Specs_&_Terminal_Information)
3. [Creating Enviroments & Installs](Creating_Enviroments_&_Installs)
    * [Creating VS Code Enviroment](Creating_VS_Code_Enviroment)
    * [Creating Anaconda Enviroment](Creating_Anaconda_Enviroment)

# 1. File List
| Support Files | | | Producer/Consumer Scripts | | | Screen Shots | | |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| File Name | Repo Location | Type | File Name | Repo Location | Type | File Name | Repo Location | Type |
| util_about.py | utils folder | python script | v1_emitter_of_tasks.py| main repo | python script | AddingPika1.png | Screenshots folder | PNG |
| util_aboutenv.py | utils folder | python script | v1_listening_wroker.py | main repo | python script | enviromentcondacreateRabbitEnv.png | Screenshots folder | PNG |
| util_logger.py | utils folder | python script | v2_ emitter_of_tasks.py | main repo | python script | packageinstallpika.png | Screenshots folder | PNG |
| aboutenv. txt | util_outputs folder | text | v2_listening_work.py | main repo | python script | runofv1andv2.PNG | Screenshots folder | PNG |
| util_about.txt | util_outputs folder | text | v3_emitter of tasks.py | main repo | python Script | v3Run3Listen1EmHitchhiker.png | Screenshots | PNG |
| v1_emitter_of_tasks.log | logs folder | log | v3_listenin_worker.py | main repo | python script | v3Run3Listen1Emit.png | Screenshots | PNG |
| v1_listening_worker.log | logs folder | log | requirements.txt | main repo | text |
| v3_emitter_of_tasks.log | logs folder | log |  tasks.csv | mainrepo | CSV |
| v3_litenin_worker.log | logs folder | log |




# 3. Creating Enviroments & Installs
Befor beginning this project two enviroments were made, one as a VS Code Enviroment and the other as an Anaconda Enviroment. RabbitMQ requires the Pika Library in order to function, to ensure that the scripts exicute create an enviroment in either VS Code or Anaconda.

VS Code Enviroments allow us to create the virtual enviroment within the workspace as a way to isolate python projects with its own pre-installed packages and interpreter. For light projects this is optimal ias VS Code enviroments will not touch other enviroments or python installations. However, pre-installed packages can be limited, and the enviroments will only stay within the folder that is selected. Meaning that you can't simply call in another enviroment. The second method of creating an Anaconda Enviroment is different as it's designed for a heavier work load and is robust. This particular method cereates an specific reusable enviroment with specific Python versiions and pre-installed packages. However, this method can be heavier due to the additional packages.

While the Anaconda Enviroment is not necessary for this project it was utilized to ensure that the enviroments between VS Code and Anaconda were consistant when running the v1 and v2 emitters in VS Code with the v1 and v2 listening scripts running in Anaconda.

## Creating VS Code Enviroment
To create a local Python virtual enviroment to isolate our project's third-party dependencies from other projects. Use the following commands to create an enviroment, when promted in VS Code set the .venv to a workspace folder and select yes. 

```
python - m venv .venv # Creates a new enviroment
.venv\Scripts\activate # Activates the new enviroment
```

Once the enviroment is created install the following:
```
python -m pip install -r requirements.txt
```
For more information on Pika see the [Pika GitHub](https://github.com/pika/pika)

## Creating Anaconda Enviroment
To create an Anaconda enviroment open an Anaconda Prompt, the first thing that will pop up is the base. Then we are going to locate our folder, to do this type the following:

```
cd \Dcuments\folder_where_repo_is\ 
cd \Documents\ACoffinCSIS44671\streaming-04-multiple-consumers # This is where the file is located in my computer
```
Once the folder has been located the line should look like this:
```
(base) C:\Users\Documents\folder_where_repo_is\streaming-04-multiple-consumers>
(base) C:\Users\Tower\Documents\ACoffinCSIS44671\streaming-04-multiple-consumers> # My File Path
```

To create an enviroment do the following:
```
conda create -n RabbitEnv # Creates the Enviroment
conda activate RabbitEnv # Activates Enviroment
```
This will create the enviroment, if you want to deactivate it just enter:
`conda deactivate`

Once the enviroment is created exicute the following:

```
python --version # Indicates Python Version Installed
conda config --add channels conda-forge # connects to conda forge
conda config --set channel_priority strict # sets priority
install pika # library installation
```
Be sure to do each of these in order indifidually in order to install pika in the enviroment. You have to use the forge to do this with Anaconda.

![Pika installation into enviroment](Screenshots/AddingPika1.PNG)   

## Before You Begin

1. Fork this starter repo into your GitHub.
1. Clone your repo down to your machine.
1. View / Command Palette - then Python: Select Interpreter
1. Select your conda environment. 

Notes: Remember to create enviroment and install pika. Always be sure that RabbitMQ is running before attempting the tasks listed. Add notes on creating an enviroment in Anaconda this time.

Added logger, cover paths to retrieve logger.

## Read

1. Read the [RabbitMQ Tutorial - Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)
1. Read the code and comments in this repo.

## RabbitMQ Admin 

RabbitMQ comes with an admin panel. When you run the task emitter, reply y to open it. 

(Python makes it easy to open a web page - see the code to learn how.)

## Execute the Producer

1. Run emitter_of_tasks.py (say y to monitor RabbitMQ queues)

Explore the RabbitMQ website.

## Execute a Consumer / Worker

1. Run listening_worker.py

Will it terminate on its own? How do you know? 

## Ready for Work

1. Use your emitter_of_tasks to produce more task messages.

## Start Another Listening Worker 

1. Use your listening_worker.py script to launch a second worker. 

Follow the tutorial. 
Add multiple tasks (e.g. First message, Second message, etc.)
How are tasks distributed? 
Monitor the windows with at least two workers. 
Which worker gets which tasks?


## Reference

- [RabbitMQ Tutorial - Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)


## Screenshot

See a running example with at least 3 concurrent process windows here:
