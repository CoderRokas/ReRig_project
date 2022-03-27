import os
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE','rerig_project.settings')

import django
django.setup()
from rerig.models import Post, Review
from django.contrib.auth.models import User

def populate():
	new_users = [
		{'username' : 'Bob', 'password' : '123', 'picture':'profile_test_images/test1.jpg'},
		{'username' : 'Alex', 'password' : 'abc', 'picture':'profile_test_images/test2.jpg'},
		{'username' : 'Tom', 'password' : 'password', 'picture':'profile_test_images/test3.jpg'},
		{'username' : 'RobertFC', 'password' : 'f1fa', 'picture':'profile_test_images/test4.jpg'},
		{'username' : 'Raptor', 'password' : 'tarkov', 'picture':'profile_test_images/test5.jpg'},
		{'username' : 'L1sa', 'password' : 'crown', 'picture':'profile_test_images/test6.jpg'},
		{'username' : 'Mary123', 'password' : 'Bandicam', 'picture':'profile_test_images/test7.jpg'},
		{'username' : 'Chloe_', 'password' : 'cArds', 'picture':'profile_test_images/test8.jpg'},
	]

	users_objects = {}

	posts = [
		{'username' : 'Bob', 'title' : 'PC Rate', 'description' : 'Rate my Rig', 'averageRating' : 4, 'category' : 'PC', 'date':datetime.datetime(2020,10,10), 'picture':'post_test_images/test1.jpg'},
		{'username' : 'Alex', 'title' : 'Should I Buy?', 'description' : 'I need a laptop for school, was looking for a good one is this any good?', 'averageRating' : 2, 'category' : 'laptop', 'date':datetime.datetime(2019,11,21), 'picture':'post_test_images/test2.jpg'},
		{'username' : 'Tom', 'title' : 'Old Setup', 'description' : 'What should I upgrade, got a pentium and gtx 480 in there', 'averageRating' : 2, 'category' : 'PC', 'date':datetime.datetime(2020,9,10),'picture':'post_test_images/test3.jpg'},
		{'username' : 'RobertFC', 'title' : 'Office laptop', 'description' : 'My laptop is too hot to touch the keyboard whenever I run fifa. Is there any way for me to fix this problem? Thats my laptop above.', 'averageRating' : 0, 'category' : 'laptop', 'date':datetime.datetime(2021,2,12),'picture':'post_test_images/test4.jpg'},
		{'username' : 'Raptor', 'title' : 'New PC help', 'description' : 'I just built my PC yesterday and every time I try to boot to windows it keeps sending me to the BIOS instead of windows. Any advice?', 'averageRating' : 0, 'category' : 'PC', 'date':datetime.datetime(2021,3,4),'picture':'post_test_images/test5.jpg'},
		{'username' : 'L1sa', 'title' : 'New PC', 'description' : 'Took a while to save up and build this, GPU prices definitely did not help!', 'averageRating' : 5, 'category' : 'PC', 'date':datetime.datetime(2021,4,1), 'picture':'post_test_images/test6.jpg'},
		{'username' : 'Bob', 'title' : 'VR PC', 'description' : 'I want to build another PC for my index, I know I want small case but I do not know what ones are good so if anyone could link me a good case I would appreciate it.', 'averageRating' : 1, 'category' : 'PC', 'date':datetime.datetime(2021,5,21), 'picture':'post_test_images/test7.jpg'},
		{'username' : 'Chloe_', 'title' : 'New laptop', 'description' : 'I need a new laptop for school and came across this one, is it any good?', 'averageRating' : 0, 'category' : 'laptop', 'date':datetime.datetime(2021,10,10), 'picture':'post_test_images/test8.jpg'},
		{'username' : 'Chloe_', 'title' : 'PC upgrade help', 'description' : 'Put in a new graphics card and the card does not want to turn on. Anyone got any idea what happened?', 'averageRating' : 2, 'category' : 'PC', 'date':datetime.datetime(2021,11,21), 'picture':'post_test_images/test9.jpg'},
		{'username' : 'L1sa', 'title' : 'laptop upgrade', 'description' : 'I am interested in getting more memory for my laptop and was wondering if my laptop can fit more or would I have to replace the existing memory? This is what my laptop looks like when I opened it.', 'averageRating' : 3, 'category' : 'laptop', 'date':datetime.datetime(2022,1,19), 'picture':'post_test_images/test10.jpg'}
	]

	posts_objects = {}

	reviews = [
		{'username' : 'Alex', 'post_title' : 'PC Rate', 'score' : 4, 'comment' : 'Too much RGB lights', 'date':datetime.datetime(2020,10,11)},
		{'username' : 'Tom', 'post_title' : 'Should I Buy?', 'score' : 2, 'comment' : 'Solid laptop would recommend!', 'date':datetime.datetime(2020,3,10)},
		{'username' : 'Tom', 'post_title' : 'Old Setup', 'score' : 2, 'comment' : 'Everything.', 'date':datetime.datetime(2020,9,11)},
		{'username' : 'Mary123', 'post_title' : 'Office laptop', 'score' : 0, 'comment' : 'That laptop was not made to play games. You need a laptop a newer laptop to play modern games and fix your thermal issue.', 'date':datetime.datetime(2021,2,12)},
		{'username' : 'Mary123', 'post_title' : 'New PC help', 'score' : 0, 'comment' : 'Looks like you do not have any drives plugged into the SATA ports', 'date':datetime.datetime(2021,3,6)},
		{'username' : 'Raptor', 'post_title' : 'New PC help', 'score' : 0, 'comment' : 'Ahh that would make sense why the drives did not appear, thanks.', 'date':datetime.datetime(2021,3,7)},
		{'username' : 'Alex', 'post_title' : 'New PC', 'score' : 5, 'comment' : 'Love the build!', 'date':datetime.datetime(2021,4,3)},
		{'username' : 'Mary123', 'post_title' : 'VR PC', 'score' : 1, 'comment' : 'I would recommend the Core V21 from thermaltake, I use it as a streaming PC and it works wonders!', 'date':datetime.datetime(2020,5,25)},
		{'username' : 'Bob', 'post_title' : 'VR PC', 'score' : 1, 'comment' : 'I will definitely check it out!', 'date':datetime.datetime(2021,5,26)},
		{'username' : 'L1sa', 'post_title' : 'New laptop', 'score' : 0, 'comment' : 'I think it is a bit overkill for a laptop for school!', 'date':datetime.datetime(2021,10,11)},
		{'username' : 'Mary123', 'post_title' : 'New laptop', 'score' : 0, 'comment' : 'I agree, there is definitely better options for a school laptop', 'date':datetime.datetime(2021,10,12)},
		{'username' : 'RobertFC', 'post_title' : 'New laptop', 'score' : 0, 'comment' : 'I am currently selling a used laptop if you are interested in buying one', 'date':datetime.datetime(2021,10,15)},
		{'username' : 'Chloe_', 'post_title' : 'New laptop', 'score' : 0, 'comment' : 'No thank you, I would rather get a new one!', 'date':datetime.datetime(2021,10,16)},
		{'username' : 'Raptor', 'post_title' : 'PC upgrade help', 'score' : 2, 'comment' : 'Did you check its plugged in the right HDMI/Display port?', 'date':datetime.datetime(2021,11,21)},
		{'username' : 'Chloe_', 'post_title' : 'PC upgrade help', 'score' : 2, 'comment' : 'Yeah, its plugged in the right one', 'date':datetime.datetime(2021,11,22)},
		{'username' : 'Raptor', 'post_title' : 'PC upgrade help', 'score' : 1, 'comment' : 'Check that your GPU power cables work and if they dont, it might be a dead card.', 'date':datetime.datetime(2021,11,23)},
		{'username' : 'Chloe_', 'post_title' : 'PC upgrade help', 'score' : 3, 'comment' : 'I switched out the cables and it works thank you!', 'date':datetime.datetime(2021,11,24)},
	]

	for new_user in new_users:
		u = add_user(new_user['username'], new_user['password'], new_user['picture'])
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

def add_user(username, password, picture):
	u = User.objects.create_user(username=username, password=password)
	u.profile.picture=picture
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