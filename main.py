import Statistics_in_PDF
import Table_sorting

if __name__ == '__main__':
    is_correct_input = False
    while not is_correct_input:
        user_input = input("Для вывода табличных данных введите - 'Вакансии'.\n"
                           "Для формирования графиков и отчёта - 'Статистика'.\n")
        if user_input == "Вакансии":
            Table_sorting.main()
            is_correct_input = True
        elif user_input == "Статистика":
            Statistics_in_PDF.main()
            is_correct_input = True
        else:
            print("Введите корректное значение.")
