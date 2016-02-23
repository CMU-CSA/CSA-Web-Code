# setting up image uploader, this might be moved to another file in future 
# for future reference 
# http://cloudinary.com/documentation/django_integration
import cloudinary
import cloudinary.uploader
import cloudinary.api
cloudinary.config( 
  cloud_name = "dflmreqmi", 
  api_key = "371879211988682", 
  api_secret = "0alLHYEY2fMf1kOJlSgELL6jx7E" 
)




from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length = 30)
    timeStr = models.CharField(max_length = 64)
    location = models.CharField(max_length = 64, default = "")
    ticket = models.CharField(max_length = 64)
    description = models.CharField(max_length = 300)
    time = models.DateField()


class Image(models.Model):
    activity = models.ForeignKey(Activity, related_name='images')
    url = models.URLField(max_length= 200)

   
    def addImage(self, activityName, fileName):
        try:
            curActivity = Activity.objects.get(name = activityName)
            try: 
                result = cloudinary.uploader.upload(fileName)
                url = result['url']
                self.url = url
                self.activity = curActivity
                self.save();
            except:
                print('image file does not exist')
                raise
        except:
            print activityName + 'does not exist, check if you enter wrong name'
            raise
        return    