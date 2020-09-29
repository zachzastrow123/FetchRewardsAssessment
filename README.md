# FetchRewardsAssessment

## Project Assumptions
1. The characters are case sensitive. For example, "banana" would be a pyramid word, but "bAnana" would not.
2. The API accepts all characters. For example, a string that reads "{{}" would be considered a pyramid word.
3. The application assumes minimal users and traffic. Concurrency is not utilized.

## Requirements
The following packages must be installed to run the Fetch Rewards Assessment:

-Python 3

-[Flask](https://pypi.org/project/Flask/)

-[Flask-API](https://pypi.org/project/Flask-API/)

-[flask-swagger-ui](https://pypi.org/project/flask-swagger-ui/)


## Run Instructions
To run the application, navigate to the folder where the application is saved, and from the command line, run 'python Assessment.py'

The API accepts a string request body and returns 'True' if the string is a pyramid word, and it returns 'False' if the string is not a pyramid word.

The API uses port 8888.

Sample curl command: curl -X POST "http://127.0.0.1:8888/pyramid" -H "accept: text/plain" -H "Content-Type: text/plain" -d "banana"

Sample response: True

## Unit Testing
To run unit tests for the application, navigate to the folder where the application is saved, and from the command line, run 'python UnitTests.py'

## Swagger
To view Swagger documentation, and to test the API within the browser, navigate to http://localhost:8888/swagger.
