#############################################################################
#Perform on an Amazon Linux 2 operating system (variant of Redhat)
#future nice to have: build lambda layer using lambda runtime docker image
#https://github.com/lambci/docker-lambda
#############################################################################

#prerequisites for python
sudo yum install -y gcc openssl-devel bzip2-devel libffi-devel 

#download and untar source code
wget https://www.python.org/ftp/python/3.9.9/Python-3.9.9.tgz

tar xzf Python-3.9.9.tgz 

cd Python-3.9.9

#builds source code
sudo ./configure
#makes sure not to overwrite existing python3
sudo make altinstall

##############################################
#Create lambda layer for alexa skills kit sdk
##############################################
mkdir ask_layer
cd ask_layer
mkdir python
cd python 
pip3.9 install ask-sdk-core==1.16.1 -t .

zip -r ask_layer.zip .

aws s3 cp ask_layer.zip s3://burnday-app-artifacts