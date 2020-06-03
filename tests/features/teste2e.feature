# Created by tausif at 03/06/20
Feature: Test End to End Rest Api Functionality
   Testing an End to End
   With Post and Get
   Validating the response with JSONPATH
   Background: Given i enter the url as https://reqres.in/

  Scenario: Sample Post Request
           Given set the resource as POST with request body and parameters api/users
           When request is POST
           Then i validate the response and check status code as 201

  Scenario: Get the Previously Posted Request
            Given there was a successful POST
            Then i assert the get response