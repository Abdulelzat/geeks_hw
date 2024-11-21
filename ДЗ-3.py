class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        result = self.__cpu * self.__memory
        print(f"Вычисления завершены. Результат: {result}")

    def __str__(self):
        return f"Компьютер с CPU: {self.__cpu} и памятью: {self.__memory} ГБ"

    def __eq__(self, other):
        return self.__memory == other.memory

    def __ne__(self, other):
        return self.__memory != other.memory

    def __lt__(self, other):
        return self.__memory < other.memory

    def __le__(self, other):
        return self.__memory <= other.memory

    def __gt__(self, other):
        return self.__memory > other.memory

    def __ge__(self, other):
        return self.__memory >= other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if sim_card_number <= len(self.__sim_cards_list):
            carrier = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {carrier}")
        else:
            print("Неверный номер сим-карты!")

    def __str__(self):
        return f"Телефон с сим-картами: {', '.join(self.__sim_cards_list)}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до локации: {location}")

    def __str__(self):
        return f"Смартфон с CPU: {self.cpu}, памятью: {self.memory} ГБ и сим-картами: {', '.join(self.sim_cards_list)}"


computer = Computer(cpu=3.4, memory=16)
phone = Phone(sim_cards_list=["Beeline", "MTS", "Tele2"])
smartphone1 = SmartPhone(cpu=2.8, memory=8, sim_cards_list=["MTS", "Beeline"])
smartphone2 = SmartPhone(cpu=3.0, memory=12, sim_cards_list=["Megafon", "Beeline"])

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

computer.make_computations()
phone.call(1, "+996 777 99 88 11")
smartphone1.use_gps("Город Алма-Ата")
smartphone2.call(2, "+7 900 123 45 67")

print(f"Компьютер и смартфон1 имеют одинаковую память: {computer == smartphone1}")
print(f"Компьютер и смартфон2 имеют одинаковую память: {computer != smartphone2}")
print(f"Компьютер имеет больше памяти чем смартфон1: {computer > smartphone1}")
print()
