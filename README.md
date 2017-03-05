# brainprinter: 3D print your brain from the web

----
## What is this project?

This project was begun for the Brainhack Global 2017 event. It is currently incomplete. Eventually this will be a web application that allows users to upload an MRI scan, and then later receive an email with the .stl file and a preview of the model.

In short, it s a web front-end for [this repository](https://github.com/danjonpeterson/brain_printer)

----
## Target use case
Someone with:
 
* No knowlege of neuroimaging or programming 
* Has a DVD of their MRI scans
* Wants a 3D print of their brain

----
## Steps for the user

1) Navigate to the front page

2) Sign in with Google, or another authentication, which would include giving an email address

3) Upload an entire exam in DICOM format, or an mprage in nifti format

4) Wait to recieve an email in ~1-2 days


----
## How it works behind the hood
The web front-end uses [this hackathon template](https://github.com/sahat/hackathon-starter) as a starting point. User information is stored as a mongo database, which includes contact information, and progress status. 

----
## How to set it up on on your local machine

DEPENDENCIES:
If you don't already have them, install [**node**](nodejs.org), [**npm**](www.npmjs.com), [**mongoDB**](www.mongodb.com/Download‎) and [**Docker**](www.docker.com)

Then, open a terminal and clone this repository

    git clone https://github.com/ajijohn/brainprinter

Change your working directory

    cd brainprinter

    brew services start mongodb

Start the Database (below command is for if you are using *homebrew*, for example)

    brew services start mongodb

Open a browser, connect to [localhost:3000](localhost:3000)

And there you go! If you want to inspect what the backend database is doing, open mongo

    mongo

"test" is the current name of the database

    use test

Take a look at the current status

    db.requests.find()


----
## How to set it up as a public webservice on AWS

TODO


----
## The team
This project was created by the Brain Printer Collective, which includes Aji John, Daniel Peterson and Valentina Staneva