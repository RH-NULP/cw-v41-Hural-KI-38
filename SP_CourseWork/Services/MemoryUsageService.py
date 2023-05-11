# Importing Libraries
import psutil


# MemoryUsageService
class MemoryUsageService:
    # Method
    @staticmethod
    def get_memory_usage_percent():
        return psutil.virtual_memory().percent
