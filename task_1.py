# '1h 45m,360s,25m,30m 120s,2h 60s'

# Напиши цикл, который посчитает общее количество минут. 
# Результат сохрани в переменную и выведи на экран. 
# Используй в решении методы split(), replace() и оператор in.
# Обрати внимание: временное значение может состоять из одного, двух или трёх единиц времени. 
# Значения расшифровываются так:
# часы — любое положительное целое число и символ h;
# минуты — любое положительное целое число и символ m;
# секунды — положительное целое число кратное 60 и символ s.

sline = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0
parts = sline.split(',')

for s in parts:
    res = s.replace(' ','')
    if 'h' in res:
        h = res.split('h', 1)[0]
        total_minutes += int(h) * 60
        res = res.split('h', 1)[1]
    if 'm' in res:
        m = res.split('m', 1)[0]
        total_minutes += int(m)
        res = res.split('m', 1)[1]
    if 's' in res:
        s = res.split('s', 1)[0]
        total_minutes += int(s) // 60
        res = res.split('s', 1)[1]

print(total_minutes)

