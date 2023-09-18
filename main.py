import subprocess

def ping_ip(ip):
    try:
        # Use o comando ping para verificar a conectividade
        subprocess.check_output(["ping", "-c", "1", ip])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    # Lista de IPs para pingar
    ips = ["10.100.1.21", "10.100.1.22", "10.100.1.26"]

    for ip in ips:
        if ping_ip(ip):
            print(f"{ip} está acessível.")
        else:
            print(f"{ip} não está acessível.")

if __name__ == "__main__":
    main()
