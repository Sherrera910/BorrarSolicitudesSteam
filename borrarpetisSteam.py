import subprocess
import sys

def run_steamcmd(command, steam_guard_code=None):
    steamcmd_path = "SteamCMD"
    login_command = f"login usuario contraseña"
    
    if steam_guard_code:
        login_command += f" {steam_guard_code}"
    
    full_command = f"{steamcmd_path}/steamcmd {login_command} +{command} +quit"
    result = subprocess.run(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

def get_friend_requests(steam_guard_code=None):
    output = run_steamcmd("friends_request_list", steam_guard_code)
    friend_requests = []
    for line in output.splitlines():
        if "Friend request from" in line:
            steam_id = line.split()[-1]
            friend_requests.append(steam_id)
    return friend_requests

def decline_friend_request(steam_id, steam_guard_code=None):
    run_steamcmd(f"friends_deny_request {steam_id}", steam_guard_code)

def main():
    if len(sys.argv) < 2:
        print("Por favor, proporciona el código de autenticación de Steam Guard ")
        sys.exit(1)

    steam_guard_code = sys.argv[1]
    friend_requests = get_friend_requests(steam_guard_code)
    print(f"Se encontraron {len(friend_requests)} solicitudes de amistad.")
    
    for steam_id in friend_requests:
        print(f"Rechazando solicitud de amistad de {steam_id}...")
        decline_friend_request(steam_id, steam_guard_code)

    print("Todas las solicitudes de amistad han sido rechazadas.")

if __name__ == "__main__":
    main()

