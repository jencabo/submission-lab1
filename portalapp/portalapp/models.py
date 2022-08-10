#-------------------------------------------
# Buzzerboy Template Portal Application
# Developed by: Fahad Zain Jawaid (fjawaid@buzzerboy.com)
# This model file should be lite, it serves as Super classes for all 
# sub application models.
# -----------------------------------------------
# Each model should have the following requirements:
# ---- 1) Audit Trail on each record (Created, Created By, Last Updated, Last Updated By)
# ---- 2) Some tables will be unilingual, and other tables will be multilingual, Multlingual tables
# ---------- will store a language key field to track what language the row is in. This way, multiple
#----------- rows of that table can together form a language specific value stream
#-------------------------------------------------
# All portals that are based on this template will have authentication (username/password), and 
# --- so core portal app will include that functionality. 
# All portals will also support multilingualism, so that functionalility will be part of the core 
# --- as well. This will include a table for SupportedLanguages
# -----------------------------------------------
