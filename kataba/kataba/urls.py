from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Admin
from django.contrib import admin
from board.models import post, board, thread
admin.autodiscover()
admin.site.register([post, thread, board])


urlpatterns = patterns('',
	# Index page
	url(r'^$',include('board.urls')),
	
	# Boards
	url(r'^(?P<boardname>[a-z]{1,3})/(?P<page>[1-9]?)$','board.views.viewboard',name='board'),
	
	# Threads
	url(r'^thread/(?P<thread_id>[0-9]+)/$','board.views.viewthread',name='viewthread'),
	
	# Posts
	url(r'^post/(?P<post_id>[0-9]+)/$','board.views.viewpost',name='viewpost'),
	
	# Update thread
	url(r'^thread/update/(?P<thread_id>[0-9]+)/(?P<posts_numb>[0-9]+)$','board.views.updatethread',name='updatethread'),

	# Add post
	url(r'^thread/(?P<thread_id>[0-9]+)/addpost$','board.views.addpost',name='addpost'),
	
	# Admin
	url(r'^admin/', include(admin.site.urls)),
	
	# Captcha
	url(r'^captcha/', include('captcha.urls')),
	
	# Cloud thread vision
	url(r'^(?P<boardname>[a-z]{1,3})/cloud$','board.views.cloud',name='addpost'),
)

#files
urlpatterns += static('images', document_root='images/')
