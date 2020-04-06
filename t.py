import random

class Horde_Maker():
	def __init__(self):
		self.C = 0
		self.B = 50
		self.B1 = 0
		self.B2 = 0
		self.B3 = 0
		self.B4 = 0
		self.range_list = []
		self.H = 0
		self.c_loot = ["Copper Ring", "Polished Silverware", "Dagger", "Sword", "Spear", "Shield"]
		self.c_val = {"Copper Ring": 8, "Polished Silverware": 20, "Dagger": 2, "Sword": 15, "Spear": 1, "Shield": 10, "Simple Amulet": 5}
		self.b_loot = []
		self.b1_loot = []
		self.b2_loot = []
		self.b3_loot = []
		self.b4_loot = []
		
	def gen_bpower(self):
		n = 0
		while n <= 0 or n > 3:
			val = input("Please enter the wage disparity of your setting on a scale of 1-3 (1 is little disparity, 2 is moderate, 3 is extreme): ")
			try:
				n = int(val)
			except ValueError:
				print("Invalid Input. ")
				n = 0

		self.C = self.B/(n*2)
		self.B1 = self.B * (n*2)
		self.B2 = self.B * (n*8)
		self.B3 = self.B * (n*32)
		self.B4 = self.B * (n*256) 
		self.range_list = [self.C, self.C, self.C, self.C, self.B, self.B, self.B, self.B, self.B1, self.B1, self.B1, self.B1, self.B2, self.B2, self.B2, self.B2, self.B3, self.B3, self.B3, self.B3, self.B4]

	def print_bpower(self):
		print(self.C)
		print(self.B)
		print(self.B1)
		print(self.B2)
		print(self.B3)
		print(self.B4)
		
	def gen_gold(self, dif):
		i = dif % 4
		m_tier = self.range_list[dif]
		self.H = int((m_tier *(3.5 * (i + 1.45)) + 65) * random.uniform(0.85, 1.15))
		#print(str(self.H))
	
	def gen_loot(self):
		#m_tier = self.range_list[dif]
		arr_num = len(self.c_loot)		
		loot = self.c_loot[random.randint(0,(arr_num - 1))]
		self.H = self.H - self.c_val[loot]
		return(loot)
	
	def gen_horde(self):
		m = 1
		while m != 0:
			
			try:
				d = input("(Enter 0 to exit)Please enter the difficulty of the dungeon on a scale of 1-20: ")
				dif = int(d)
				
				if m != 0:
					loot_amount = random.randint(1, 4)
					loot_total = ""
					self.gen_gold(dif)
						
					while(loot_amount != 0):
						loot = self.gen_loot()
						loot_total += loot + ", "
						loot_amount = loot_amount - 1
						
						
					print(str(self.H) + " Gold pieces")
					print(loot_total)
					#print(self.c_val[loot])
					
				else:
					print("Thank you for using my Horde Generator Program! ")
					
			except ValueError:
				print("You entered an Invalid Character. Enter an integer between 1-20. ")
				
			except IndexError:
				print("The number you entered was too large. Enter an integer between 1-20. ")

horde1 = Horde_Maker()
horde1.gen_bpower()
horde1.print_bpower()
horde1.gen_horde()
