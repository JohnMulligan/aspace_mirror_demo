from django.db import models

class LevelOfDescription(models.Model):
    name = models.CharField(max_length=50,unique=True)

class Record(models.Model):
    title = models.CharField(max_length=500)
    ref_id = models.CharField(max_length=32)
    level_of_description = models.ForeignKey(
        "LevelOfDescription",
        on_delete=models.CASCADE,
    )

#PHYSICAL DESCRIPTION
#CONDITION

'''

Title
Barbados Advocate
Ref ID
3abb6adb6426bb1ad845e34a57e79842
Level of Description
File
Publish?
True
Has Unpublished Ancestor?
True
Restrictions Apply?
False
Repository Processing Note
Unique ID TBA

'''
