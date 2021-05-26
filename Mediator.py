class WindowBase:
    def show(self):
        pass

    def hide(self):
        pass


class MainWindow(WindowBase):
    def show(self):
        print('Показать MainWindow')

    def hide(self):
        print('Скрыть MainWindow')


class SettingWindow(WindowBase):
    def show(self):
        print('ПОказать SettingWindow')

    def hide(self):
        print('Скрыть SettingWindow')


class HelpWindow(WindowBase):
    def show(self):
        print('Показать HelpWindow')

    def hide(self):
        print('Скрыть HelpWindow')


class WindowMediator:
    def __init__(self):
        self.windows = dict.fromkeys(['main', 'setting', 'help'])

    def show(self, win):
        for window in self.windows.values():
            if not window is win:
                window.hide()
        win.show()

    def set_main(self, win):
        self.windows['main'] = win

    def set_setting(self, win):
        self.windows['setting'] = win

    def set_help(self, win):
        self.windows['help'] = win


main_win = MainWindow()
setting_win = SettingWindow()
help_win = HelpWindow()

med = WindowMediator()
med.set_main(main_win)
med.set_setting(setting_win)
med.set_help(help_win)

main_win.show()

med.show(setting_win)

med.show(help_win)