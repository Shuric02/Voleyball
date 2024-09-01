from django.contrib import admin

# Register your models here.

from .models import Web_admins, Players, СoefficientsOfCharacteristics, MatchHistory, MatchTeam, Team


admin.site.register(Players)
admin.site.register(Web_admins)
admin.site.register(СoefficientsOfCharacteristics)
admin.site.register(Team)
admin.site.register(MatchTeam)
admin.site.register(MatchHistory)