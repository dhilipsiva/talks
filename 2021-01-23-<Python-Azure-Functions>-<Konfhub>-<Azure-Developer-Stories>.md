<!--
$theme: gaia
template: invert
-->

# Python Azure Functions

## Azure Developer Stories

### KonfHub

## [@dhilipsiva](https://github.com/dhilipsiva)

---

- 10 years of experience in Python, JavaScript, DevOps & more
- Optimistic Nihilist.
- Wannabe Astrophysicist.
- I code for fun & profit.
- I love Science, Python, FOSS & fitness.
- Dad of 2. Environmentalist. Story Teller. Gamer.
- Jack of all trades & Master of none
- [http://dhilipsiva.com](http://dhilipsiva.com)
- [dhilipsiva@gmail.com](mailto:dhilipsiva@gmail.com)

---

# I have no idea what I am talking about :stuck_out_tongue_winking_eye:

---


#  Azure Functions

* Event-driven serverless compute platform
* On-demand service
* Provides a continually-updated infrastructure
* You can build web APIs, respond to database changes, process IoT streams, manage message queues, and more.
* Only worry about our app and not infrastructure
* Automatically scales

---

# Supported Languages

* ***Python***
* C#
* Go
* Java
* JavaScript / TypeScript
* PowerShell
* Rust
* Any other Language (Custom Image + PowerShell)

---

# Deployment Approaches

1. Commandline
2. VS Code (with an official azure plugin)

I will be taking the ***command line*** approach on my Debian machine as it's easier for me. So the rest of the talk will use this method.

If you are someone who likes to use GUI tools, you should probably opt for ***VS Code*** approach: https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python

---

# Prerequisites

* ***Azure Account*** : https://portal.azure.com/
* ***Azure Functions Core Tools*** : Used for creating projects & apps, testing Functions locally, deploying, logs, etc.
* ***Azure CLI*** : For managing Azure Cloud Reources
* ***Python 3.8 (or 3.7, 3.6)*** : Azure only supports Python 3.x

---

# Azure Functions Core Tools

Install the Microsoft package repository GPG key
```
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
```
Set up the APT source
```
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/debian/$(lsb_release -rs | cut -d'.' -f 1)/prod $(lsb_release -cs) main" > /etc/apt/sources.list.d/dotnetdev.list'
```
Install the Core Tools package (`func` binary)
```
sudo apt-get update
sudo apt-get install azure-functions-core-tools-3
```

---

# Azure CLI (`az` binary)

Install using a script (maintained by Azure team)

```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

Azure Login 

```bash
az login
```

If you want to list available locations

```bash
az account list-locations
```

---

# Alternative installs

* Azure Functions Core tools: https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local 
* Azure CLI: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-linux

---

# Creating Project and Apps

Create Project
```bash
func init $PROJECT_NAME --python
```

Create Function

```bash
func new \
    --name $FUNCTION_NAME \
    --template "HTTP trigger" \
    --authlevel "anonymous"
```

Run locally

```bash
func start
```

---

# Creating Azure Resources

Create Resource Group

```bash
az group create \
    --name $GROUP_NAME \
    --location $LOCATION_NAME
```
General-purpose storage account

```bash
az storage account create \
    --name $STORAGE_NAME \
    --location $LOCATION_NAME \
    --resource-group $GROUP_NAME \
    --sku Standard_LRS
```

---

# Creating Resources (contd.)

Create the function app in Azure

```bash
az functionapp create \
    --resource-group $GROUP_NAME \
    --consumption-plan-location $LOCATION_NAME \
    --runtime python \
    --runtime-version 3.8 \
    --functions-version 3 \
    --name $APP_NAME \
    --storage-account $STORAGE_NAME \
    --os-type linux
```

---

# Deploy

```bash
func azure functionapp publish $APP_NAME
```

## Logs

```bash
func azure functionapp logstream $APP_NAME --browser
```

---

# Delete Azure Resources

```bash
az group delete --name $GROUP_NAME
```

---

# Thanks! :pray:

dhilipsiva@pm.me

[http://dhilipsiva.com](http://dhilipsiva.com)

https://github.com/dhilipsiva/talks

[http://www.slideshare.net/dhilipsiva](http://www.slideshare.net/dhilipsiva)

Source Code: https://github.com/reckonsys/python-azure-functions-demo

## Questions:question:
