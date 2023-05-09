import datetime
import math
import random

def difference_between_tenses():
    return "Present Simple описує рутинні дії або загальні істини, а Present Continuous описує дії, які відбуваються прямо зараз."

def difference_between_noun_and_adjective():
    return "Іменник - це слово, яке називає предмет, особу, місце або ідею. Прикметник - це слово, яке описує або характеризує іменник."

def dative_verb_formation():
    return "Дієслова не мають відмінків. Відмінки мають іменники, прикметники, числівники та займенники."

def distance_between_earth_and_sun():
    return "Середня відстань між Землею та Сонцем становить близько 93 мільйонів миль (150 мільйонів кілометрів)."

def asteroids_and_comets():
    return "Астероїди - це невеликі тіла сонячної системи, що орбітують навколо Сонця. Комети - це тіла сонячної системи, що містять лід та складаються з різних матеріалів. Вони мають орбіти навколо Сонця, які часто мають високу ексцентриситет."

def current_season():
    month = datetime.datetime.now().month
    if 3 <= month <= 5:
        return "Весна"
    elif 6 <= month <= 8:
        return "Літо"
    elif 9 <= month <= 11:
        return "Осінь"
    else:
        return "Зима"

def sing_carols():
    carols = [
        "Тиха ніч, свята ніч! Все спить, одна зоря...",
        "Радість на світ народилась, христос народився!",
        "Небо і земля нині торжествують...",
    ]
    return random.choice(carols)

def current_month():
    return datetime.datetime.now().strftime("%B")

def inspiring_quotes():
    quotes = [
        "Живи, як зірка, що не гасне, хоч і небеса покриють хмарами.",
        "Найкращий спосіб передбачити майбутнє - створити його.",
        "Сміливість - це не відсутність страху, а перемога над ним.",
        "Справжній успіх - це бути вірним своїм снам.",
        "Завжди прагніть добра, навіть якщо хочеться все кинути."
    ]
    return random.choice(quotes)

def newtons_law_of_universal_gravitation():
    m1 = float(input("Введіть масу першого тіла (кг): "))
    m2 = float(input("Введіть масу другого тіла (кг): "))
    r = float(input("Введіть відстань між тілами (м): "))
    
    G = 6.67430 * 10**(-11)
    F = G * (m1 * m2) / r**2
    return F


def stefan_boltzmann_law():
    A = float(input("Введіть площу поверхні (м^2): "))
    T = float(input("Введіть температуру (K): "))
    
    sigma = 5.6703 * 10**(-8)
    P = sigma * A * T**4
    return P


def planck_constant():
    return "Стала Планка дорівнює 6.62607015 × 10^(-34) Js"

def distance_between_two_points_3D(x1, y1, z1, x2, y2, z2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance

def length_of_circle_arc():
    r = float(input("Введіть радіус кола: "))
    theta = float(input("Введіть кут у градусах: "))

    arc_length = r * math.radians(theta)
    return f"Довжина дуги кола: {arc_length:.2f}"


def trapezoid_area():
    a = float(input("Введіть довжину першої основи трапеції: "))
    b = float(input("Введіть довжину другої основи трапеції: "))
    h = float(input("Введіть висоту трапеції: "))

    area = (a + b) * h / 2
    return f"Площа трапеції: {area:.2f}"


def sine_and_cosine():
    x = float(input("Введіть кут в радіанах: "))
    sin_x = math.sin(x)
    cos_x = math.cos(x)
    return f"Синус кута: {sin_x:.2f}, Косинус кута: {cos_x:.2f}"

def highest_mountains():
    return ("1. Гора Еверест - 8848 м\n"
            "2. К2 - 8611 м\n"
            "3. Канченджанга - 8586 м\n"
            "4. Лхотсе - 8516 м\n"
            "5. Макалу - 8462 м\n")

def countries_with_most_borders():
    return "Китай та Росія"

def largest_desert_after_sahara():
    return "Австралійська пустеля"

def random_prediction():
    predictions = [
        "Пес патрон стане головним селебріті в Україні.",
        "Жабка в кабінеті Буданова перетвориться на принца, який вб’є путіна стрілою.",
        "Ватикан не перестане говорити “постраждалих” “хороших” “рузкіх”.",
    ]
    return random.choice(predictions)


def favorite_dog_tea():
    print("Який ви чай виходячи з вашої улюбленої породи собак:")
    print("1. лабрадор")
    print("2. пудель")
    print("3. такса")
    print("4. який собака? я люблю котів!")

    user_choice = input("Введіть номер вашої відповіді: ")

    if user_choice == '1':
        return "Ромашковий чай"
    elif user_choice == '2':
        return "Фруктовий чай"
    elif user_choice == '3':
        return "Чай з трьома ложечками цукру"
    elif user_choice == '4':
        return "Пожований чай"
    else:
        return "Неправильне значення. Будь ласка, спробуйте ще раз."


def region_test():
    print("Тест на визначення регіону проживання. Як ви називаєте оцю штуку з якої роблять деруни?")
    print("1. бульба")
    print("2. крумпля")
    print("3. бараболя")
    print("4. картошка")
    print("5. Solanum tuberosum")

    user_choice = input("Введіть номер вашої відповіді: ")

    if user_choice == '1':
        return "Львівщина або Волинь"
    elif user_choice == '2':
        return "Закарпаття"
    elif user_choice == '3':
        return "Тернопільщина або Хмельниччина або Віниччина"
    elif user_choice == '4':
        return "Центральна частина України"
    elif user_choice == '5':
        return "Біофак"
    else:
        return "Неправильне значення. Будь ласка, спробуйте ще раз."


def useless_facts():
    facts = [
        "Око страуса більше, ніж його мозок.",
        "Майкл Джоpдан одержав від Nіke більше грошей, ніж всі працівники на фабpиках цієї фіpми в Малайзії.",
        "Якщо кричати на склянку води протягом 80 років, то можна її скип’ятити.",
        "Насправді, ППО- це Порошенко Петро Олексійович, наш сивочолий гетьман!",
    ]

    return random.choice(facts)


def rate_chat_bot():
    print("Оцініть чат-бот:")
    print("1. прекрасний")
    print("2. норм")
    print("3. я рахую, шо він не прекрасний")

    user_choice = input("Введіть номер вашої відповіді: ")

    if user_choice == '1':
        return "Ну звісно!"
    elif user_choice == '2':
        return "Не норм, а прекрасний!"
    elif user_choice == '3':
        return "Перерахуй!"
    else:
        return "Неправильне значення. Будь ласка, спробуйте ще раз."


def distance_between_two_points():
    x1 = float(input("Введіть координату x першої точки: "))
    y1 = float(input("Введіть координату y першої точки: "))
    x2 = float(input("Введіть координату x другої точки: "))
    y2 = float(input("Введіть координату y другої точки: "))

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return f"Відстань між двома точками: {distance:.2f}"


def pythagorean_theorem():
    a = float(input("Введіть довжину першої сторони: "))
    b = float(input("Введіть довжину другої сторони: "))
    c = float(input("Введіть довжину третьої сторони: "))
    sides = [a, b, c]

    sides.sort()
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return "Трикутник є прямокутним."
    else:
        return "Трикутник не є прямокутним."


categories = {
    "Фізика": {
        "Закон всесвітнього тяжіння Ньютона": newtons_law_of_universal_gravitation,
        "Закон Стефана-Больцмана": stefan_boltzmann_law,
        "Стала Планка": planck_constant,
    },
    "Філологія": {
        "Яка різниця між Present Simple та Present Continuous?": difference_between_tenses,
        "Яка різниця між іменником та прикметником?": difference_between_noun_and_adjective,
        "Як утворюються дієслова в давальному відмінку?": dative_verb_formation,
    },
    "Астрономія": {
        "Яка є відстань між Землею та Сонцем?": distance_between_earth_and_sun,
        "Що таке астероїди та комети?": asteroids_and_comets,
    },
    "Загальні": {
        "Яка зараз пора року?": current_season,
        "Заспівати колядку": sing_carols,
        "Який зараз місяць?": current_month,
        "Сказати надихаючу цитату": inspiring_quotes,
    },
    "Географія": {
        "Найвищі гори світу": highest_mountains,
        "Країни з найбільшою кількістю кордонів": countries_with_most_borders,
        "Друга за розмірами пустеля після Сахари": largest_desert_after_sahara,
    },
    "Математика": {
        "Теорема Піфагора": pythagorean_theorem,
        "Відстань між двома точками (2D)": distance_between_two_points,
        "Довжина дуги кола": length_of_circle_arc,
        "Площа трапеції": trapezoid_area,
        "Синус і косинус кута": sine_and_cosine,
    },
    "Питання від студента": {
        "Передбачення від чат бота ": random_prediction,
        "Який ви чай виходячи з вашої улюбленої породи собак": favorite_dog_tea,
        "Тест на визначення регіону проживання. Як ви називаєте оцю штуку з якої роблять деруни?": region_test,
        "Нікому непотрібні факти": useless_facts,
        "Оцініть чат бот": rate_chat_bot,
    },

}
def save_chat_history(chat_history):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"dialog-{formatted_time}.txt"

    with open(file_name, "w", encoding="utf-8") as file:
        for line in chat_history:
            file.write(line + "\n")

def display_categories(categories):
    print("Категорії питань:")
    for index, category in enumerate(categories.keys(), 1):
        print(f"{index}. {category}")

def display_questions(category):
    questions = categories.get(category)
    if questions:
        for index, question in enumerate(questions.keys(), 1):
            print(f"{index}. {question}")
        return True
    else:
        print("Такої категорії не існує.")
        return False

class ConsoleColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    print(f"{ConsoleColors.OKGREEN}Вітаємо в нашому чат-боті! Для того, щоб завершити роботу, введіть 'вихід'.{ConsoleColors.ENDC}")

    chat_history = []

    while True:
        print("Виберіть категорію запитань:")
        for i, category in enumerate(categories.keys(), start=1):
            print(f"{i}. {category}")

        user_input = input("Введіть номер категорії або 'вихід' для завершення: ").lower()
        chat_history.append("Користувач: " + user_input)

        print(f"{ConsoleColors.OKCYAN}{user_input}{ConsoleColors.ENDC}")  # Вивід користувача синім кольором

        if user_input == "вихід":
            save_chat_history(chat_history)
            break

        if user_input.isdigit() and 1 <= int(user_input) <= len(categories.keys()):
            category = list(categories.keys())[int(user_input) - 1]
            questions = list(categories[category].keys())
            while True:
                print(f"\n{category}:")
                for i, question in enumerate(questions, start=1):
                    print(f"{i}. {question}")

                user_input = input("Введіть номер питання, 'назад' для повернення в головне меню або 'вихід' для завершення: ").lower()
                chat_history.append("Користувач: " + user_input)

                print(f"{ConsoleColors.OKCYAN}{user_input}{ConsoleColors.ENDC}")  # Вивід користувача синім кольором

                if user_input == "вихід":
                    save_chat_history(chat_history)
                    return
                if user_input == "назад":
                    break

                if user_input.isdigit() and 1 <= int(user_input) <= len(questions):
                    answer = categories[category][questions[int(user_input) - 1]]
                    response = answer()
                    
                    if isinstance(response, tuple):
                        quote = random.choice(response)
                        chat_history.append("Чат-бот: " + str(quote))
                        response = quote

                    else:
                        chat_history.append("Чат-бот: " + str(response))

                    print(f"{ConsoleColors.OKGREEN}{response}{ConsoleColors.ENDC}")  # Вивід відповіді бота зеленим кольором

                else:
                    print("Некоректний ввод. Спробуйте ще раз.")
        else:
            print("Некоректний ввод. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
