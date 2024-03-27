lake = input("You come across a lake. Do you want to swim across, or wait for a boat? (swim/wait) ")
if lake == "swim":
    print("You get eaten by a hungry shark. Game over.")
elif lake == "wait":
    print("A boat arrives and you arrive at the island safely.")
cave = input("You come to a cave. Do you want to venture inside or walk on? (venture/walk) ")
if cave == "venture":
    print("You are squished by boulders never to be seen again. Game over.")
elif cave == "walk":
    direction = input("Do you go left, right, or straight? (left/right/straight) ")
    if direction == "left":
        print("You are trampled by a herd of wildebeest. Game over.")
    elif direction == "straight":
        print("You get stung by a poisonous wasp. Game over.")
    elif direction == "right":
        print("You march on and find the buried treasure! Yippee!!")