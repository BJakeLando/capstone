from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Peep

class ProfileInLine(admin.StackedInline):
    model = Profile
# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    # Just display username fields on admin page
    fields = ["username"]
    inlines = [ProfileInLine]

# Unregister initial user
admin.site.unregister(User)
# Reregister User
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)


admin.site.register(Peep)
