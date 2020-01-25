from mozilla_django_oidc.auth import OIDCAuthenticationBackend

import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.full_load(ymlfile)

def provider_logout(request):
    redirect_url = 'https://iddev.fedorainfracloud.org/logout'
    return redirect_url

class OIDC(OIDCAuthenticationBackend):
    def update_user(self, user, claims):
        if user.username in cfg['auth']['admins']:
            if not user.is_superuser: 
                user.is_superuser = True
                user.is_staff = True
        else:
            if user.is_superuser:
                user.is_staff = False
                user.is_superuser = False
        user.save()
        return user
    
    def create_user(self, claims):
        user = super(OIDC, self).create_user(claims)
        user.username = claims.get('nickname', '')
        user.email = claims.get('email', '')
        try:
            user.first_name = claims.get('name', '')
        except:
            user.first_name = user.username
        user.save()
        return self.update_user(user,claims)
        