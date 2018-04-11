from django.db import models
from django.utils import timezone

# Create your models(Relationship) here.


class RelHouseHolder(models.Model):

    class Meta:
        db_table = "rel_house_holder"
        ordering = ['-checkin_time']

    rel_id = models.AutoField(primary_key=True)
    house_id = models.IntegerField(unique=True)
    householder_id = models.IntegerField()
    checkin_time = models.DateTimeField(default=timezone.now)
    moveout_time = models.DateTimeField(default=timezone.datetime.max)

    def __str__(self):
        return "%s - %s - %s - %s" % (self.rel_id,
                                      self.house_id,
                                      self.householder_id,
                                      self.checkin_time)


class RelCarHolder(models.Model):

    class Meta:
        db_table = "rel_car_holder"
        ordering = ['checkin_time']

    rel_id = models.AutoField(primary_key=True)
    car_id = models.IntegerField(unique=True)
    householder_id = models.IntegerField()
    checkin_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s - %s - %s" % (self.rel_id,
                                 self.car_id,
                                 self.householder_id)


class RelHouseholderRepair(models.Model):

    class Meta:
        db_table = "rel_householder_repair"
        ordering = ['repair_id']

    rel_id = models.AutoField(primary_key=True)
    householder_id = models.IntegerField()
    repair_id = models.IntegerField()

    def __str__(self):
        return "%s - %s - %s" % (self.rel_id,
                                 self.householder_id,
                                 self.repair_id)


class RelStaffProfile(models.Model):

    class Meta:
        db_table = "rel_staff_profile"

    rel_id = models.AutoField(primary_key=True)
    staff_id = models.IntegerField()
    profile_id = models.IntegerField()

    def __str__(self):
        return "%s - %s - %s" % (self.rel_id,
                                 self.staff_id,
                                 self.profile_id)
