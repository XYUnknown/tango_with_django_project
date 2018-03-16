from registration.backends.simple.views import RegistrationView
from rango.models import UserProfile
from rango.forms import UserRegistrationForm


class MyRegistrationView(RegistrationView):
    form_class = UserRegistrationForm
    success_url = '/accounts/register/'

    def register(self, form):
        new_user = super(MyRegistrationView, self).register(form)
        print(form.cleaned_data)
        user_profile = UserProfile()
        user_profile.user = new_user
        if form.is_valid():
            print("valid")
            user_profile.website = form.cleaned_data['website']
            print(user_profile.website)
            user_profile.picture = form.cleaned_data['picture']
            new_user.save()
            user_profile.save()
        else:
            print("not valid")
        return new_user

    def get_success_url(self, user):
        return self.success_url
