from django.db import models
from django.utils import timezone

# Create your models(Entity) here.


# User
class HouseHolder(models.Model):

    class Meta:
        db_table = 'householder'
        ordering = ['householder_id', 'username']

    householder_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=10, unique=True,)
    password = models.CharField(max_length=32)
    realname = models.CharField(max_length=10)
    tel = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=30, unique=True)
    register_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s - %s - %s" % (self.householder_id,
                                 self.username,
                                 self.realname)


class House(models.Model):

    class Meta:
        db_table = 'house'
        ordering = ['house_id', 'location']

    house_id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=100, unique=True)
    size = models.SmallIntegerField(default=0)
    text_description = models.CharField(max_length=100)
    image_description = models.ImageField()

    def __str__(self):
        return "%s - %s - %s" % (self.house_id,
                                 self.location,
                                 self.text_description)


class Car(models.Model):

    class Meta:
        db_table = 'car'
        ordering = ['car_id', 'car_number']

    car_id = models.IntegerField(primary_key=True)
    car_model = models.CharField(max_length=10)
    car_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return "%s - %s - %s" % (self.car_id,
                                 self.car_model,
                                 self.car_number)


class Repair(models.Model):

    class Meta:
        db_table = 'repair'
        ordering = ['-publish_time']    # 排序首先显示最早发布保修内容

    repair_id = models.IntegerField(primary_key=True)
    house_id = models.IntegerField()
    repair_description = models.CharField(max_length=100)
    publish_time = models.DateTimeField(default=timezone.now)
    staff_id = models.IntegerField()
    repair_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "%s - %s - %s" % (self.repair_id,
                                 self.house_id,
                                 self.repair_description)


class Staff(models.Model):

    class Meta:
        db_table = "staff"

    staff_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=32)
    tel = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=30, unique=True)
    level = models.BooleanField(default=False)

    def __str__(self):
        return "%s - %s - %s" % (self.staff_id,
                                 self.username,
                                 self.level)


class Profile(models.Model):

    class Meta:
        db_table = "staff_profile"

    profile_id = models.IntegerField(primary_key=True)
    realname = models.CharField(max_length=10)
    id_number = models.CharField(max_length=18, unique=True)
    age = models.SmallIntegerField()
    job = models.CharField(max_length=10)
    checkin_time = models.DateTimeField(default=timezone.now)
    salary = models.FloatField()

    def __str__(self):
        return "%s - %s - %s" % (self.profile_id,
                                 self.realname,
                                 self.job)


class Billboard(models.Model):

    class Meta:
        db_table = "billboard"
        ordering = ["-publish_time"]

    billboard_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=10, unique=True)
    content = models.TextField(max_length=255)
    staff_id = models.IntegerField()
    publish_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s - %s - %s" % (self.billboard_id,
                                 self.title,
                                 self.publish_time)

