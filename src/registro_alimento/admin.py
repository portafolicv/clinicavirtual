from django.contrib import admin

# Register your models here.
from .models import Unidad_Medida, Envase, Alimento, Proteina, Lipido, HidratoC, Vitamina, Mineral, ProteinaAlimento, LipidoAlimento, HidratoCAlimento,VitaminaAlimento,MineralAlimento

admin.site.register(Unidad_Medida)
admin.site.register(Envase)
admin.site.register(Alimento)
admin.site.register(Proteina)
admin.site.register(Lipido)
admin.site.register(HidratoC)
admin.site.register(Vitamina)
admin.site.register(Mineral)
admin.site.register(ProteinaAlimento)
admin.site.register(LipidoAlimento)
admin.site.register(HidratoCAlimento)
admin.site.register(VitaminaAlimento)
admin.site.register(MineralAlimento)