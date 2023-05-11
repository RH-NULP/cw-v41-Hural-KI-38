# Importing Libraries
import psutil


# NetworkConnectionsService
class NetworkConnectionsService:
    # Method
    @staticmethod
    def get_network_connections():
        connections = psutil.net_connections()
        connection_list = []
        for conn in connections:
            if conn.status == 'ESTABLISHED':
                connection_list.append({'protocol': conn.type,
                                        'local_address': f'{conn.laddr.ip}:{conn.laddr.port}',
                                        'remote_address': f'{conn.raddr.ip}:{conn.raddr.port}',
                                        'status': conn.status})
        return connection_list
