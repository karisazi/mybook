from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    name = models.CharField(max_length=300)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    username = models.CharField(blank=True)
    
    def __str__(self):
        return self.user.username

class Book(models.Model):
	cover = models.ImageField(upload_to='book_cover')
	title = models.CharField(max_length=300)
	description = models.TextField()
	writer = models.CharField(max_length=300)

	GENRE_CHOICES = (
		('AE', 'Academic & Education'),
		('AR', 'Art'),
		('BI', 'Biography'),
		('BC', 'Business & Career'),
		('CY', 'Children & Youth'),
		('EN', 'Environment'),
		('FL', 'Fiction & Literature'),
		('HF', 'Health & Fitness'),
		('LI', 'Lifestyle'),
		('PG', 'Personal Growth'),
		('PL', 'Politics & Laws'),
		('RE', 'Religion'),
		('SR', 'Science & Research'),
		('TE', 'Technology')
	)

	genre = models.CharField(choices=GENRE_CHOICES, default='AE', max_length=2)
	favorite = models.BooleanField()
	publish_year = models.IntegerField()
	pages = models.IntegerField()
	keywords = models.TextField(blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	id_user = models.IntegerField()
	is_global = models.BooleanField(default=False)  # Indicates if the book is available to all users
	file = models.FileField(upload_to='book_file')

	def __str__(self):
		return self.title