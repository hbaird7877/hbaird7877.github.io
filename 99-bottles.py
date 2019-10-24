
def ninety_nine_bottles(num):
    counter = num
    bottles = num - 1
    while (counter > 0):
        if (bottles == 1):
            print("{} bottles of beer on the wall, {} bottles of beer. \nTake one down and pass it around, {} bottle of beer on the wall.".format(counter, counter, bottles))
        elif (counter == 1):
            print("{} bottle of beer on the wall, {} bottle of beer. \nTake one down and pass it around, no more bottles of beer on the wall. \nNo more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, 99 bottles of beer on the wall.".format(counter, counter))
        else:
            print("{} bottles of beer on the wall, {} bottles of beer. \nTake one down and pass it around, {} bottles of beer on the wall.".format(counter, counter, bottles))
        counter = counter - 1
        bottles = bottles - 1
          
ninety_nine_bottles(99)
