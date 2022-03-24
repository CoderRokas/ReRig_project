import os
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE','rerig_project.settings')

import django
django.setup()
from rerig.models import Post, Review
from django.contrib.auth.models import User

def populate():
	new_users = [
		{'username' : 'Bob', 'password' : '123'},
		{'username' : 'Alex', 'password' : 'abc'},
		{'username' : 'Tom', 'password' : 'password'},
	]

	users_objects = {}

	posts = [
		{'username' : 'Bob', 'title' : 'New PC', 'description' : 'Rate my Rig', 'averageRating' : 4, 'category' : 'PC', 'date':datetime.datetime(2020,10,10), 'picture':'post_test_images/test1.jpg'},
		{'username' : 'Alex', 'title' : 'Should I Buy?', 'description' : 'I need a laptop for school, was looking for a good one is this any good?', 'averageRating' : 2, 'category' : 'laptop', 'date':datetime.datetime(2019,11,21), 'picture':'post_test_images/test2.jpg'},
		{'username' : 'Tom', 'title' : 'Old Setup', 'description' : 'What should I upgrade, got a pentium and gtx 480 in there', 'averageRating' : 2, 'category' : 'PC', 'date':datetime.datetime(2020,9,10),'picture':'post_test_images/test3.jpg'}
	]

	posts_objects = {}

	reviews = [
		{'username' : 'Alex', 'post_title' : 'New PC', 'score' : 4, 'comment' : 'Too much RGB lights', 'date':datetime.datetime(2020,10,11)},
		{'username' : 'Tom', 'post_title' : 'Should I Buy?', 'score' : 2, 'comment' : 'Solid laptop would recommend!', 'date':datetime.datetime(2020,3,10)},
		{'username' : 'Tom', 'post_title' : 'Old Setup', 'score' : 2, 'comment' : 'Everything.', 'date':datetime.datetime(2020,9,11)}
	]

	for new_user in new_users:
		u = add_user(new_user['username'], new_user['password'])
		users_objects[new_user['username']] = u
	
	for post in posts:
		p = add_post(users_objects[post['username']], post['title'], post['description'], post['averageRating'], post['category'], post['date'], post['picture'])
		posts_objects[post['title']] = p

	for review in reviews:
		add_review(users_objects[review['username']], posts_objects[review['post_title']], review['score'], review['comment'], review['date'])

	# for c in Category.objects.all():
	# 	for p in Page.objects.filter(category=c):
	# 		print(f'- {c}: {p}')
	for u in User.objects.all():
		print(u, 'posts:')
		for p in Post.objects.filter(author=u):
			print('-',p)
		
		print(u, 'reviews:')
		for r in Review.objects.filter(author=u):
			print('-',r)

def add_user(username, password):
	u = User.objects.create_user(username=username, password=password)
	u.save()
	return u

def add_post(author, title, description, averageRating, category, date, picture):
	p = Post.objects.get_or_create(author=author, title=title, description=description, averageRating=averageRating, category=category,picture=picture)[0]
	p.author = author
	p.title = title
	p.description = description
	p.averageRating = averageRating
	p.category = category
	p.picture = picture
	p.save()
	return p

def add_review(author, post, score, comment, date):
	r = Review.objects.get_or_create(author=author, post=post, score=score, comment=comment)[0]
	r.author = author
	r.post = post
	r.score = score
	r.comment = comment
	r.save()
	return r

# Start execution here!
if __name__ == '__main__':
	print('Starting ReRig population script...')
	populate()