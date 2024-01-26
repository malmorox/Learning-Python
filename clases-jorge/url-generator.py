def host_generator(protocol:bool,domain:str,path:str):
    def url_generator(usuario:str,id_user:str):
        return print(f'{"https" if protocol else "http"}://{domain}/{path}/{usuario}/{id_user}')
    return url_generator

generator = host_generator(True, 'example.com', 'path')
generator('username', '123')
