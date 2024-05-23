# streaming-04-multiple-consumers
> Executed by: A. C. Coffin | Completed on: May 2024 | NW Missouri State University | CSIS: 44671-80| Dr. Case |
> Use RabbitMQ to distribute tasks to multiple workers

# Overview:
 This project explores the use of multiple Consumers with a single Producer as it handled a csv file. Each of the tasks, is layed out within the file and is to be exicuted by multiple "workers" or consumer scripts that are consuming the producer's output. Unlike the example above these are not filtering through the data, but simply working through the streams. This project contains two sample scripts and thrid custom script designed to output to multiple consumers. 
 
 One process will create task messages. Multiple worker processes will share the work. 

  Prior to running this project read [RabbitMQ Tutorial - Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html) and review the code and comments in this repo.

## Screenshot

See a running example with at least 3 concurrent process windows here:
![Hitchhiker's Guide to the Galaxy on multiple consumers](Screenshots/v3Run3Listen1EmHitchhiker.PNG)

Each of the Consumers has numbers corresponding to the row number in the attached tasks.csv. 
Let's see who can identify the book being referenced... I'll give you a hint, What's the answer to life?

# Table of Contents
1. [File List](File_List)
2. [Machine Specs & Terminal Information](Machine_Specs_&_Terminal_Information)
3. [Prerequisites](Prerequisites)
4. [Before you Begin](Before_you_Begin)
5. [Creating Enviroments & Installs](Creating_Enviroments_&_Installs)
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

# 2. Machine Specs & Terminal Information
This project was completed using a Windows OS computer with the following specs. These are not required to run this repository. For further details see util_about.txt and aboutenv.txt in the utils_outputs located in the utils folder.

 * Operating System: nt Windows 10
 * System Architecture: 64bit
 * Number of CPUs: 12
 * Machine Type: AMD64
 * Python Version: 3.11.4
 * Python Build Date and Compiler: tags/v3.11.4:d2340ef with Jun  7 2023 05:45:37
 * Python Implementation: CPython
 * Active pip environment:   None
 * Active conda environment: None
 * Terminal Environment:        VS Code
 * Terminal Type:               cmd.exe
 * Preferred command:           python

# 3. Prerequisites
1. Git
2. Python 3.7+ (3.11+ preferred)
3. VS Code Editor
4. VS Code Extension: Python (by Microsoft)
5. RabbitMQ Server Installed and Running Locally
6. Anaconda Installed

# 4. Before you Begin

1. Fork this starter repo into your GitHub.
2. Clone your repo down to your machine.
3. View / Command Palette - then Python: Select Interpreter
4. Select your conda environment. 


# 5. Creating Enviroments & Installs
Befor beginning this project two enviroments were made, one as a VS Code Enviroment and the other as an Anaconda Enviroment. RabbitMQ requires the Pika Library in order to function, to ensure that the scripts exicute create an enviroment in either VS Code or Anaconda.

VS Code Enviroments allow us to create the virtual enviroment within the workspace as a way to isolate python projects with its own pre-installed packages and interpreter. For light projects this is optimal ias VS Code enviroments will not touch other enviroments or python installations. However, pre-installed packages can be limited, and the enviroments will only stay within the folder that is selected. Meaning that you can't simply call in another enviroment. The second method of creating an Anaconda Enviroment is different as it's designed for a heavier work load and is robust. This particular method cereates an specific reusable enviroment with specific Python versiions and pre-installed packages. However, this method can be heavier due to the additional packages.

While the Anaconda Enviroment is not necessary for this project it was utilized to ensure that the enviroments between VS Code and Anaconda were consistant when running the v1 and v2 emitters in VS Code with the v1 and v2 listening scripts running in Anaconda.

## 5a. Creating VS Code Enviroment
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

## 5b. Creating Anaconda Enviroment
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


# RabbitMQ Admin 

RabbitMQ comes with an admin panel. When you run the task emitter, reply y to open it. 

(Python makes it easy to open a web page - see the code to learn how.)

# Executing the Code

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

# Creating v3 Scripts

# Results


## Reference

- [RabbitMQ Tutorial - Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)


