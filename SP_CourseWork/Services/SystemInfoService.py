# Importing Libraries
import platform
import psutil


# SystemInfoService
class SystemInfoService:
    # Methods
    @staticmethod
    def get_system():
        return platform.system()

    @staticmethod
    def get_node():
        return platform.node()

    @staticmethod
    def get_version():
        return platform.version()

    @staticmethod
    def get_processor():
        return platform.processor()

    @staticmethod
    def get_cpu_count():
        return psutil.cpu_count(logical=True)

    @staticmethod
    def get_total_virtual_memory():
        return psutil.virtual_memory().total
