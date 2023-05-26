from allauth.account.adapter import DefaultAccountAdapter

class Silant_projectAccountAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request):
        return False