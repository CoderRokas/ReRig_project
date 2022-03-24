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
		{'username' : 'Bob', 'title' : 'post1', 'description' : 'A very interesting description', 'averageRating' : 4, 'category' : 'desktop', 'date':datetime.datetime(2020,10,10)},
		{'username' : 'Alex', 'title' : 'post2', 'description' : 'A very interesting description', 'averageRating' : 2, 'category' : 'desktop', 'date':datetime.datetime(2019,11,21)},
		{'username' : 'Alex', 'title' : 'post3', 'description' : 'A very interesting description', 'averageRating' : 2, 'category' : 'laptop', 'date':datetime.datetime(2020,9,10)}
	]

	posts_objects = {}

	reviews = [
		{'username' : 'Bob', 'post_title' : 'post1', 'score' : 4, 'comment' : 'This is good', 'date':datetime.datetime(2020,10,10)},
		{'username' : 'Bob', 'post_title' : 'post2', 'score' : 2, 'comment' : 'This is average', 'date':datetime.datetime(2020,3,10)},
		{'username' : 'Tom', 'post_title' : 'post2', 'score' : 2, 'comment' : 'This is average', 'date':datetime.datetime(2020,5,10)}
	]

	for new_user in new_users:
		u = add_user(new_user['username'], new_user['password'])
		users_objects[new_user['username']] = u
	
	for post in posts:
		p = add_post(users_objects[post['username']], post['title'], post['description'], post['averageRating'], post['category'], post['date'])
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

def add_post(author, title, description, averageRating, category, date):
	p = Post.objects.get_or_create(author=author, title=title, description=description, averageRating=averageRating, category=category)[0]
	p.author = author
	p.title = title
	p.description = description
	p.averageRating = averageRating
	p.category = category
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