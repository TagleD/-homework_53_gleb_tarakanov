class DataBase:
    choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('made', 'Сделано')]

    @classmethod
    def get_status(cls, status):
        for choice in cls.choices:
            if choice[0] == status:
                return choice[1]
