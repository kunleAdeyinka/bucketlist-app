# BucketList Application

**https://mustdolistapp.herokuapp.com**


[![Build Status](https://travis-ci.org/kunleAdeyinka/bucketlist-app.svg?branch=master)](https://travis-ci.org/kunleAdeyinka/bucketlist-app)

This is a simple bucket list application where users can register, sign in and create their bucket list. 
We'll be using Flask, a Python web application framework, to create the application, with PostgresSQL as the back end.
This is hosted on Heroku with Travis CI used for continous integration.

# Tasks
1. When the application loads up, first page should be a the welcome page asking users to sign up.
2. The user can follow links to sign up and log into the application.
3. A user should be able to sign in and logout of the application.
4. A user signed in can click a link to add a bucket list item.
5. A form is presented to enter a bucket list item.
6. Once filled and submitted the user is returned to the welcome page showing the latest bucket list in the system.
7. Each bucket list displayed has the title, description and the author of the item.
8. Users will be able to edit and delete their bucketlist item.
9. Added pagination to the welcome page since we are displaying all the bucket list items in the database
