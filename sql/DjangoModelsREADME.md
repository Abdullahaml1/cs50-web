# Django Models [docs](https://docs.djangoproject.com/en/3.2/ref/models/)
is and abstraction layer over the database to make it easier to use.

## How to use it
you have to define your models using `django.models.Model` class prefarable to use it in `"app_name"/models` for example: 
```python
from django.db import models

class Flight (models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duratiion = models.IntegerField()

```
* The types of Fields is [here](https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types)
* valid attributes for fields are [here](https://docs.djangoproject.com/en/3.2/topics/db/models/#field-options) basics ones:

| Attribute Name                | Description                                                      |
|-------------------------------+------------------------------------------------------------------|
| `null=True/False`             | corresponds to (NULL, NOT NULL) of sql                           |
| `blank=True/False`            | like `null`but it is a validation before inserting into database |
| `default=<the defualt value>` | like sql DEFAULT                                                 |
| `unique=True/False`           | like sql UNIQUE                                                  |
| `primary_key=True`            | setting primary key like sql PRIMARY KEY                            |

By default, Django gives each model an auto-incrementing primary key with the type specified per app in AppConfig.default_auto_field or globally in the DEFAULT_AUTO_FIELD setting. For example:
```pyton
id = models.BigAutoField(primary_key=True)
```
If you’d like to specify a custom primary key, specify primary_key=True on one of your fields. If Django sees you’ve explicitly set Field.primary_key, it won’t add the automatic id column.

Each model requires exactly one field to have primary_key=True (either explicitly declared or automatically added).

* The valid relationships are [here ](https://docs.djangoproject.com/en/3.2/topics/db/models/#relationships)

TODO ManyToManyField, ForeignKeyField
