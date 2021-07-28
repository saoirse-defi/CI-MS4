![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Code Institute, Milestone 4: Farm2Table

## Introduction

Over the past decade, the world has truly become a global economy. Global supply chain expansion has provided unparalleled choice for the consumer. In relation to the food industry, the term 'out of season' has become a thing of the past. No longer do we have to wait until the summer months to enjoy berries or winter for citrus fruits. With the popularity of grocery chains such as Lidl & Aldi, locally sourced fruit & vegetables are being phased out for cheaper produce which is normally shipped halfway across the globe. To endure this expedition, the produce is harvasted well before it has reached maturity and ripened in shipping containers by the use of 'controlled environments'. This produce tends to turn bad very quickly due to this unnatural journey, sometimes within 48 hours of purchase causing massive food wastage. Most of us have lost the connection to the food we eat.

With my final milestone project for Code Institute, I will attempt to tackle this problem within our society. My goals is to get Ireland eating locally & in season again by creating a marketplace to connect local producers with consumers. My project Farm2Table aims to reduce the friction associated with sourcing local produce by having all local producers of fruit & veg in one marketplace. This environment will inspire competition between producers, allowing the consumers to easily find the best price for their local fruit & veg.

### Notes for Assessment Team


### Future Features

This section will outline potential features which I would like to implement in future.


## Considerations

### Use Cases


## UX

### Project Goals

The goal of this project is to get Ireland eating locally again by creating a marketplace where fruit & vegetable producers will compete for orders.

### User Goals

### Developer & Business Goals

This section will outline goals set out by application creator both in relation to how they would like to develop as a software engineer & their financial goals as regards to the website.

#### Developer Goals


#### Business Goals

Currently I have identified 3 possible streams of income this project would be able to generate. 

* A small fee will be applied to each purchase made within the application for connecting the producer with the consumer & processing payment between the 2 parties.

* Producers will have the ability to purchase premium Farm2Table memberships giving them access to additional features, such as being highlighted on the front page of the website, ad-free storefronts.

* Advertising revenue will be generated from the web traffic on the application.


### User Stories

|User Type |I want to be able to...  | So that I can... |
|:--- | ---: | :---:|
|center text|center text|center text|
|Seller|Add my listing to a marketplace|I can attract orders from a larger number of customers|
|Seller|cell data2|cell data3|
|Seller|cell data2|cell data3|
|Seller|cell data2|cell data3|
|Seller|cell data2|cell data3|
|Seller|cell data2|cell data3|


1. As a user of this web application I want:
    * A clean and enjoyable UX, everything should be where I want it.
    * Fonts that are legible but something a bit different to the norm.
    * Little to no load times when the website first starts or has to complete a process.

2. As somebody looking to advertise on this website I would like:
    * Content that is family friendly and not provocative, so our brand doesn't become tarnished.
    * Heavy user traffic in order to get our brand in front of as many eyeballs as possible.
    * Fast load times to ensure impatient users don't leave the site.


### Design Choices

#### Favicon

I really enjoy this favicon which was sourced from [Favicon.cc](https://www.favicon.cc/?action=icon&file_id=636006)

![Favicon](static/favicon.ico)

#### Responsive Front-End Framework

For this project, I decided to use the Materialize framework which is build on the principles of material design.
After completing the project using this new framework, I can safely say that I prefer it more than Bootstrap which I have used on my previous 2 milestone projects.
It appears to provide more feedback to the user when they are navigating throughout the web application while remaining responsive on most devices.

#### Icons

All icons for this application have been sourced from [Google Fonts](https://fonts.google.com/icons) collected from the Material Icons library. As the designer of the web application, the selection of the icons must be done in line with other successful applications. 

##### Favourite Icon

##### Edit Icon

##### Delete Icon


#### Fonts


##### Varela Round


#### Colours


##### Materialize Button

The colour of the buttons throughout the site is unchanged as it is the primary button colour for the Materialize framework. During the design process, I noticed that this shade of blue complemented the teal hue of the navbar.


## Key Frontend Design Elements

This section will outline the key elements within this application giving descriptions on the purpose of each element.


### Error Handling

#### Flash Messages


#### API Exceptions


#### Other Low Level Exceptions

Other low level exceptions such as client-side errors (4xx) or server-side errors (5xx) will also be handled, describing to the user which error occurred. The user will also have an option to either return to their homepage or the login page depending on their credentials. 


#### Lottie Player Animations

Lottie provides lightweight animation hosting which provides significantly smaller footprint than conventional animations.


## Wireframes


### User Interaction


## Implementation

This section will outline the technologies & processes used in the design & implementation of this application.

### Materialize Framework

For this project, the frontend framework I decided to use was Materialize. In my previous 2 milestone projects, I chose Bootstrap for the frontend, but I can now safely say that I much prefer the look of Materialize.
As it is based on the principles of material design, all elements just seem that little bit sharper and current.


#### CRUD Operations

One of the main goals of this milestone project was to integrate a database within our application and use it to it's full potential. CRUD in computer programming is an acronym which stands for create, read, update & delete. This covers the 4 main operations of a database. Within this section I will go over how I implemented each of these operations.

##### Create Operation


##### Read Operation


##### Update Operation


##### Delete Operation



#### Flask

Flask is a web application framework written in Python based on the Werkzeug toolkit & the Jinja2 templating language. During my development of this application is when I noticed the usefulness of flask, getting to experiment with the different flask libraries. Jinja templating also opened a lot of doors for me as a web developer when managing repeated pre-defined data.


### Modules


## Performance

#### Image Resizing & Compression

Due to the nature of the application, no image compression was needed as all design elements are from the Materialize framework. No images were used in the making of this application.


#### Lottie Player Animations

By using the Lottie animation player, we can bring beautiful animations into our application without having to worry about file size and hence performance. I have used a single hosted Lottie animation on the error.html page.


###### Autoprefixing

The CSS style rules have been [Autoprefixed](https://autoprefixer.github.io/) to maintain uniformity of style rules across all browsers.


## Testing

### User Testing

As the application began to take shape with all major components in place, the user testing could commence. This was done by reviewing each component line by line to ensure that the code works as intended. If an edit was to be made, the developer made sure to the changes were reflected correctly on the frontend.

### Mobile Testing


### Application Testing


## Bugs Discovered


## Dependencies

This section will cover all software dependencies needed to run this application.


## Deployment

### Github Pages Deployment Procedure

This project was developed using Gitpod, committed to git and pushed to Github using the built-in function with Gitpod.

To deploy this page from Github pages from its Github repository, the following steps were taken.

1. Log into Github.
2. From the list of repositories on the screen, select saoirse-defi/milestone1-bad-arts-1.0.
3. From the menu items near the top of the page, select Settings.
4. Scroll down to the Github Pages section.
5. Under source click the drop-down menu labelled None and select Master Branch.
6. On selecting Master Branch, the page is automatically refreshed, the website is now deployed.
   
At the moment of submitting this milestone project, the default branch is version1.2 which is the latest version.


#### How to run this project locally:

To clone this project into Gitpod you will need:
1. A Github account
2. Use the Chrome browser

Then follow these steps:
1. Install the Gitpod browser extensions for Chrome
2. After installation, restart the browser
3. Log into Gitpod with your Gitpod account
4. Navigate to the Github project repository
5. Click the green 'Gitpod' button in the top right corner of the repository
6. This will trigger a new Gitpod workspace to be created from the code in Github where you can work locally


To work on the code within a local IDE such as VScode:
1. Follow this link to the Github repository
2. Under the repository name, click 'clone' or 'download'
3. In the clone with the https section, copy the clone URL for the repository
4. In your local IDE, open the terminal
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type 'git clone', and then paste the URL copied in step 3

git clone https://www.Github.com/USERNAME/REPOSITORY

7. Press enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository can be found here [Github](https://docs.Github.com/en/free-pro-team@latest/Github/creating-cloning-and-archiving-repositories/cloning-a-repository).


### Heroku Deployment Procedure

#### How to run your project on Heroku

Follow these steps:
1. Create a virtual environment with pipenv and install Flask and Gunicorn
2. Create a “Procfile” and write the following code "touch Procfile" in the command line
3. Create “runtime.txt” and write the following code "touch runtime.txt" in the command line
4. Create a folder named “app” and enter the folder
5. Create a python file, “main.py” and enter the sample code below

from flask import Flask
app = Flask(__name__)
@app.route("/")
def home_view():
        return "<h1>Welcome to Geeks for Geeks</h1>

6. Get back to the previous directory “eflask”.Create a file“wsgi.py” and insert the following code

from app.main import app
if __name__ == "__main__":
        app.run()

7. Run the vitual environment write "pipenv shell" in the command line.
8. Initialize an empty repo, add the files in the repo and commit all the changes
9. Login to heroku CLI using "heroku login"
10.  Create a unique name for your Web app, write "heroku create hashboard"
11. Push your code from local to the heroku remote using "git push heroku master"


#### How to create a MongoDB database

1. Create a MongoDB Atlas account [here](https://www.mongodb.com/cloud)
2. Log into your MongoDB Atlas account 
3. Create a free, shared cluster by selecting your preferred provider, stick to the free tier
4. Name your cluster and click create to deploy your cluster
5. Add your connection IP address to the IP access list
6. Create a new database user for your cluster
7. Install PyMongo within your flask application, check version to see if installed correctly
8. Provide a connection method & a configured connection string to MongoDB Atlas
9. Import MongoClient from PyMongo within flask
10. Insert a command within flask that specifies a client is for connecting to your cluster
11. Create a new database within your cluster
12. Create a new collection for your database
13. Create a new document to add to your collection


## Credit

[Materialize Framework Documentation](https://materializecss.com/)

[HTML Element fade-out](https://stackoverflow.com/questions/1911290/make-div-text-disappear-after-5-seconds-using-jquery#1911308)

[Etherscan API Documentation](https://etherscan.io/apis)

[Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/)

[Jinja Documentation](https://jinja.palletsprojects.com/en/3.0.x/)

[Werkzeug Documentation](https://werkzeug.palletsprojects.com/en/2.0.x/)

[Ethereum Documentation](https://ethereum.org/en/)

[Mongo DB Documentation](https://docs.mongodb.com/)

[Python Docstrings](https://www.geeksforgeeks.org/python-docstrings/)

[Pylint Error Help](https://learn.adafruit.com/improve-your-code-with-pylint/pylint-errors)

[Heroku Documentation](https://devcenter.heroku.com/categories/python-support)

[Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet)

[Displaying Information to the user efficiently](https://www.youtube.com/watch?v=Ox9MW9Z8srE&list=PLOPo1bGrV4htxbQCS3CPZ59O1kpPdE7PK)




