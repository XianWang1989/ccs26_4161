
url(r'^edit/image/(?P<slug>[\w-]+)/$', EditImage.as_view(), name="editImage"),
url(r'^edit/space/(?P<slug>[\w-]+)/$', EditSpaceView.as_view(), name="editSpace"),
