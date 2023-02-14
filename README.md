# League of Legends Skins Prices
<p align="center">
    <img src="https://raw.githubusercontent.com/AlexandreBidon/LoL-Skins-Prices/master/docs/assets/main_title.jpg" width="100%">
</p>

<p align="center">
  <a href="#presentation">Presentation</a> •
  <a href="#how-to-run">How To Run</a> •
  <a href="#how-it-works">How It Works</a> •
  <a href="#credits">Credits</a> •
  <a href="#todo">TODO</a> 
</p>

## Presentation
**Note : This repo is part of a last year project at ENSAI school. The subject can be [found here](docs/Sujet%20projet%20g%C3%A9nie%20logiciel.pdf). As a result, this project is not intended for production use. Several issues are present in the code, such as potential SQL Injection.**

### Features
- See all the skins and their current prices on the website
- Create an account and add your favorite skins to your list
- Receive an email when a skin you like is in sale

### Tech stack
- Logging system
- React frontend
- PostgreSQL database
- Backend API using FastAPI

## How to run
### Demonstration


### Launch the tests

## How it works
### API
**[The list of all the endpoints can be found here](docs/ENDPOINTS.md)**.
You can also see

### Database

### Frontend
<p align="center">
    <img src="https://raw.githubusercontent.com/AlexandreBidon/LoL-Skins-Prices/master/docs/assets/demo_web.png" width="100%">
</p>

### Mailing system
<p align="center">
    <img src="https://raw.githubusercontent.com/AlexandreBidon/LoL-Skins-Prices/master/docs/assets/demo_mail.png" width="100%">
</p>

## Credits
### Authors
- Tiroumalai Freddy ([tiroumalaifreddy](https://github.com/tiroumalaifreddy))
- Bidon Alexandre ([AlexandreBidon](https://github.com/AlexandreBidon))

## TODO
- Revamp database object to prevent SQL Injection (remove `"".format()`)
- Improve the handling of Exceptions in the API : returns the good error code
- Add authentification for users in the API
- Add more tests (mock DB and mail object)
- Improve the frontend : add a user page to control the account from here