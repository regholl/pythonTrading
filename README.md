# pythonTrading
a way to trade and view stocks in the CLI

# UPDATE 5/10: 

Going to focus on Frontend Development for now and go back to SQL when the rest is finished.

  + cleaned up unnecessary files from the repo using gitignore
  + initializing GET request was broken, site works again

  I took a look at the SQLAlchemy tutorial again and ran it in the Python interpreter, I think I have a better idea of where I messed up and can fix it. Going to take another stab at it.
  
  - Deleted as many non-source files as possible, removing txts is next

# UPDATE 5/7: 

After talking with some more experienced friends, I am going to hold off on Docker until I am ready to deploy

  - deleted Portfolio class and related files, unnecessary since its just a list object of Stock objects
  + added SQLite functionality, working on SQLAlchemy now
  + wrote HTML files using chatGPT as a partner when I needed to add html features I was new to
  + added Jinja Template code into Positions.html to display Stocks from the app
  + developed SQL Schema for the relational database
  
  I am going to be rewriting the app in /ver2/ to have
    - API Connection to tda-api/TDA
    - sqlite to handle the database
    - flask + jinja to display info
    
  I will run tests on these to clean up the code and then after that, I will start tackling the functionality to connect the base python app to other programs.


# UPDATE 4/30: 

Gonna start adding updates as a changelog here as well, full blog posts on my website

+ added class files for all DB info
  + made Docker container
  + added basic frontend functionality
  + recovered old API connection
