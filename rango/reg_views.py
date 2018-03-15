from registration.backends.simple.views import RegistrationView
from rango.models import UserProfile
from rango.forms import UserRegistrationForm


class MyRegistrationView(RegistrationView):
    form = UserRegistrationForm()

    def register(self, form):
        new_user = super(MyRegistrationView, self).register(form)
        user_profile = UserProfile()
        user_profile.user = new_user
        if 'website' in form:
            user_profile.website = form.cleaned_data['website']
        if 'picture' in form:
            user_profile.picture = form.cleaned_data['picture']
        #new_user.save()
        user_profile.save()
        return new_user

    def get_success_url(self, user):
        return '/accounts/register/'
