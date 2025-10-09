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