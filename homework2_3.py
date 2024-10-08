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
        return self.__cpu + self.__memory


    def __str__(self):
        return f'Computer: CPU: {self.__cpu}, Memory: {self.__memory}'

    def __lt__(self, other):
        return self.memory < other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __eq__(self, other):
        return self.memory == other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __ge__(self, other):
        return self.memory >= other.memory

    def __ne__(self, other):
        return self.memory != other.memory


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
        if sim_card_number == 1:
            print(f'Идет звонок на номер {call_to_number} с {sim_card_number} - Beeline')
        elif sim_card_number == 2:
            print(f'Идет звонок на номер {call_to_number} с {sim_card_number} - MegaCom')

    def __str__(self):
        return f'Phone: sim_cards_list: {self.sim_cards_list}'


class SmartPhone(Phone, Computer):
    def __init__(self, sim_cards_list, cpu, memory):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)
        self.__sim_cards_list = sim_cards_list
        self.__cpu = cpu
        self.__memory = memory

    def use_gps(self, location):
        print(f'Пройдите прямо 2 км, а затем поверните направо и вы окажетесь в {location}')

    def __str__(self):
        return f'Smartphone: sim_cards_list: {self.__sim_cards_list}, cpu: {self.__cpu}, memory: {self.__memory}'


phone_1 = Phone([1, 2])
computer_1 = Computer(16, 128)
smartphone_1 = SmartPhone([1, 2], 8, 64)
smartphone_2 = SmartPhone([1, 2], 8, 216)
computer_2 = Computer(8, 164)

print(phone_1)
print(computer_1)
print(smartphone_1)
print(smartphone_2)

smartphone_1.use_gps('Geeks')
phone_1.call(1, 770180971)
smartphone_1.call(2, 502497165)
print(computer_1.make_computations())
print(smartphone_1.make_computations())
print(smartphone_2.make_computations())
phone_1.call(2, 502497165)

print(f'Memory of the computer is impotrtant: {computer_1.memory < computer_2.memory}')

