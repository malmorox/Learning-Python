class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = []
        self.status = False

    def power_on(self):
        self.status = True
        print("El teléfono está encendido.")

    def power_off(self):
        self.status = False
        print("El teléfono está apagado.")

    def install_app(self, *apps: str):
        for app in apps:
            if app not in self.apps:
                self.apps.append(app)

    def uninstall_app(self, app: str):
        if app in self.apps:
            self.apps.remove(app)