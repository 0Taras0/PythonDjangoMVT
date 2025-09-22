# Simple MVT

```
py --version
py -m venv .venv
```

# Activate venv
```
.venv\Scripts\activate.bat
python.exe -m pip install --upgrade pip
py -m pip install Django
py

>>>import django
>>>print(django.get_version())
>>>quit()

python -m django --version
mkdir djangomvt
django-admin startproject mysite djangomvt
cd djangomvt
py manage.py runserver 9581

py manage.py startapp categories
py manage.py migrate

py manage.py startapp users

deactivate
```

# Migrations
```
cd djangomvt

python manage.py makemigrations

python manage.py migrate
```

# Shell
```
python manage.py shell
```
## In Shell
```
from categories.models import Category
```
### **Create**
```
Category.objects.create(name="Супи", slug="soups", image="soups.jpg")

Category.objects.create(name="Салати", slug="salads", image="salads.jpg")

Category.objects.create(name="Десерти", slug="desserts", image="desserts.jpg")

Category.objects.all()
```

### **Update**
```
c = Category.objects.get(slug="salads")

c.name = "Овочеві салати"

c.image = "fresh_salads.jpg"

c.save()

Category.objects.get(slug="salads")
```

### **Remove**
```
c = Category.objects.get(slug="soups")

c.delete()

Category.objects.all()
```

## Close Shell
```
exit()
```