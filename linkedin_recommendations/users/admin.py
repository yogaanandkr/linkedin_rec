from django.contrib import admin
from . models import Bio, Recommendations, Posts, Follow
# Register your models here.


admin.site.register(Bio)
admin.site.register(Recommendations)
admin.site.register(Posts)
admin.site.register(Follow)