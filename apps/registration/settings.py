
ALLAUTH_INSTALLED_APPS = [
'allauth',
'allauth.account',
'allauth.socialaccount',
'allauth.socialaccount.providers.facebook',
'allauth.socialaccount.providers.google',
]

SOCIALACCOUNT_PROVIDERS =  {'facebook': {
                                    'METHOD': 'oauth2',
                                    'SCOPE': ['email', 'public_profile', 'user_friends'],
                                    'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
                                    'INIT_PARAMS': {'cookie': True},
                                    'FIELDS': [
                                        'id',
                                        'email',
                                        'name',
                                        'first_name',
                                        'last_name',
                                        'verified',
                                        'locale',
                                        'timezone',
                                        'link',
                                        'gender',
                                        'updated_time',
                                    ],
                                    'EXCHANGE_TOKEN': True,
                                    'LOCALE_FUNC': lambda request:'en_us',
                                    'VERIFIED_EMAIL': False,
                                    'VERSION': 'v2.5',
                                },
                    'google':{
                              'SCOPE': ['email'],
                              'AUTH_PARAMS': { 'access_type': 'online' }
                            },

                            }

SITE_ID = 4

###########################################################################################
# Add the 'allauth' backend to AUTHENTICATION_BACKEND and keep default ModelBackend
AUTHENTICATION_BACKENDS = [ 'django.contrib.auth.backends.ModelBackend',
                           'allauth.account.auth_backends.AuthenticationBackend']
# EMAIL_BACKEND so allauth can proceed to send confirmation emails
# ONLY for development/testing use console
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'

# Custom allauth settings
# Use email as the primary identifier
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True

# Make email verification mandatory to avoid junk email accounts
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Eliminate need to provide username, as it's a very old practice
ACCOUNT_USERNAME_REQUIRED = False

SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_QUERY_EMAIL = True

#Makes user logout immediately after logout is pressed. Doesn't wait for confirmation
# ACCOUNT_LOGOUT_ON_GET = False


#used to display custom signup form
ACCOUNT_SIGNUP_FORM_CLASS = 'apps.registration.forms.SignupForm'
