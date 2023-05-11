# Importing Libraries
import psutil


# ProcessInfoService
class ProcessInfoService:
    # Method
    @staticmethod
    def get_process_info():
        process_list = []
        for process in psutil.process_iter():
            try:
                process_info = process.as_dict(attrs=['pid', 'name', 'status', 'memory_info', 'create_time'])
                process_list.append(process_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return process_list
