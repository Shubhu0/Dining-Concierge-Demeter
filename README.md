# Dining-Concierge-Demeter

This is a serverless, micro service-driven web application created completely using AWS cloud services. The main application of this chatbot is to provide restaurant suggestions to its users based on the preferences provided to it through conversations.

We have support for Yelp-API with suggestions and real time chat. 

## Services Used
1. Amazon S3 - To host the frontend
2. Amazon Lex - To create the bot
3. API Gateway - To set up the API
4. Amazon SQS - to store user requests on a first-come bases
5. ElasticSearch Service - To quickly get restaurant ids based on the user preferences of cuisine collected from SQS
6. DynamoDB - To store the restaurant data collected using Yelp API
7. Amazon SNS - to send restaurant suggestions to users through SMS
8. Lambda - To send data from the frontend to API and API to Lex, validation, collecting restaurant data, sending suggestions using SNS.
9. Yelp API - To get suggestions for food
10. AWS Congito - For authentication

## Architecture:

<img width="929" alt="Assignment 1 architecture diagram (2)" src="https://user-images.githubusercontent.com/85689959/136675790-24f28e24-45d6-4df2-85e0-4956405b6f88.png">

## Chat Example:
![example](chat_example.png)
