def bottle_song(bottles):
	if bottles == 1 :
		return print(f'{bottles} bottle of beer on the wall, {bottles} bottle of beer take one down pass it around, go to the store buys some more 99 bottles of beer on the wall.')
	else:
		print(f'{bottles} bottles of beer on the wall, {bottles} bottles of beer take one down pass it around, {int(bottles)-1} bottle of beer on the wall')
		return bottle_song(bottles - 1)

bottle_song(99)