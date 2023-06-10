# simple-todo

A project that runs a Flask API server and an app via vite, four separate containers, using Docker Compose. Here are four components: 

1. Frontend [React, Tailwind, Vite]
2. API [Python Flask]
3. Database [MySql]
4. Redis as API Caching Layer


## Installation

Clone this repository first-
```sh
$ git clone git@github.com:SadikurSadik/simple-todo.git
```

Now cd into Project Directory
```sh
$ cd simple-todo
```

For development, the `flask-api/`, `react-app/` and `db` directories have their own docker containers, which are configured via the docker-compose.yml file.

```sh
$ docker-compose up
```

The client server is spun up at `localhost:5173` and flask api server running on `localhost:5000` 

The local directories are mounted into the containers, so changes will reflect immediately. However, changes to package.json or requirements.txt will likely need to a rebuild:
```sh
$ docker-compose down && docker-compose build && docker-compose up
```

I have a blog post on  how this project work, you can check it out.

- https://medium.com/@sadik7070/simple-todo-65134caac44b


Have a good day. Thank you.



