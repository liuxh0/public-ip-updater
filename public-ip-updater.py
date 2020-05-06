import http.client
import sys
import time

def main():
    arguments = sys.argv[1:]
    if len(arguments) < 1:
        print('Missing id in argument')
        sys.exit()

    id = arguments[0]
    update_interval = int(arguments[1]) if len(arguments) > 1 else 60

    last_ip = ''
    while True:
        public_ip = get_public_ip()
        print('Public IP: ', public_ip)

        if public_ip != last_ip:
            update_public_ip(id, public_ip)
            last_ip = public_ip

        time.sleep(update_interval)

def get_public_ip() -> str:
    connection = http.client.HTTPSConnection('api.ipify.org')
    connection.request('GET', '')
    response = connection.getresponse()
    response_body = response.read().decode('utf-8')
    connection.close()

    return response_body

def update_public_ip(id: str, value: str) -> None:
    print('Start updating...')

    connection = http.client.HTTPSConnection('m8eovl6ek1.execute-api.eu-central-1.amazonaws.com')
    connection.request('PUT', '/Prod/' + id, value)
    response = connection.getresponse()
    connection.close()

    if response.status == 200:
        print('Update successfully')
    else:
        print('Update failed')
        sys.exit()

if __name__ == '__main__':
    main()
