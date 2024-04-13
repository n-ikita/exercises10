from solution import NavalBattle

player1 = NavalBattle('#')
NavalBattle.new_game()
for y in range(1, 11):
    for x in range(1, 11):
        player1.shot(x, y)


NavalBattle.show()

