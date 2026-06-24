import json
import random
from datetime import datetime, timedelta

class Exercise:
    def __init__(self, name, calories, sets_or_duration, ex_type):
        self.name = name
        self.calories = calories
        self.sets_or_duration = sets_or_duration
        self.ex_type = ex_type


class Meal:
    def __init__(self, name, calories, date):
        self.name = name
        self.calories = calories
        self.date = date


class User:
    def __init__(self, name, goal):
        self.name = name
        self.goal = goal
        self.exercises = []
        self.meals = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def add_meal(self, meal):
        self.meals.append(meal)

    def today_calories_burned(self):
        today = datetime.now().strftime("%Y-%m-%d")
        return sum(ex.calories for ex in self.exercises if ex.date == today)

    def today_calories_eaten(self):
        today = datetime.now().strftime("%Y-%m-%d")
        return sum(m.calories for m in self.meals if m.date == today)


class FitnessTracker:
    def __init__(self):
        self.user = None
        self.exercises_list = [
            ("Лицеви опори", 5, "strength"),
            ("Клекове", 7, "strength"),
            ("Коремни преси", 4, "strength"),
            ("Набирания", 8, "strength"),
            ("Бягане", 10, "cardio"),
            ("Колоездене", 8, "cardio"),
            ("Скачане на въже", 12, "cardio"),
            ("Плуване", 11, "cardio")
        ]
        self.foods_list = [
            ("Пиле с ориз", 500),
            ("Салата", 200),
            ("Сандвич", 450),
            ("Яйца", 300),
            ("Кисело мляко", 180),
            ("Плодове", 150)
        ]

    def create_user(self, name, goal):
        self.user = User(name, goal)
        print(f"Здравей, {name}!")

    def add_exercise(self):
        if not self.user:
            print("Първо създай профил!")
            return

        print("\nИзбери упражнение:")
        for i, (name, cal, ex_type) in enumerate(self.exercises_list, 1):
            type_text = "(силово)" if ex_type == "strength" else "(кардио)"
            print(f"{i}. {name} {type_text} - {cal} калории")

        choice = int(input("> ")) - 1

        name, cal_per_unit, ex_type = self.exercises_list[choice]

        if ex_type == "strength":
            sets = int(input("Колко серии? "))
            actual_cal = cal_per_unit * sets
            ex = Exercise(name, actual_cal, sets, "strength")
        else:
            duration = int(input("Колко минути? "))
            actual_cal = cal_per_unit * duration
            ex = Exercise(name, actual_cal, duration, "cardio")

        today = datetime.now().strftime("%Y-%m-%d")
        ex.date = today
        self.user.add_exercise(ex)

        if ex_type == "strength":
            print(f"Добавено: {name}, {sets} серии, {actual_cal} калории")
        else:
            print(f"Добавено: {name}, {duration} мин, {actual_cal} калории")

    def add_meal(self):
        if not self.user:
            print("Първо създай профил!")
            return

        print("\nИзбери храна:")
        for i, (name, cal) in enumerate(self.foods_list, 1):
            print(f"{i}. {name} ({cal} калории)")

        choice = int(input("> ")) - 1
        name, cal = self.foods_list[choice]

        today = datetime.now().strftime("%Y-%m-%d")
        meal = Meal(name, cal, today)
        self.user.add_meal(meal)
        print(f"Добавено: {name}, {cal} калории")

    def daily_report(self):
        if not self.user:
            print("Първо създай профил!")
            return

        eaten = self.user.today_calories_eaten()
        burned = self.user.today_calories_burned()
        balance = eaten - burned

        print("\n=== ДНЕВЕН ОТЧЕТ ===")
        print(f"Приети калории: {eaten}")
        print(f"Изгорени калории: {burned}")
        print(f"Баланс: {balance}")

        if self.user.goal == "lose":
            if balance < 0:
                print("Супер! В калориен дефицит си.")
            else:
                print("Внимавай! Приел си повече, отколкото си изгорил.")
        else:
            if balance > 0:
                print("Супер! В калориен излишък си.")
            else:
                print("Трябва да ядеш повече за да качиш маса.")

    def history(self):
        if not self.user:
            print("Първо създай профил!")
            return

        print("\n=== ПОСЛЕДНИ ТРЕНИРОВКИ ===")
        for ex in self.user.exercises[-5:]:
            if ex.ex_type == "strength":
                print(f"{ex.date}: {ex.name} - {ex.sets_or_duration} серии, {ex.calories} кал")
            else:
                print(f"{ex.date}: {ex.name} - {ex.sets_or_duration} мин, {ex.calories} кал")

        print("\n=== ПОСЛЕДНИ ХРАНЕНИЯ ===")
        for meal in self.user.meals[-5:]:
            print(f"{meal.date}: {meal.name} - {meal.calories} кал")

    def save_data(self, filename="data.json"):
        if not self.user:
            return

        data = {
            "name": self.user.name,
            "goal": self.user.goal,
            "exercises": [{"name": e.name, "calories": e.calories,
            "sets_or_duration": e.sets_or_duration,
            "ex_type": e.ex_type, "date": e.date}
                for e in self.user.exercises], "meals": [{"name": m.name, "calories": m.calories, "date": m.date} for m in self.user.meals]
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Запазено!")

    def load_data(self, filename="data.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.user = User(data["name"], data["goal"])

            for ex in data["exercises"]:
                e = Exercise(ex["name"], ex["calories"], ex["sets_or_duration"], ex["ex_type"])
                e.date = ex["date"]
                self.user.add_exercise(e)

            for m in data["meals"]:
                meal = Meal(m["name"], m["calories"], m["date"])
                self.user.add_meal(meal)

            print(f"Данните са заредени. Здравей, {self.user.name}!")
            return True
        except:
            return False

# menu:

def main():
    tracker = FitnessTracker()

    print("=== ФИТНЕС ТРАКЕР ===")

    if not tracker.load_data():
        print("\nНов профил:")
        name = input("Име: ")
        goal = input("Цел (lose/gain): ")
        tracker.create_user(name, goal)

    while True:
        print("\n" + "-" * 30)
        print("1. Добави тренировка")
        print("2. Добави хранене")
        print("3. Дневен отчет")
        print("4. История")
        print("5. Запази и изход")

        choice = input("\n> ")

        if choice == "1":
            tracker.add_exercise()
        elif choice == "2":
            tracker.add_meal()
        elif choice == "3":
            tracker.daily_report()
        elif choice == "4":
            tracker.history()
        elif choice == "5":
            tracker.save_data()
            print("Чао!")
            break


if __name__ == "__main__":
    main()