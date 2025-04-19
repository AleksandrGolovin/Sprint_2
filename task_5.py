# Задание 5
# Создать класс, который подсчитывает результаты состязаний — Results. И двух его наследников — 
# Football и Hockey. Подклассы наследуют все атрибуты, а ещё у них есть свои методы.
# 1. Напиши класс Results. Проинициализируй в нём атрибуты victories, draws, losses через конструктор.
# 2. Напиши класс Football, который наследуется от класса Results. Его методы:
# * number_of_wins(), который должен возвращать запись вида Футбольных побед: 1.
# Количество побед должно браться из переменной victories.
# * number_of_draws(), который должен возвращать запись вида Футбольных ничьих: 1.
# Количество ничьих должно браться из переменной draws.
# * number_of_losses(), который должен возвращать запись вида Футбольных поражений: 1.
# Количество поражений возьми из переменной losses.
# * total_points(), который должен возвращать запись вида Общее количество очков: 5.
# Количество очков рассчитай формуле: 3*количество побед + количество ничьих.
# 3. Напиши класс Hockey, который наследуется от класса Results. Его методы:
# * number_of_wins(), который должен возвращать запись вида Хоккейных побед: 1.
# Количество побед метод берёт из переменной victories.
# * number_of_draws(), который должен возвращать запись вида Хоккейных ничьих: 1.
# Количество ничьих метод берёт из переменной draws.
# * number_of_losses(), который должен возвращать запись вида Хоккейных поражений: 1.
# Количество поражений должно браться из переменной losses.
# * total_points(), который должен возвращать запись вида Общее количество очков: 5.
# Количество очков рассчитывается по формуле: 2*количество побед + количество ничьих.
# 4. Создай объекты football_team и hockey_team классов Football и Hockey соответственно.
# В качестве параметров передай (2, 2, 2).
# 5. Вызови все методы для объектов football_team и hockey_team.
# Используй цикл for. Названия методов при этом не должны повторяться для обоих объектов.

class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses

    def number_of_wins(self):
        return f'{self.get_title_by_child_type(self)} побед: {self.victories}'
    
    def number_of_draws(self):
        return f'{self.get_title_by_child_type(self)} ничьих: {self.draws}'
    
    def number_of_losses(self):
        return f'{self.get_title_by_child_type(self)} поражений: {self.losses}'
    
    def total_points(self):
        points_rules = self.get_points_rules_by_child_type(self)
        points = points_rules['victory'] * self.victories + points_rules['draw'] * self.draws
        return f"Общее количество очков: {points}"
    
    @classmethod
    def get_instance_methods(cls):
        return [
            name for name, attr in vars(cls).items()
            if not isinstance(attr, (classmethod, staticmethod))  # Не классовые, не статические
            and not (name.startswith('__') and name.endswith('__'))  # Не магические
        ]

    @staticmethod
    def get_title_by_child_type(child_type) -> str:
        match type(child_type).__name__:
            case 'Football':
                return "Футбольных"
            case 'Hockey':
                return "Хоккейныйх"
            case _:
                return "Неизвестных"
    
    @staticmethod
    def get_points_rules_by_child_type(child_type) -> dict[str, int]:
        match type(child_type).__name__:
            case 'Football':
                return {'victory': 3, 'draw': 1}
            case 'Hockey':
                return {'victory': 2, 'draw': 1}
            case _:
                return {'victory': 0, 'draw': 0}
    
class Football(Results):
    pass

class Hockey(Results):
    pass
    
# Экземпляры классов
football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

# Вывести в консоль
for team in (football_team, hockey_team):
    for method in Results.get_instance_methods():
        print(getattr(team, method)())