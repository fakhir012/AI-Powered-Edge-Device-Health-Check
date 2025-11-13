from base_Service import BaseService
import paramiko
import json

class SSHService(BaseService):
      def __init__(self):
        super().__init__("SSHService")
 def start(self) -> None:
        super().start() #loads SSH keys or configuration here
