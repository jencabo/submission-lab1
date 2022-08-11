#-------------------------------------------
# Buzzerboy Template Portal Application
# Developed by: Fahad Zain Jawaid (fjawaid@buzzerboy.com)
# This model file should be lite, it serves as Super classes for all 
# -----------------------------------------------
# Each model should have the following requirements:
# ---- 1) Audit Trail on each record (Created At, Created By, Last Updated At, Last Updated By)
# ---- 2) Some tables will be unilingual, and other tables will be multilingual, Multlingual tables
# ---------- will store a language key field to track what language the row is in. This way, multiple
#----------- rows of that table can together form a language specific value stream
#-------------------------------------------------
# All portals that are based on this template will have authentication (username/password), and 
# --- so core portal app will include that functionality. 
# All portals will also support multilingualism, so that functionalility will be part of the core 
# --- as well. This will include a table for SupportedLanguages
# -----------------------------------------------

#Necessary imports
from django.db import models
from django.contrib.auth.models import User
import uuid

#CORE MODELS
class SupportedLanguage(models.Model):
    languageKey = models.CharField(max_length=4)
    description = models.CharField(max_length=255)
    flagURL = models.TextField
    flagPic = models.ImageField(null=True, blank=True, default="", upload_to="settings/flags")

    def __str__(self):
        return self.description + " (" + self.languageKey + ")"

    def flag_img (self):
        return "<img id=flag'" + self.id.__str__() + "' src='" + self.flag_url + "'/>"

    @property
    def flag_url(self):
	    if self.flagPic and hasattr(self.flagPic, 'url'):
		    return self.flagPic.url 


#INHERITABLE MODELS
class AuditableBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True

class MutlilingualBaseModel(AuditableBaseModel):
    language = models.ForeignKey(SupportedLanguage, on_delete=models.DO_NOTHING)
    obj_lang_uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
        unique_together = ('id', 'language',)
