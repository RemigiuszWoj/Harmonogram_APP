import random

FIRST_NAMES = ["Adam", "Julia", "Damian", "Wieslaw", "Joanna", "Kaziemierz", "Wiktor", "Tomasz", "Jagoda",
         "Anna", "Aleksandra", "Mateusz", "Maciej", "Bartosz", "Celina", "Boguslaw", "Jedrzej",
         "Rafal", "Przemyslaw", "Dariusz", "Mariusz", "Bogdan", "Piotr", "Pawel", "Kamil",
         "Magdalena", "Cecylia", "Janusz", "Hubert", "Aleksander"]

LAST_NAMES = ["Nowak", "Galazka", "Wisnia", "Wojcik", "Kowalczyk", "Kamien", "Lawenda", "Ziolo",
            "Nowiczok", "Palec", "Dab", "Koziol", "Janczak", "Wierzba", "Kwiatek", "Wojcieszak",
            "Krawiec", "Kaczmarek", "Piotrowicz", "Grabik", "Wlos", "Kowal", "Zajac", "Michalczyk",
            "Trzmiel", "Wieczorek", "Wrobel", "Socha", "Majka", "Olcha"]

ADDRESS = ["Grabiszynska", "Dworcowa", "Szczesliwa", "Krolewiecka", "Kolataja", "Kosciuszki",
           "Wyspianskiego", "Teczowa", "Balonowa", "Lotnicza", "Legnicka", "Krakowska",
           "Boleslawiecka", "Karkonowska", "Wroclawska", "Robotnicza", "Strzegomska", "Szewdzka"]

EMAIL_SUFIX = ["gmail.com", "wp.pl", "onet.pl"]

FUNCTION = ["Welder", "Forklift operator", "Mechanic", "Electrician",
            "Varnisher", "Dark Knight", "Trainee"]

DRYER_MODELS = ["dryer_20_t", "dryer_35_t", "dryer_50_t"]

MATERIALS = ["Steel", "Wheels", "Frame", "Bin", "Engine", "Pipes",
             "Vertical", "Snails", "Control cabinet", "PLC"]

def get_first_name() -> str:
    return random.choice(FIRST_NAMES)

def get_last_name() -> str:
    return random.choice(LAST_NAMES)

def get_address() -> str:
    return random.choice(ADDRESS) + " " + str(random.randint(1,20)) + "/" + str(random.randint(1,20))

def get_telepchone() -> int:
    return str(random.randint(1,9)) + "".join([str(random.randint(0, 9)) for _ in range(8)])

def get_email() -> str:
    return "{}.{}.{}".format(get_first_name().lower(), get_last_name().lower(),
        random.choice(EMAIL_SUFIX))

def get_nip() -> int:
    return str(random.randint(1,9)) + "".join([str(random.randint(0, 9)) for _ in range(9)])

def get_function() -> str:
    return random.choice(FUNCTION)

def get_dryer_model() -> str:
    return random.choice(DRYER_MODELS)

def get_price() -> int:
    return int(str(random.randint(1,2)) + str(random.randint(0,9)) + "".join(["0" for _ in range(3)]))

def get_param_bool_status() -> bool:
    return bool(random.getrandbits(1))

def get_item_quantity() -> int:
    return int(random.randint(0,9))

def get_item_price() -> int:
    return int(str(random.randint(1,2)) + str(random.randint(0,9)) + "".join(["0" for _ in range(2)]))

def get_deliwery_time() -> int:
    return int( "".join([str(random.randint(0,5)) for _ in range(2)]))

def get_item_name(id) -> str:
    return MATERIALS[id - 1]