# Kitchen Sink Project Setup Guide

## Inspiration

Took inspiration from testdriven.io. Check out the tutorial [here](https://testdriven.io/dockerizing-django-with-postgres-gunicorn-and-nginx).

## Changes I Made

- Not using postgres as a database (You can add it back in if you want to, just look at what testdriven.io did)
- Split settings into settings files according to [HackSoftware, Django Styleguide](https://github.com/HackSoftware/Django-Styleguide?tab=readme-ov-file#settings)
- Using development will also added [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/index.html)
- Added [Celery and Celery Beat](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html) in a container
- Added Tailwind via [Django Tailwind CLI](https://django-tailwind-cli.andrich.me)
- Added Scripts to be able to use [Alpine.js](https://alpinejs.dev)
- Added Scripts to be able to use [htmx](https://htmx.org)

If coming from Bootstrap and used to components, check out [Penguin UI](https://www.penguinui.com) to "Get Your Project Off The Ice Fast & Easy."

## Development

Uses the default Django development server.

1. Rename *.env.dev-sample* to *.env.dev*.
1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

    Tailwind is installed by default, if using bootstrap you can change as needed, the runserver command for development just remove the tailwind parameter.


### Production

Uses gunicorn + nginx.

1. Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db*. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.
