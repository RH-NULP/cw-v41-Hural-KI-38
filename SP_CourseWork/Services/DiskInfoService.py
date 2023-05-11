# Importing Libraries
import psutil


# DiskInfoService
class DiskInfoService:
    # Method
    @staticmethod
    def get_disk_info():
        disk_info = []
        for partition in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                total = round(usage.total / (1024 * 1024 * 1024), 2)
                free = round(usage.free / (1024 * 1024 * 1024), 2)
                used = round(usage.used / (1024 * 1024 * 1024), 2)
                disk_info.append((partition.mountpoint, total, free, used))
            except Exception as e:
                print(f"Error getting disk usage info for {partition.mountpoint}: {e}")
        return disk_info
