# How to run the database

> docker build -t lol_db_image ./

> docker run -d --name lol_db -p 5432:5432 lol_db_image


## Commandes utiles

> docker system prune -a

> lsof -i :5432

> sudo kill pid