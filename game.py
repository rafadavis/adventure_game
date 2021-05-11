from player import Player
import world

def play():
    print("Escape from Cave Terror!")
    player = Player()
    
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        action_input = get_player_command()

        if action_input == 'n':
            player.move_north()

        elif action_input == 's':
            player.move_south()

        elif action_input == 'e':
            player.move_east()

        elif action_input == 'w':
            player.move_west()

        elif action_input == 'i':
            player.print_inventory()

        elif action_input == 'a':
            player.attack()
            
        else:
            print("Invalid action!")

def get_player_command():
    return input('Action: ').lower()

play()
