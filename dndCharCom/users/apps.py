from django.apps import AppConfig

#make sure to link your user app to the rest of the code
#it needs to be referenced here and in the project URL folder
# we need a templates folder in order to actually load HTML on the page, capture form data, etc.

class UsersConfig(AppConfig):
    name = 'users'
