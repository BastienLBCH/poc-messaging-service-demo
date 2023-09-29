# Poc Messaging Service CQRS commands part
This code is a proof of concept. 
Meaning it's not made to run on a production environment (e.g. it uses a sqlite database) 
and it is also the first time I use these design patterns.

It's part of an instant messaging service designed with the CQRS designed pattern combined with event sourcing.

This repo contains the command part, meaning that it takes commands and transforms it in events before sending it through Kafka.


## Installation
### Preparing
**Prerequisite :** Having docker installed

You need to create a .env file in the folder pocMessagingServiceCommands/pocMessagingServiceCommands at the same level than the settings.py file

Options are :
```
KEYCLOAK_PUBLIC_KEY
KEYCLOAK_ALG

BOOTSTRAP_SERVERS
TOPIC

ENV
```
Explaining one by one :
- **KEYCLOAK_PUBLIC_KEY**: Public key used by Keycloak to sign the JWT delivered
- **KEYCLOAK_ALG**: Algorithm used by Keycloak to sign the JWT
- **BOOTSTRAP_SERVERS**: Address of the Kafka server used to 
- **TOPIC**: Topic to send the messages on
- **ENV**: Define this variable to ENV=test for unit test purpose.

For unit test, you have to add extra variables :
```
CLIENT_ID
USERNAME_TEST
PASSWORD_TEST
```
- **CLIENT_ID**: ID of the keycloak's client used for testing purpose
- **USERNAME_TEST**: Username of a user existing for testing purpose
- **PASSWORD_TEST**: Password of a user existing for testing purpose

**Example of a complete .env file :**
```
KEYCLOAK_PUBLIC_KEY=MIIBIjANB...AQAB
KEYCLOAK_ALG=RS256

KEYCLOAK_TOKEN_URL=http://localhost:8080/realms/poc/protocol/openid-connect/token
BOOTSTRAP_SERVERS=localhost:9092
TOPIC=messaging-service

ENV=test

CLIENT_ID=test-login-client
USERNAME_TEST=John
PASSWORD_TEST=azerty
```


### Building and deploying

> [!IMPORTANT]
> This repo is only one "service" of the whole project, if you want to really test it you need :
> - [The query part](https://github.com/BastienLBCH/poc-messaging-service-queries) 
> - Kafka
> - Keycloak
> 
> To be configured and runnning

You can easily deploy this service using docker using these commands in the project root directory:
```bash
docker build . -t poc-messaging-service-command
```
then
```bash 
docker run -p 8000:8000 --name poc-messaging-service-command poc-messaging-service-command 
```


## Usage
This API provides endpoints to create conversations, post messages and add a participant to a conversation.


### Create a conversation
- **Endpoint**: /conversations/
- **Method**: POST

Headers :

| Attribute       |                  Value |
|:----------------|-----------------------:|
| Authorization   |  Bearer {access token} |


Body :
(Can either be raw using the JSON syntax or a form)

| Attribute |               Value |
|:----------|--------------------:|
| name      | {conversation name} |


### Delete a conversation
- **Endpoint**: /conversations/{conversation id}/delete
- **Method**: DELETE




### Add user to a conversation
- **Endpoint**: /conversations/{conversation id}/members
- **Method**: POST

Headers :

| Attribute       |                  Value |
|:----------------|-----------------------:|
| Authorization   |  Bearer {access token} |


Body :
(Can either be raw using the JSON syntax or a form)

| Attribute       |                                                 Value |
|:----------------|------------------------------------------------------:|
| participant_id  |           {Id of the user to add to the conversation} |





### Send a message to a conversation
- **Endpoint**: /conversations/{conversation id}
- **Method**: POST

Headers :

| Attribute       |                  Value |
|:----------------|-----------------------:|
| Authorization   |  Bearer {access token} |


Body :
(Can either be raw using the JSON syntax or a form)

| Attribute        |                                                 Value |
|:-----------------|------------------------------------------------------:|
| message_content  |                 {Message to send to the conversation} |







