from google import genai


client = genai.Client(api_key="AIzaSyAt-lA3DkrV0jhrQmai-odan_fgbwFUmr8")

deformations = ("Перфекционизм в достижениях; воспринимаемый перфекционизм; зависимость от достижений;\n"
                "Зависимость от одобрения; зависимость от любви; страх отвержения;\n"
                "Необходимость угождать другим; страх конфликтов; самообвинение;\n"
                "Обвинение других людей; мне все должны; правота;\n"
                "Безнадёжность; никчёмность\\неполноценность;\n"
                "Эмоциональный перфекционизм; страх гнева; страх эмоций; воспринимаемый нарциссизм; "
                "ошибка лесного пожара; ошибка прожектора; магическое мышление;\n"
                "Низквя устойчивость к фрустрации; комплекс супермена\\супервумен.")


def create_deformation(think: str):
    chat = client.chats.create(model="gemini-2.5-flash-lite")

    promt1 = f"Ты психолог. "\
             f"Выбери из списка подходящие когнитивные искажения к мысли в кавычках и отправь только их."\
             f"\n{deformations}\n"\
             f"\n\"{think}\""

    promt2 = f"Кратко опиши, почему ты сделал такой выбор?"

    response = chat.send_message(promt1)
    deformation = response.text

    response = chat.send_message(promt2)
    description = response.text

    print(f"{deformation}\n\n{description}")

    return {"deformation": deformation, "description": description}


def create_advantage(think: str, advantages: list[list[str]], disadvantages: list[list[str]], advantage_condition: bool):
    chat = client.chats.create(model="gemini-2.5-flash-lite")

    advantages = list_to_string(advantages)
    disadvantages = list_to_string(disadvantages)

    if advantage_condition:
        generated_description = "плюс"
    else:
        generated_description = "минус"

    promt = f"Есть мысль: \"{think}\"\n. " \
             f"У неё есть плюсы{advantages} и минусы{disadvantages}\n" \
             f"Напиши {generated_description}, которого нет в списке, и отправь только его"

    print(promt)

    response = chat.send_message(promt)
    description = response.text

    print(f"{description}")

    return description


def list_to_string(list_of_str: list[list[str]]):
    list_of_str = [string[0] for string in list_of_str]

    if len(list_of_str) > 0:
        return ":\n" + "\n".join(list_of_str) + "\n"
    else:
        return "(пусто)"