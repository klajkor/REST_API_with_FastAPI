FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

#It's important to copy the app code after installing the dependencies, that way you can take advantage of Docker's cache. That way it won't have to install everything from scratch every time you update your application files, only when you add new dependencies.
#This also applies for any other way you use to install your dependencies. If you use a requirements.txt, copy it alone and install all the dependencies on the top of the Dockerfile, and add your app code after it.

#RUN apt update
#RUN apt install net-tools
COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock
RUN pip install pipenv
RUN pipenv install

COPY ./app /app
