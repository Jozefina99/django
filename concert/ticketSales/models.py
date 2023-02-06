from django.db import models
from jalali_date import date2jalali,datetime2jalali

# Create your models here.

class  concertModel(models.Model):
	class Meta:
		verbose_name="کنسرت"
		verbose_name_plural="کنسرتها"

	Name=models.CharField(max_length=100)
	SingerName=models.CharField(max_length=100)
	length=models.IntegerField()
	Poster=models.ImageField(upload_to="ConcertImages/",null=True)

	def  __str__(self):
		return self.SingerName

class  locationModel(models.Model):
	class Meta:
		verbose_name="محل برگزاری"
		verbose_name_plural="محل برگزاری"

	IdNumber=models.IntegerField(primary_key=True)
	Name=models.CharField(max_length=100)
	Adress=models.CharField(max_length=500,default="تهران - برج میلاد")
	Phone=models.CharField(max_length=11,null=True)
	capacity=models.IntegerField()
	test=models.CharField(max_length=10,null=True)

	def __str__(self):
		return self.Name

class timeModel(models.Model):

	class Meta:
		verbose_name="سانس"
		verbose_name_plural="سانس"

	concertModel= models.ForeignKey("concertModel",on_delete=models.PROTECT)
	locationModel= models.ForeignKey(to=locationModel,on_delete=models.PROTECT)
	StartDateTime= models.DateTimeField()
	Seats=models.IntegerField()
	Start=1
	End=2
	Cancel=3
	Sales=4
	status_choices=((Start,"فروش بلیط شروع شده "),
					(End,"فروش بلیط تمام شده"),
					(Cancel,"این سانس کنسل شده"),
					(Sales,"درحال فروش بلیط"))
	Status=models.IntegerField(choices=status_choices,verbose_name=",عیت")

	def __str__(self):
		return "Time: {} ConcertName: {} Location: {}".format(self.StartDateTime,self.concertModel.Name,self.locationModel.Name)
	def get_jalali_date(self):
		return datetime2jalali(self.StartDateTime)	
class ProfileModel(models.Model):
	class Meta:
		verbose_name="کاربر"
		verbose_name_plural="کاربر"

	Name=models.CharField(max_length=100)
	Family=models.CharField(max_length=100)
	ProfileImage=models.ImageField(upload_to="ProfileImage/")
	Man=1
	Women=2
	status_choices=(("Man","مرد"),("Women","زن"))
	Gender=models.IntegerField(choices=status_choices)


	def __str__(self):
		return "FullName:{} {}".format(Name,Family)

class ticketModel(models.Model):
	class Meta:
		verbose_name="بلیط"
		verbose_name_plural="بلیط"
	ProfileModel= models.ForeignKey("ProfileModel",on_delete=models.PROTECT,verbose_name="کاربر")
	timeModel= models.ForeignKey("timeModel",on_delete=models.PROTECT,verbose_name="سانس")
	ticketImage=models.ImageField(upload_to="TicketImage/",verbose_name="عکس")

	Name=models.CharField(max_length=100,verbose_name="عنوان")
	Price=models.IntegerField(verbose_name="مبلغ")

	def __str__(self):
		return "TicketInfo: Profile: {} ConcertInfo: {}".format(timeModel.__str__())
