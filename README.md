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

pip install Pillow

py manage.py makemigrations categories

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

# Clone project
```
.venv\Scripts\activate.bat

pip freeze

pip freeze > requirements.txt

git clone https://github.com/0Taras0/PythonDjangoMVT
cd djangomvt
py -m venv .venv
.venv\Scripts\activate.bat

python.exe -m pip install --upgrade pip
py -m pip install Django
cd djangomvt
py manage.py runserver 4892
```

## Add super user
```
py manage.py createsuperuser
admin
admin@gmail.com
123456
py manage.py runserver 4892
```

## Add products and images
```
py manage.py startapp products

py manage.py makemigrations products

py manage.py migrate
```