money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
total = 0
budget = money_capital + salary

while spend <= budget:
    ostatok = budget - spend
    budget = ostatok + salary
    spend += spend * increase
    total += 1

print("Количество месяцев, которое можно протянуть без долгов:", total)
