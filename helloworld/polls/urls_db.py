from django.conf.urls import url
from helloworld import testdb

urlpatterns = [
    url('^testdb',testdb.testdb),
    url('^add_user/$',testdb.add_user),
    url('^update_psw/$',testdb.update_psw),
    url('^delete_user/$',testdb.delete_user),
    url('^select_user1/$', testdb.select_user1),
    url('^select_user2/$', testdb.select_user2),
    url('^select_user3/$', testdb.select_user3),
    url('^select_user4/$', testdb.select_user4),
    url('^select_user5/$', testdb.select_user5),
    url('^select_user6/$', testdb.select_user6),
    url('^get_json/$', testdb.get_json),
    url('^get_model_to_dict/$', testdb.get_model_to_dict),
    url('^json_data/$', testdb.json_data),

]