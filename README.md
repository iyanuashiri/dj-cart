# dj-cart

## Introduction

This is not a session based cart system. Session based carts are not suitable for REST endpoints because REST is stateless. This implementation stores the contents of the cart in the database.

## Prerequisites

- Django 1.1+
- django content type framework in your INSTALLED_APPS


## Installation

```bash
pip install dj-cart
```

After installation is complete:

    add 'cart' to your INSTALLED_APPS directive and
    
 Run
 
 ```bash
 python manage.py migrate
 ```

## Usage
