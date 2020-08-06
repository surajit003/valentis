import os, csv

path = "/opt/valentisHealth/medication/"
os.chdir(path)
from medication.models import MyDawa

with open('mydawa.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        p = MyDawa.objects.create(brand=row['brand'], size=row['size'], price=row['price'])
        p.save()
