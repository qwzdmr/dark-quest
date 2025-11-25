import random
import time
# ≪≫ ★ ┌・ ├・ └・ ✟ ═╬╬═

item_list = [
    "Корень Можжевельника", "Валериана Лекарственная", "Таинственная Коробка", "Рыцарский Меч"
]
item_description = [
    "Слегка горьковато-сладкое с выраженными хвойными нотами растение. Обладает лечебными свойствами. [+15 HP]",
    "Не особо приятная на вкус жидкость. Одна вашему ментальному здоровью она явно поможет. [+25 Enegry]",
    "Поговаривают, что если её открыть, то можно обрести временное спокойствие... [PAUSE game]",
    "Меч, которым когда-то вы пользовались на полях битвы. Теперь - это шанс на выживание. [+10 Damage]"
]
item_use_actions = [
    "Выжать сок из корня можжевельника себе в рот.",
    "Сжевать лист Валерианы.",
    "Открыть коробку.",
    "Использовать меч на постоянной основе."
]

menu_icon = [
    "    __  __________   ____  __",
    "   /  |/  / ____/ | / / / / /",
    "  / /|_/ / __/ /  |/ / / / / ",
    " / /  / / /___/ /|  / /_/ /  ",
    "/_/  /_/_____/_/ |_/\____/   "
]

prologue_lyrics = [
    "≪Г≫ Вы - странствующий мечник. Во время последнего столкновения с гоблинами вы потеряли сознание от удара тупым предметом по затылку.",
    "Непонятным для вас образом вы оказались в странном лабиринте...",
    "≪Осмотревшись вокруг вы увидели, что стены лабиринта сделаны не из бетона, дерева или прочих привычных для подобных дел материалов.",
    "Это какое-то странное растение. Нечто похожее на лозу.≫",
    '"Действительно, лоза... Но почему она такая твёрдая?" - ≪сказал Р, притрагиваясь к одному из ответвлений лоз≫',
    "≪вся стена зашуршала≫",
    '"Что это такое?" - ≪удивлённо воскликнул Р≫',
    "≪одна из лоз обвивает вас вокруг шеи≫",
    "≪в порыве паники вы начинаете дёргаться, лоза всё сильнее сковывает шею и затрудняет дыхание≫",
    "≪Г≫ Не уж-то ты так быстро собрался помирать, мечник?",
    "≪Г, тяжело вздыхая≫ Что-ж, давать прямые ответы я права не имею, но...",
    '"Да заткнись ты! Только мешаешь!" - ≪сказали вы использовав последний воздух в ваших лёгких≫',
    "≪Г≫ Как грубо... Я не договорил. Я ведь могу давать подсказки.",
    "≪Вы всхрапнули пытаясь было ответить ему, но воздуха в ваших лёгких уже нет...≫",
    '"Сопротивление убивает." - ≪Смиренно произнёс Г≫',
    '"Для тебя, мечника что давал отпор стольким, скольких не сосчитать, будет трудно понять, что такое смирение." - ≪Буд-то насмехаясь продолжил Г≫',
    "≪У вас почти не осталось сил≫",
    "≪Прокручивая в голове его слова вы поняли, что стоит перестать бороться, но как же? Я ведь мечник! Я был рождён для битв и сражений!",
    "Неужели мне придется так легко принять свою учесть? Да ни за что!≫",
    "≪Лоза притянула вас ближе к стене, буд-то она хочет вас засосать в свои стены. Вы наступили на какой-то предмет≫",
    "≪Опустив глаза на ноги вы увидели старый, ржавый, но всё еще заточенный нож≫",
    "≪Из последних сил вы подняли этот нож и порезали лозу≫",
    '"Что это чёрт возьми за место?" - ≪сказали вы, параллельно жадно набирая воздух в свои лёгкие≫',
    "≪Г≫ Я ведь сказал, я не имею права отвечать на вопросы.",
    '"Но ведь ты можешь давать подсказки , ведь так? Расскажи мне об этом месте настолько ясно, насколько это возможно." - ≪со злобой произнесли вы, немного сдержав свою гордость≫',
    "≪Г≫ Хорошо, я постараюсь...",
    "С чего бы начать? О, ну для начала, та лоза, что пыталась тебя убить - зовётся дьявольские силки. Сопротивление в этом месте = смерть, помни об этом.",
    "Однако смерть может тебя настигнуть не только благодаря этим странным растениям.",
    '"Что? Я могу помереть не только от этих дьявольских сосунков?" - ≪раздражённо произнесли вы≫',
    "≪Г≫ Силков. И да, ты можешь помереть не только от них.",
    '"Да что чёрт возьми может быть опаснее чертовых растений, которые норовят тебя убить!" - ≪размышляли вы в голове≫',
    "≪Г≫ О, ну предположим... Орки, гоблины, змеи?",
    '"Чего? Как ты услышал мои мысли?" - ≪удивлённо вскрикнули вы≫',
    "≪Г≫ Тебе, мечник, я смотрю совсем в той стычке голову отбили. Я ведь в твоей голове. Я слышу и вижу всё, что видишь ты. Знаю о чем ты думаешь и что с тобой происходит.",
    '"Ясно..." - ≪вы всё также шокированы, но не подаёте виду≫',
    '"Пожалуй, хватит страшилок. Где мой меч?" - ≪произнесли вы≫',
    "≪Г≫ Где-то в этом лабиринте. Надо постараться, чтоб его отыскать.",
]

first_stage_lirycs = [
    # Left Side
    "≪ Вы повернули налево и...",
    "уткнулись в тупик! ≫",
    "≪Р≫ Видимо придётся выбрать другой вариант.",
    "≪Г≫ Постой. Даже если ты встречаешь тупик - осмотрись, вдруг найдёшь что-то полезное.",
    '"Не неси чушь, что я мо..." - ≪Присмотревшись вы замечаете еле заметный блеск, вызванный светом от луны≫',
    "≪ Подойдя ближе вы находите... ≫",
    # Front Side
    "≪ Вы решили пойти прямо. Пред собой вы узрели блестящий меч. Вы подходите и поднимаете его. ≫",
    "≪ Вы присматриваетесь и понимаете, что это ваш меч, которым вы когда-то громили врагов. ≫",
    '"Говоришь, будет трудно его отыскать?" - ≪Усмехнувшись сказали вы≫',
    "≪Г≫ Действительно, меч найти было не трудно. Однако я рекомендую тебе обернуться.",
    # Right Side
    "≪ Вы решили повернуть направо ≫",
    "≪ Странный ветер дует вам в лицо ≫",
    "≪ Подняв взор вы увидели перед собой ещё три ответвления ≫",
    "≪Р≫ Да сколько еще будет этих проходов?",
    "≪Г≫ Нууу... 3 таких ответвления на каждом из 3-ёх этапов лабиринта.",
    "≪Р≫ Я в шоке..."
]

second_stage_lyrics = [
    #Left Side
    "≪ Вы повернули налево и... ≫",
    "≪ ОПЯТЬ ОНИ! ≫",
    # Front Side
    "≪ Вы прошли прямо и... ≫",
    "≪ нашли продолжение! ≫",
    "≪ Пред вами снова три ответвления.≫",
    # Right Side
    "≪ Вы повернули направо... ≫",
    "≪ и провалились в странную яму ≫",
    "≪ Вы подвернули ногу, а пока выбирались из нёё потратили немного сил. ≫",
    " [-15 HP, -15 ENRG] ",
]

third_stage_lyrics = [
    # Left Side
    "≪ Вы повернули налево и... ≫",
    "≪ прошли в какую то пустую комнату.≫",
    # Front Side
    "≪ Вы долго идёте прямо и уже думаете сдаться, но в какой-то момент замечаете свет в конце ≫",
    "≪ Наконец-вы доходите до конца. ≫",
    "≪ В лицо светит солнце и дует ветер, вы - сободны.≫",
    "",
    "═╬ НЕЙТРАЛЬНАЯ КОНЦОВКА ╬═",
    # Right Side
    "≪ Вы поворачиваете направо и... ≫",
    "≪ там тупик. Однако вы нашли... ≫"
]

between_stages_action_variable = [
    "═╬ Чего желаете? ╬═",
    "┌・1 Пройти дальше.",
    "├・2 Глянуть свой инвентарь.",
    "├・3 Посмотреть свои Характеристики.",
    "└・4 Выпить яд [СДАТЬСЯ]"
]

continue_way_action_variable = [
    "═╬ Выберите направление! ╬═",
    "┌・0 Вернуться к выбору действий.",
    "├・1 Пройти налево.",
    "├・2 Пройти прямо.",
    "└・3 Пройти направо."
]

fight_action_variable = [
    "═╬ Выберите действие! ╬═",
    "┌・0 Сбежать от сражения! [-50 HP INSTANTLY]",
    "├・1 Нанести удар.",
    "└・2 Глянуть свой инвентарь."
]

dialogue_lirycs = [
    '"Кажется я уже близок к выходу... - ≪запыхаясь произносите вы≫',
    'А они боятся света - ≪произнёс маленький мальчик, сидящий на замшелом камне≫',
    '≪ Вы вздрогнули и приподняли меч≫',
    '"Ты?! Как ты здесь оказался, дитя? Это место смерти!" - ≪произнесли вы≫',
    '"Я живу здесь. А ты заблудился. Я видел." - ≪спокойно произнёс мальчик≫',
    '"Видел? Этих... тварей?" - ≪произносите вы≫',
    '"Они просто слушают. Ты был слишком громким. И страшным." - ≪так-же спокойно продолжил мальчик≫',
    '"Дай руку. Я знаю тихую тропу." - ≪протягивая свою маленькую ручку сказал мальчик≫'
]

first_ending_YB = [
    "≪Г≫ Не стоит этого делать...",
    '"Да плевать, с меня хватит этих испытаний" - ≪сказали вы протягивая руку мальчику≫',
    "≪ Вы получвствовали резкую прохладу, в глазах буд-то попал луч света. ≫",
    "≪ Вы очнулись. ≫",
    "≪ Вокруг вас тела товарищей, мимо пробегает лошадь с наездником. ≫",
    "≪ Вдруг она резко останавливается и нарпавляется в вашу стторону... ≫",
    "≪ Наездник слез с лошади и подошёл в упор к вам ≫",
    "≪ Вы держите зрительный контакт. ≫",
    "≪ Вдруг этот воин издал громкий свист. ≫",
    "≪ Из далека возникает ещё три лошади, а на них - наездники. ≫",
    "≪ Они остановились возле вас, слезли с лошадей и сняли шлемы. ≫",
    "≪ Вы их узнали... Это ваши братья. Теперь вы в безопасности.≫",
    "",
    "═╬ СЧАСТЛИВАЯ КОНЦОВКА ╬═"
]

second_ending_NB = [
    '*Как-то это подозрительно, маленький мальчик, живущий в этом лабиринте?!* - ≪размышляли вы≫',
    "≪Г≫ Соглашусь, может не стоит?",
    '"Прости малыш, но я не могу. Т... таков этикет рыцаря, понимаешь?" - ≪пытаясь солгать произнесли вы≫',
    '"Естественно, понимаю." - ≪произнёс мальчик≫',
    '"Что-ж, тогда я пойду? В интересном же ты месте живёшь..." - ≪сказали вы≫',
    '"Ага! Все обитатели этого места - мои друзья" - ≪с улыбкой произнёс мальчик≫',
    '"Оу... Что-ж, мне пора" - ≪уже начиная удаляться произнесли вы≫',
    "≪ Вам резко поплохело ≫",
    "≪ Вы чувствуете, будто силы покидают вас. ≫",
    "≪ Повернувшись на мальчика - вы видите, как его лицо становится... ≫",
    "≪ нечеловеческим, глаза наполняются пустотой, а рот исчезает...≫",
    "≪ Так вы и погибаете... Не познав чувства освобождения от лабиринта. ≫",
    "",
    "═╬ ПЛОХАЯ КОНЦОВКА ╬═"
]

# STATS
max_health = 100
max_energy = 100
energy = 100
health = 100
damage = 5
swings = 0
in_fight = False

# PLAYER INFO
inventory = []
currently_wearing = "НИЧЕГО"
is_sword_equipped = False
current_stage = 0

# INFO ABOUT STAGES
complited_sides_first_stage = []
complited_sides_second_stage = []
complited_sides_third_stage = []

# mob_indificator = "MOB NAME", MOB HEALTH, MOB DAMAGE
mob_name_list = ["✟ ГОБЛИН ✟", "✟ ОРК ✟", "✟ ЗМЕЯ ✟"]
mob_hp_list = [25, 40, 20]
mob_damage_list = [10, 20, 7]
min_mob_hp = 0
all_mob_health = 0
all_mob_damage = 0
mob_name = ""

def menu():
    print("\n \n \n")
    for i in menu_icon:
        print(i)
    print("""═╬ Приветствую! Желаете сыграть в наш квест ✟ ТЁМНЫЙ ЛАБИРИНТ ✟? ╬═
          ┌・1 Естетвенно!
          └・2 Нет-уж!""")
    want_to_play = str(input("★ Сделайте верный выбор: "))
    want_to_play.lower()
    if want_to_play == "1":
        print("\nХорошо, запомните:\n ≪Р≫ - Рыцарь (вы)\n ≪Г≫ - Голос в голове.")
        time.sleep(1)
        prologue()
    elif want_to_play == "2":
        print("Bye bye!")
        pass
    else:
        print("\n \n \n \n ??? \n \n \n \n")
        return(menu())

def prologue():
    print("\n \n \n")
    cooldown = 0.7
    for i in range (0,5):
        print(prologue_lyrics[i])
        time.sleep(cooldown)
    continue_scene = str(input("\n ★ Нажмите ENTER что-бы продолжить\n"))
    for i in range (5, 14):
        print(prologue_lyrics[i])
        time.sleep(cooldown)
    continue_scene = str(input("\n ★ Нажмите ENTER что-бы продолжить\n"))
    for i in range (14, 19):
        print(prologue_lyrics[i])
        time.sleep(cooldown)
    continue_scene = str(input("\n ★ Нажмите ENTER что-бы продолжить\n"))
    for i in range (19, 27):
        print(prologue_lyrics[i])
        time.sleep(cooldown)
    continue_scene = str(input("\n ★ Нажмите ENTER что-бы продолжить\n"))
    for i in range (27, 37):
        print(prologue_lyrics[i])
        time.sleep(cooldown)
    continue_scene = str(input("\n ★ Нажмите ENTER что-бы продолжить\n"))
    first_stage()

def first_stage():
    global current_stage
    current_stage = 1
    print("\n \n \n")
    choose_variable()

def choose_variable():
    print("\n \n \n")
    for i in between_stages_action_variable:
        print(i)
    action = str(input(" ★ Ваш выбор: "))
    match action:
        case "1":
            choose_continue_way()
        case "2":
            inventory_open()
        case "3":
            stats()
        case "4":
            print("≪Слишком устав от испытаний, которые пришлось пережить в данном месте, вы")
            time.sleep(0.7)
            print("достали из кармана бутылёк с ядом и залпом выпили его. Ваша гибель")
            time.sleep(0.7)
            print("оказалась мучительней, чем испытания.≫")
            time.sleep(0.7)
            print("✟ ВЫ ПРОИГРАЛИ ✟")
            continue_scene = str(input("\n ★ Нажмите ENTER что-бы закрыть игру\n"))
            pass
        case _:
            print("\n \n \n✟ Такого варианта нет!")
            return(choose_variable())
  
def choose_continue_way():
    global current_stage, health, energy
    print("\n \n \n")
    item_id = 0
    for i in continue_way_action_variable:
        print(i)
    action = str(input(" ★ Ваш выбор: "))
    match action:
        case "0":
            choose_variable()
        case "1":
            if current_stage == 1 and not "I WERE ON LEFT SIDE" in complited_sides_first_stage:
                for i in range (0, 5):
                    print(first_stage_lirycs[i])
                    time.sleep(0.7)
                continue_game = str(input("\n ★ Нажмите ENTER что-бы поднять предмет\n"))
                add_item_to_inventory()
                complited_sides_first_stage.append("I WERE ON LEFT SIDE")
                return(choose_continue_way())
            elif current_stage == 1 and "I WERE ON LEFT SIDE" in complited_sides_first_stage:
                print("\n \n \n≪ Я ведь там уже был, зачем мне туда идти? ≫")
                return(choose_continue_way())
            
            if current_stage == 2 and not "I WERE ON LEFT SIDE" in complited_sides_second_stage:
                for i in range (0, 2):
                    print(second_stage_lyrics[i])
                    time.sleep(0.7)
                complited_sides_second_stage.append("I WERE ON LEFT SIDE")
                mob_spawn()
                add_item_to_inventory()
                return(choose_continue_way())
            elif current_stage == 2 and "I WERE ON LEFT SIDE" in complited_sides_second_stage:
                print("\n \n \n≪ Я ведь там уже был, зачем мне туда идти? ≫")
                return(choose_continue_way())
            
            if current_stage == 3 and not "I WERE ON LEFT SIDE" in complited_sides_third_stage:
                for i in range (0, 2):
                    print(third_stage_lyrics[i])
                    time.sleep(0.7)
                dialogue_with_boy()

        case "2":
            if current_stage == 1 and not "I WERE ON FRONT SIDE" in complited_sides_first_stage:
                for i in range (6, 10):
                    print(first_stage_lirycs[i])
                    time.sleep(0.7)
                continue_game = str(input("\n ★ Нажмите ENTER что-бы поднять меч\n"))
                inventory.append(item_list[3])
                print(f'≪ В инвентарь добавлен предмет "{item_list[3]}"! ≫')
                print("≪ Подняв его вы развернулись и увидели перед собой...")
                complited_sides_first_stage.append("I WERE ON FRONT SIDE")
                count = random.randint(1,2)
                print("✟ ОБЯЗАТЕЛЬНО ЭКИПИРУЙТЕ МЕЧ В ИНВЕНТАРЕ ПЕРЕД АТАКОЙ! ✟")
                time.sleep(0.7)
                mob_spawn()
                return(choose_continue_way())
            elif current_stage == 1 and "I WERE ON FRONT SIDE" in complited_sides_first_stage:
                print("\n \n \n≪ Я ведь там уже был, зачем мне туда идти? ≫")
                return(choose_continue_way())
            
            if current_stage == 2 and not "I WERE ON FRONT SIDE" in complited_sides_second_stage:
                for i in range (2, 5):
                    print(second_stage_lyrics[i])
                    time.sleep(0.7)
                current_stage = 3
                return(choose_continue_way())
            
            if current_stage == 3 and not "I WERE ON FRONT SIDE" in complited_sides_third_stage:
                for i in range(2, 6):
                    print(third_stage_lyrics[i])
                    time.sleep(0.7)
                continue_scene = str(input("\n ★ Нажмите ENTER что-бы закрыть игру\n"))
                pass

        case "3":
            if current_stage == 1 and not "I WERE ON RIGHT SIDE" in complited_sides_first_stage:
                current_stage = 2
                for i in range(10, 16):
                    print(first_stage_lirycs[i])
                    time.sleep(0.7)
                complited_sides_first_stage.append("I WERE ON RIGHT SIDE")
                return(choose_continue_way())
            
            if current_stage == 2 and not "I WERE ON RIGHT SIDE" in complited_sides_second_stage:
                for i in range(5, 9):
                    print(second_stage_lyrics[i])
                health -= 15
                energy -= 15
                complited_sides_second_stage.append("I WERE ON RIGHT SIDE")
                return(choose_continue_way())
            elif current_stage == 2 and "I WERE ON RIGHT SIDE" in complited_sides_second_stage:
                print("\n \n \n≪ Я ведь там уже был, зачем мне туда идти? ≫")
                return(choose_continue_way())
            if current_stage == 3 and not "I WERE ON RIGHT SIDE" in complited_sides_third_stage:
                for i in range(7, 9):
                    print(third_stage_lyrics[i])
                    time.sleep(0.7)
                return(choose_continue_way())

        case _:
            print("\n \n \n✟ Такого варианта нет!")
            return(choose_continue_way())         

def inventory_open():
    global inventory, health, energy, damage, is_sword_equipped
    print("\n \n \n")
    inventory_actions = []
    print("═╬ СОДЕРЖИМОЕ ИНВЕНТАРЯ ╬═")
    for i in inventory:
        if len(inventory) >= 0: print(f"✟ {i} ✟")
        else: print("Инвентарь пуст!")
    print("═╬ ДЕЙСТВИЯ С ПРЕДМЕТАМИ ╬═")
    print("0・Вернуться к действиям.")
    for i in inventory:
        if item_list[0] in i:
            inventory_actions.append("1・" + item_use_actions[0])
        if item_list[1] in i:
            inventory_actions.append("2・" + item_use_actions[1])
        if item_list[2] in i:
            inventory_actions.append("3・" + item_use_actions[2])
        if is_sword_equipped == False and item_list[3] in i:
            inventory_actions.append("4・" + item_use_actions[3])
    for i in inventory_actions:
        print(i)
    action = str(input(" ★ Ваш выбор: "))
    match action:
        case "0":
            if in_fight == False:
                choose_variable()
            else:
                player_attack_chose()
        case "1":
            inventory.remove(item_list[0])
            print("≪ Вы выжали сок можжевельника! [+15 HP] ≫")
            if health == max_health:
                health = 100
            elif max_health > 85:
                need_health = max_health - health
                health += need_health
            else:
                health += 15
            return(inventory_open())
        case "2":
            inventory.remove(item_list[1])
            print("≪ Вы сжевали лист Валерианы! [+ 25 ENERGY] ≫")
            if energy == max_energy:
                energy = 100
            elif max_energy > 75:
                need_energy = max_energy - energy
                energy += need_energy
            else:
                energy += 15
            return(inventory_open())
        case "3":
            inventory.remove(item_list[2])
            print("≪ Вы открыли Таинственную коробку и...")
            print("вокруг вас возвелись стены, за вами возник диван")
            print("вы присели на диван. ≫")
            continue_game = str(input("\n ★ Нажмите ENTER что-бы продолжить игру\n"))
            return(inventory_open())
        case "4":
            if is_sword_equipped == False:
                inventory.remove(item_list[3])
                print("≪ Вы экипировали меч! [+10 DMG] ≫")
                damage += 10
                is_sword_equipped = True
                return(inventory_open())
            else:
                print("✟ Меч уже в руке!")
                return(inventory_open())
        case _:
            print("✟ Такого варианта нет!")
            return(inventory_open())

def add_item_to_inventory():
    global inventory
    item_id = random.randint(0, 2)
    inventory.append(item_list[item_id])
    print(f'≪ В инвентарь добавлен предмет "{item_list[item_id]}"! ≫')
    print("≪ Подняв предмет вы развернулись, куда пойти теперь? ≫")

def dialogue_with_boy():
    for i in dialogue_lirycs:
        print(i)
        time.sleep(0.7)
    action = str(input("═╬ Выберите действие! ╬═\n┌・1 Довериться мальчику.\n└・2 Не давать руку."))
    match action:
        case "1":
            for i in first_ending_YB:
                print(i)
                time.sleep(0.7)
            continue_scene = str(input("\n ★ Нажмите ENTER что-бы закрыть игру\n"))
            pass
        case "2":
            for i in second_ending_NB:
                print(i)
                time.sleep(0.7)
            continue_scene = str(input("\n ★ Нажмите ENTER что-бы закрыть игру\n"))
            pass
        case _:
            print("\n \n \n✟ Такого варианта нет!")
            return(dialogue_with_boy())

def stats():
    print("\n \n \n")
    print("═╬ ВАША СТАТИСТИКА ╬═")
    print(f"┌・HP: {health}\n├・Energy: {energy}\n└・DMG: {damage}")
    continue_game = str(input("\n ★ Нажмите ENTER что-бы продолжить игру\n"))
    return(choose_variable())

def mob_spawn():
    global in_fight, all_mob_health, all_mob_damage, mob_name
    # IF I WILL NOT DO THIS TWO TIMES - mob_elements_id = 1.
    count = random.randint(1,2)
    for i in range (0, 1): mob_elements_id = random.randint(0, 2)
    print("\n \n \n")
    mob_name = mob_name_list[mob_elements_id]
    mob_health = mob_hp_list[mob_elements_id]
    mob_damage = mob_damage_list[mob_elements_id]
    all_mob_health = mob_health * count
    all_mob_damage = mob_damage * count
    swings_needed = all_mob_health/damage
    swings_needed = round(swings_needed, 1)
    print(f"┌・{count}x {mob_name}\n├・Урон каждого: {mob_damage}\n└・HP каждого: {mob_health}\n✟ Вам понадобиться {swings_needed} взмахов мечём!")
    in_fight = True
    player_attack_chose()

def player_attack_chose():
    global health, energy, in_fight, all_mob_health, all_mob_damage, mob_name
    print("\n \n")
    for i in fight_action_variable:
        print(i)
    action = str(input(" ★ Ваш выбор: "))
    match action:
        case "0":
            health -= 50
            print('\n \n✟ Какой же из тебя мечник, если ты бежишь как трус?\n"Отвянь" - ≪стиснув зубы ответили вы≫')
            in_fight = False
            choose_continue_way()
        case "1":
            player_attack()
        case "2":
            inventory_open()
        case _:
            print("\n \n \n✟ Такого варианта нет!")
            return(player_attack_chose())      

def player_attack():
    global health, energy, swings, all_mob_health, all_mob_damage, mob_name, in_fight
    print("\n \n \n")
    if all_mob_health > 0:
        if health > 0:
            if energy > 11 and swings != 2:
                if all_mob_health < 14:
                    need_damage = all_mob_health
                    all_mob_health -= need_damage
                    in_fight = False
                    print(f"✟ Вам удалось нанести урон сплешем по врагам!\n ★ У вас: {health}HP, {energy} ENRG\n ★ HP противников (общее): {all_mob_health}")
                    print("✟ Вы уничтожили всех мобов!")
                else:
                    energy -= 10
                    all_mob_health -= damage
                    swings += 1
                    print(f"✟ Вам удалось нанести урон сплешем по врагам!\n ★ У вас: {health}HP, {energy} ENRG\n ★ HP противников (общее): {all_mob_health}")
                    return(player_attack_chose())
            elif energy < 11:
                print("✟ У вас слишком мало сил для атаки!")
                return(player_attack_chose())
            elif swings == 2:
                health -= all_mob_damage
                print(f"✟ Враг нанёс по вам удар!\n ★ У вас: {health} HP, {energy} ENRG\n ★ Вам нанесли -{all_mob_damage} HP!\n ★ HP противников (общее): {all_mob_health}")
                swings = 0
                return(player_attack_chose())
        else:
            print("═╬ Вы слишком сильно истекли кровью и погибли. ╬═")
            print("✟ ВЫ ПРОИГРАЛИ ✟")
            continue_scene = str(input("\n ★ Нажмите ENTER что-бы закрыть игру\n"))
            pass
    else:
        print("✟ Вы уничтожили всех мобов!")
        in_fight = False

menu()
