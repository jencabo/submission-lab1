from core.seed_data import SupportedLanguages
from core.seed_data.SupportedLanguages import SupportedLanguages_SeedData

class SeedData:

    @staticmethod
    def load(delete_old_data = True):

        #Delete old data if allowed. This may be required to preserve referrential integrity
        if delete_old_data:
            pass     

        #1. SupportedLanguages
        SupportedLanguages_SeedData.seed_data(delete_old_data)


