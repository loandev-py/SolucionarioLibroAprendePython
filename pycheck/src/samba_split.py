# ***********************
# SEPARANDO RECURSO SAMBA
# ***********************

def run(smb_path: str) -> tuple:
    # TU CÓDIGO AQUÍ
    smb_path = smb_path.strip('//')
    host, path = smb_path.split('/',1)

    return host, '/'+path


if __name__ == '__main__':
    run('//1.1.1.1/aprende/python')