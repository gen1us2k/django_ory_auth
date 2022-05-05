# Ory Django

This package provides integration with Ory Cloud or Ory Kratos for your django application

## Installing

You can simply run

```
   pip install django_ory_auth
```

or

```
   poetry add django_ory_auth
```

or

```
   pipenv install django_ory_auth
```

## Configuration

You need to add these variables to your settings

```
ORY_SDK_URL=https://projectId.projects.oryapis.com
LOGIN_URL=https://projectId.projects.oryapis.com/ui/login
LOGOUT_URL=https://projectId.projects.oryapis.com/logout
```
