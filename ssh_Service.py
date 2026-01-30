from base_Service import BaseService
import paramiko

class SSHService(BaseService):
    def __init__(self):
        super().__init__("SSHService")

    def run_command(self, host, username, key_path, command):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Load RSA key explicitly
            key = paramiko.RSAKey.from_private_key_file(key_path)

            ssh.connect(
                hostname=host,
                username=username,
                pkey=key
            )

            stdin, stdout, stderr = ssh.exec_command(command)

            result = {
                "ok": True,
                "command": command,
                "output": stdout.read().decode(),
                "error": stderr.read().decode()
            }

            ssh.close()
            return result

        except Exception as e:
            return {"ok": False, "error": str(e)}
