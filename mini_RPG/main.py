import random

print("==============================")
print("       MINI RPG LEGENDS")
print("==============================")
print()
print("1. new game")
print("2. load game")
print("3. exit game")

while True:
    try:
        choice = int(input("Enter your choice: "))

        # NEW GAME
        if choice == 1:
            print("\n===== CREATE PLAYER =====")

            name = input("Name of the player: ")

            print("\nCreate class")
            print("1. Warrior")
            print("2. Wizard")
            print("3. Archer")

            while True:
                try:
                    class_choice = int(input("Enter your class: "))
                    if class_choice == 1:
                        hero_class = "Warrior"
                        max_hp = 120
                        attack = 15
                        break
                    elif class_choice == 2:
                        hero_class = "Wizard"
                        max_hp = 75
                        attack = 25
                        break
                    elif class_choice == 3:
                        hero_class = "Archer"
                        max_hp = 95
                        attack = 20
                        break
                    else:
                        print("invalid class")
                except ValueError:
                    print("invalid choice")

            hp = max_hp
            level = 1
            exp = 0
            exp_needed = 20
            gold = 0
            potions = 3

            print("\n===== PLAYER CREATED =====")
            print("name", name)
            print("class", hero_class)
            print("level", level)
            print("Hp", hp)
            print("attack", attack)
            print("exp", exp)
            print("gold", gold)
            print("potions", potions)

            # PLAYER MENU
            while True:
                print("\n===== PLAYER MENU =====")
                print("1. Player")
                print("2. Inventory")
                print("3. Explore")
                print("4. Save game")
                print("5. Exit")

                menu_choice = int(input("Enter your choice: "))

                # PLAYER
                if menu_choice == 1:
                    print("\n===== PLAYER =====")
                    print("name", name)
                    print("class", hero_class)
                    print("level", level)
                    print("Hp", hp)
                    print("attack", attack)
                    print("exp", exp)
                    print("gold", gold)
                    print("potions", potions)

                # INVENTORY
                elif menu_choice == 2:
                    print("\n===== INVENTORY =====")
                    print("potions", potions)
                    print("gold", gold)

                # EXPLORE
                elif menu_choice == 3:
                    print("===== EXPLORE =====")
                    event = random.randint(1, 2)
                    if event == 1:
                        print("You found gold")
                        gold += 10
                        print("You got 10 gold")
                    elif event == 2:
                        print("You found a monster")
                        monster_type = random.randint(1, 3)
                        if monster_type == 1:
                            monster_name = "Goblin"
                            monster_hp = 30
                            monster_attack = 10
                            monster_gold = 10
                            monster_exp = 10
                        elif monster_type == 2:
                            monster_name = "Orc"
                            monster_hp = 50
                            monster_attack = 15
                            monster_gold = 20
                            monster_exp = 20
                        elif monster_type == 3:
                            monster_name = "Dragon"
                            monster_hp = 80
                            monster_attack = 20
                            monster_gold = 50
                            monster_exp = 40

                        print("Monster:", monster_name)
                        print("Monster HP:", monster_hp)
                        print("Monster Attack:", monster_attack)

                        # BATTLE
                        while True:
                            print("\n1. Attack")
                            print("2. Potion")
                            print("3. Run")

                            battle_choice = int(input("Enter your choice: "))
                            if battle_choice == 1:
                                critical = random.randint(1, 5)
                                if critical == 1:
                                    monster_hp -= attack * 2
                                    print("Critical Hit")
                                    print("Damage", attack * 2)
                                else:
                                    monster_hp -= attack
                                    print("You attacked Monster")
                                    print("Damage", attack)
                                print("monster HP", monster_hp)

                                # MONSTER DEFEATED
                                if monster_hp <= 0:
                                    print("Monster defeated")
                                    gold += monster_gold
                                    print("You got", monster_gold, "gold")
                                    exp += monster_exp
                                    print("You got", monster_exp, "exp")

                                    # LEVEL UP
                                    if exp >= exp_needed:
                                        level += 1
                                        max_hp += 10
                                        hp += 10
                                        attack += 5
                                        exp = 0
                                        exp_needed += 20

                                        print("level up")
                                        print("Your Level", level)

                                    # POTION DROP
                                    item_chance = random.randint(1, 5)
                                    if item_chance == 1:
                                        potions += 1
                                        print("You found a potion")
                                    break

                                # MONSTER ATTACK
                                monster_critical = random.randint(1, 5)
                                if monster_critical == 1:
                                    hp -= monster_attack * 2
                                    print("Monster Critical Hit")
                                    print("Damage", monster_attack * 2)
                                else:
                                    hp -= monster_attack
                                    print("Monster attacked you")
                                    print("Damage", monster_attack)
                                print("Your HP", hp)

                                # PLAYER DIED
                                if hp <= 0:
                                    print("You died")
                                    print("Game Over")
                                    break

                            # POTION
                            elif battle_choice == 2:
                                if potions > 0:
                                    hp += 30
                                    if hp > max_hp:
                                        hp = max_hp
                                    potions -= 1

                                    print("You used a potion")
                                    print("Your HP", hp)
                                    print("Potions", potions)
                                else:
                                    print("You don't have potions")

                            # RUN
                            elif battle_choice == 3:
                                print("You run away")
                                break
                            else:
                                print("Invalid choice")

                # SAVE GAME
                elif menu_choice == 4:
                    file = open("save.txt", "w")

                    file.write(name + "\n")
                    file.write(str(level) + "\n")
                    file.write(str(hp) + "\n")
                    file.write(str(gold) + "\n")
                    file.write(str(potions) + "\n")
                    file.write(str(attack) + "\n")
                    file.write(str(exp) + "\n")
                    file.write(str(exp_needed) + "\n")
                    file.write(str(max_hp) + "\n")
                    file.write(hero_class + "\n")
                    file.close()

                    print("Game saved")

                # EXIT
                elif menu_choice == 5:
                    print("Exit")
                    break
                else:
                    print("Invalid choice")

        # LOAD GAME
        elif choice == 2:

            try:
                print("load game...")
                file = open("save.txt", "r")
                data = file.read()
                file.close()
                data = data.split("\n")
                name = data[0]
                level = int(data[1])
                hp = int(data[2])
                gold = int(data[3])
                potions = int(data[4])
                attack = int(data[5])
                exp = int(data[6])
                exp_needed = int(data[7])
                max_hp = int(data[8])
                hero_class = data[9]

                print("\n===== PLAYER =====")
                print("name", name)
                print("class", hero_class)
                print("level", level)
                print("Hp", hp)
                print("attack", attack)
                print("exp", exp)
                print("gold", gold)
                print("potions", potions)

                print("Game loaded")

                # LOADED GAME MENU
                while True:
                    print("\n===== PLAYER MENU =====")
                    print("1. Player")
                    print("2. Inventory")
                    print("3. Explore")
                    print("4. Save game")
                    print("5. Exit")

                    load_choice = int(input("Enter your choice: "))

                    # PLAYER
                    if load_choice == 1:
                        print("\n===== PLAYER =====")
                        print("name", name)
                        print("class", hero_class)
                        print("level", level)
                        print("Hp", hp)
                        print("attack", attack)
                        print("exp", exp)
                        print("gold", gold)
                        print("potions", potions)

                    # INVENTORY
                    elif load_choice == 2:
                        print("\n===== INVENTORY =====")
                        print("potions", potions)
                        print("gold", gold)

                    # EXPLORE
                    elif load_choice == 3:
                        print("===== EXPLORE =====")
                        event = random.randint(1, 2)
                        if event == 1:
                            print("You found gold")
                            gold += 10
                            print("You got 10 gold")

                        elif event == 2:
                            print("You found a monster")
                            monster_type = random.randint(1, 3)
                            if monster_type == 1:
                                monster_name = "Goblin"
                                monster_hp = 30
                                monster_attack = 10
                                monster_gold = 10
                                monster_exp = 10
                            elif monster_type == 2:
                                monster_name = "Orc"
                                monster_hp = 50
                                monster_attack = 15
                                monster_gold = 20
                                monster_exp = 20
                            elif monster_type == 3:
                                monster_name = "Dragon"
                                monster_hp = 80
                                monster_attack = 20
                                monster_gold = 50
                                monster_exp = 40

                            print("Monster:", monster_name)
                            print("Monster HP:", monster_hp)
                            print("Monster Attack:", monster_attack)

                            # BATTLE
                            while True:
                                print("\n1. Attack")
                                print("2. Potion")
                                print("3. Run")
                                battle_choice = int(input("Enter your choice: "))

                                if battle_choice == 1:
                                    critical = random.randint(1, 5)
                                    if critical == 1:
                                        monster_hp -= attack * 2
                                        print("Critical Hit")
                                        print("Damage", attack * 2)
                                    else:
                                        monster_hp -= attack
                                        print("You attacked Monster")
                                        print("Damage", attack)

                                    print("monster HP", monster_hp)

                                    # MONSTER DEFEATED
                                    if monster_hp <= 0:
                                        print("Monster defeated")
                                        gold += monster_gold
                                        print("You got", monster_gold, "gold")
                                        exp += monster_exp
                                        print("You got", monster_exp, "exp")

                                        # LEVEL UP
                                        if exp >= exp_needed:
                                            level += 1
                                            max_hp += 10
                                            hp += 10
                                            attack += 5
                                            exp = 0
                                            exp_needed += 20
                                            print("level up")
                                            print("Your Level", level)

                                        # POTION DROP
                                        item_chance = random.randint(1, 5)
                                        if item_chance == 1:
                                            potions += 1
                                            print("You found a potion")

                                        break

                                    # MONSTER ATTACK
                                    monster_critical = random.randint(1, 5)
                                    if monster_critical == 1:
                                        hp -= monster_attack * 2
                                        print("Monster Critical Hit")
                                        print("Damage", monster_attack * 2)
                                    else:
                                        hp -= monster_attack
                                        print("Monster attacked you")
                                        print("Damage", monster_attack)

                                    print("Your HP", hp)

                                    # PLAYER DIED
                                    if hp <= 0:
                                        print("You died")
                                        print("Game Over")
                                        break

                                # POTION
                                elif battle_choice == 2:
                                    if potions > 0:
                                        hp += 30
                                        if hp > max_hp:
                                            hp = max_hp
                                        potions -= 1

                                        print("You used a potion")
                                        print("Your HP", hp)
                                        print("Potions", potions)

                                    else:
                                        print("You don't have potions")

                                # RUN
                                elif battle_choice == 3:
                                    print("You run away")
                                    break

                                else:
                                    print("Invalid choice")

                    # SAVE GAME
                    elif load_choice == 4:
                        file = open("save.txt", "w")

                        file.write(name + "\n")
                        file.write(str(level) + "\n")
                        file.write(str(hp) + "\n")
                        file.write(str(gold) + "\n")
                        file.write(str(potions) + "\n")
                        file.write(str(attack) + "\n")
                        file.write(str(exp) + "\n")
                        file.write(str(exp_needed) + "\n")
                        file.write(str(max_hp) + "\n")
                        file.write(hero_class + "\n")

                        file.close()

                        print("Game saved")

                    # EXIT
                    elif load_choice == 5:
                        print("Exit")
                        break

                    else:
                        print("Invalid choice")

            except FileNotFoundError:
                print("Save file not found")
                print("Please create a new game first")

        # EXIT GAME
        elif choice == 3:
            print("exit game, goodbye")
            break

        else:
            print("invalid choice")

    except ValueError:
        print("invalid choice")