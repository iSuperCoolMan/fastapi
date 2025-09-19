import openai


openai.api_key="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" #задаем переменную токена

deformations = ("Перфекционизм в достижениях; воспринимаемый перфекционизм; зависимость от достижений;\n"
                "Зависимость от одобрения; зависимость от любви; страх отвержения;\n"
                "Необходимость угождать другим; страх конфликтов; самообвинение;\n"
                "Обвинение других людей; мне все должны; правота;\n"
                "Безнадёжность; никчёмность\\неполноценность;\n"
                "Эмоциональный перфекционизм; страх гнева; страх эмоций; воспринимаемый нарциссизм; "
                "ошибка лесного пожара; ошибка прожектора; магическое мышление;\n"
                "Низквя устойчивость к фрустрации; комплекс супермена\\супервумен.")


def create_deformation(think: str):  # создаем ввод текста
    promt1 = f"Ты психолог. "\
             f"Выбери из списка подходящие когнитивные искажения к мысли в кавычках и отправь только их."\
             f"\n{deformations}\n"\
             f"\n\"{think}\""

    promt2 = f"Опиши, почему ты сделал такой выбор?"

    chat1 = openai.chat.completions.create(model="gpt-3.5-turbo", messages=[
        {"role": "user", "content": promt1}
    ])

    deformation = chat1.choices[0].message.content

    chat2 = openai.chat.completions.create(model="gpt-3.5-turbo", messages=[
        {"role": "user", "content": promt1},
        {"role": "assistant", "content": deformation},
        {"role": "user", "content": promt2}
    ])

    description = chat2.choices[0].message.content

    print(f"{deformation}\n\n{description}")

    return {"deformation": deformation, "description": description}