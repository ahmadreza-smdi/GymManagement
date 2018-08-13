from crudbuilder.abstract import BaseCrudBuilder
from .models import Member
class MemberCrud(BaseCrudBuilder):
    model = Member
    search_fields = ['name']
    tables2_fields = ('name','phone_number','birth_date','first_session_date','sex','age','skill','profile')
    tables2_pagination = 20
    modelform_excludes = ['user']
    login_required = True
    