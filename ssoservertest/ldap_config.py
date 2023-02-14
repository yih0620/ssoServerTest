# ldap_config.py
import ldap
from django_auth_ldap.config import LDAPSearchUnion, LDAPSearch, GroupOfNamesType

# use ldap to auth first
AUTHENTICATION_BACKENDS = [
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_LDAP_SERVER_URI = "ldap://192.168.10.1:389"  # ldap or ad address
AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_BIND_DN = 'PCRD-AD'
AUTH_LDAP_BIND_PASSWORD = 'IBGbgmuuvv@201909'

AUTH_LDAP_USER_SEARCH = LDAPSearch("OU=MPI,DC=mpi,DC=com,DC=tw",
                                   ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")

AUTH_LDAP_GROUP_SEARCH = LDAPSearch("OU=MPI,DC=mpi,DC=com,DC=tw",
    ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"
)

AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()


AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

#AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#    "is_staff": "CN=FAB)湖口管理看板,OU=MPI,DC=mpi,DC=com,DC=tw",
#    "is_superuser": "CN=資訊室維運課,OU=MPI,DC=mpi,DC=com,DC=tw",
#}

AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_DEBUG_LEVEL: 1,
    ldap.OPT_REFERRALS: 0,
}

# ldap info mapping to django user col
# django user col: ldap info
AUTH_LDAP_USER_ATTR_MAP = {
    'username': 'sAMAccountName',
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

#如果為True，每次組成員都從ldap重新獲取，保證組成員的即時性；反之會對組成員進行緩存，提升性能，但是降低即時性
AUTH_LDAP_FIND_GROUP_PERMS = True


##AUTH_LDAP_USER_SEARCH = LDAPSearch(
##    "dc=djangoTestAd,dc=local", ldap.SCOPE_SUBTREE, "uid=%(user)s"
##)


#AUTH_LDAP_USER_SEARCH = LDAPSearch("OU=MPI,DC=mpi,DC=com,DC=tw",
#                                   ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")


##get group
#AUTH_LDAP_GROUP_SEARCH = LDAPSearch("OU=MPI,DC=mpi,DC=com,DC=tw",
#    ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"
#)

#AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr='cn')

##is_staff:can enter user manage;  is_superuser:can create user;  is_active:can login
#AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#   "is_staff": ("cn=super,OU=MPI,DC=mpi,DC=com,DC=tw", "cn=staff,OU=MPI,DC=mpi,DC=com,DC=tw",),
#   "is_superuser": "cn=super,OU=MPI,DC=mpi,DC=com,DC=tw"
#}
##AUTH_LDAP_USER_FLAGS_BY_GROUP = {
##    "is_staff": "CN=FAB)湖口管理看板,OU=MPI,DC=mpi,DC=com,DC=tw",
##    "is_superuser": "CN=資訊室維運課,OU=MPI,DC=mpi,DC=com,DC=tw",
##}

## if ldap server is on windows server
#AUTH_LDAP_CONNECTION_OPTIONS = {
#    ldap.OPT_DEBUG_LEVEL: 1,
#    ldap.OPT_REFERRALS: 0,
#}

## ldap info mapping to django user col
## django user col: ldap info
#AUTH_LDAP_USER_ATTR_MAP = {
#    'username': 'sAMAccountName',
#    "first_name": "givenName",
#    "last_name": "sn",
#    "email": "mail"
#}

## check out every time
#AUTH_LDAP_FIND_GROUP_PERMS = True


##-----------------------------------
#AUTH_LDAP_SERVER_URI = 'ldap://192.168.10.1:389'

#AUTH_LDAP_BIND_DN = 'PCRD-AD'
#AUTH_LDAP_BIND_PASSWORD = 'IBGbgmuuvv@201909'
#import ldap
#from django_auth_ldap.config import LDAPSearch, GroupOfNamesType


#AUTH_LDAP_USER_SEARCH = LDAPSearch("OU=MPI,DC=mpi,DC=com,DC=tw",
#                                   ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")

#AUTH_LDAP_GROUP_SEARCH = LDAPSearch("OU=MPI,DC=mpi,DC=com,DC=tw",
#    ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"
#)

#AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()


#AUTHENTICATION_BACKENDS = (
#    'django_auth_ldap.backend.LDAPBackend',
#    'django.contrib.auth.backends.ModelBackend',
#)

#AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#    "is_staff": "CN=FAB)湖口管理看板,OU=MPI,DC=mpi,DC=com,DC=tw",
#    "is_superuser": "CN=資訊室維運課,OU=MPI,DC=mpi,DC=com,DC=tw",
#}

#AUTH_LDAP_CONNECTION_OPTIONS = {
#    ldap.OPT_DEBUG_LEVEL: 1,
#    ldap.OPT_REFERRALS: 0,
#}

#AUTH_LDAP_USER_ATTR_MAP = {
#    "first_name": "givenName",
#    "last_name": "sn",
#    "email": "mail"
#}

##如果為True，每次組成員都從ldap重新獲取，保證組成員的即時性；反之會對組成員進行緩存，提升性能，但是降低即時性
#AUTH_LDAP_FIND_GROUP_PERMS = True
