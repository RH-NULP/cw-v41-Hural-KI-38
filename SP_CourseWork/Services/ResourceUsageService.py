# Importing Libraries
import psutil


# ResourceUsageService
class ResourceUsageService:
    # Method
    @staticmethod
    def get_resource_usage():
        # CPU Usage
        cpu_percent = psutil.cpu_percent()

        # Memory Usage
        mem = psutil.virtual_memory()
        mem_percent = mem.percent

        # Disk Usage
        disk = psutil.disk_usage('/')
        disk_percent = disk.percent

        # Network Connections
        net_io_counters = psutil.net_io_counters()
        bytes_sent = net_io_counters.bytes_sent
        bytes_recv = net_io_counters.bytes_recv

        return {
            'cpu_percent': cpu_percent,
            'mem_percent': mem_percent,
            'disk_percent': disk_percent,
            'bytes_sent': bytes_sent,
            'bytes_recv': bytes_recv
        }
