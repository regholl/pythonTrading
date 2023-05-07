# pythonTrading
a way to trade and view stocks in the CLI

###########################################################################################################################################################################

UPDATE 5/7: After talking with some more experienced friends, I am going to hold off on Docker until I am ready to deploy
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
  
  ###########################################################################################################################################################################
  

UPDATE 4/30: Gonna start adding updates as a changelog here as well, full blog posts on my website
  + added class files for all DB info
  + made Docker container
  + added basic frontend functionality
  + recovered old API connection
