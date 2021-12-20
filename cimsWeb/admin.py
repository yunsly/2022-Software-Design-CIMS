from django.contrib import admin
from .models import SocialDistanceLevelOfRegion
from .models import MetroCity
from .models import Do
from .models import SelfGoverningDo
from .models import SelfGoverningSi
from .models import Si
from .models import Gun
from .models import CoronicStatusOfRegion, CoronicStatusOfKorea
from .models import SocialDistanceLevel


admin.site.register(SocialDistanceLevelOfRegion)
admin.site.register(MetroCity)
admin.site.register(Do)
admin.site.register(SelfGoverningDo)
admin.site.register(SelfGoverningSi)
admin.site.register(Si)
admin.site.register(Gun)
admin.site.register(SocialDistanceLevel)
admin.site.register(CoronicStatusOfRegion)
admin.site.register(CoronicStatusOfKorea)
