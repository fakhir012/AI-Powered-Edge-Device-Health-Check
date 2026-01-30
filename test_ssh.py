from ssh_Service import SSHService

ssh = SSHService()

result = ssh.run_command(
    host="127.0.0.1",
    username="fakhir",
    key_path="/cs/home/fakhir/.ssh/id_rsa",
    command="uptime"
)


print(result)

