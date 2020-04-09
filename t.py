import random

class Horde_Maker():
	def __init__(self):
		self.B = 50
		self.range_list = []
		self.H = 0
		
	def gen_bpower(self):
		n = 0
		while n <= 0 or n > 3:
			val = input("Please enter the wage disparity of your setting on a scale of 1-3 (1 is little disparity, 2 is moderate, 3 is extreme): ")
			try:
				n = int(val)
			except ValueError:
				print("Invalid Input. ")
				n = 0
		
		self.c = self.Power(self.B/(n*2), ["Copper Ring", "Polished Silverware", "Dagger", "Sword", "Spear", "Shield"], {"Copper Ring": 8, "Polished Silverware": 20, "Dagger": 2, "Sword": 15, "Spear": 1, "Shield": 10, "Simple Amulet": 5})
		self.b = self.Power(self.B, ["Weak Magic Ring", "Weak Magic Bracer", "Ornate Necklace", "Potion of Healing", "Potion of Slickness"], {"Weak Magic Ring": 40, "Weak Magic Bracer": 35, "Ornate Necklace":75, "Potion of Healing": 50, "Potion of Slickness": 35})
		self.b1 = self.Power(self.B * (n*2), ["Potion of Greater Healing", "Masterwork Weapon", "Drow Poison", "Rare Fang"], {"Potion of Greater Healing": 200, "Masterwork Weapon" : 300, "Drow Poison": 175, "Rare Fang": 100})
		self.b2 = self.Power(self.B * (n*8), ["Potion of Superior Healing", "+1 Weapon"], {"Potion of Superior Healing": 800, "+1 Weapon": 2000})
		self.b3 = self.Power(self.B * (n*32), ["Potion of Supreme Healing", "+2 Weapon"], {"Potion of Supreme Healing": 3200, "+2 Weapon": 8000})
		self.b4 = self.Power(self.B * (n*256), ["Ambrosia", "Scroll of One-Thousand Swords", "Grimoir of Nemesis", "Ashen Staff", "The Hero's Sword", "+3 Weapon"], {"Ambrosia": 12000, "Scroll of One-Thousand Swords": 8000, "Grimoir of Nemesis": 10000, "Ashen Staff": 15000, "The Hero's Sword": 25000, "+3 Weapon": 18000})
		
		self.range_list = [self.c, self.b, self.b1, self.b2, self.b3, self.b4]
		
	def print_bpower(self):
		self.c.print_bp()
		self.b.print_bp()
		self.b1.print_bp()
		self.b2.print_bp()
		self.b3.print_bp()
		self.b4.print_bp()
		
	def gen_gold(self, dif):
		i = dif % 4
		m_tier = self.range_list[int(dif/4)]
		self.H = int((m_tier.bpower *(3.5 * (i + 1.45)) + 65) * random.uniform(0.85, 1.15))
	
	def gen_loot(self, dif):
		m_tier = self.range_list[int(dif/4)]
		arr_num = len(m_tier.loot)
		loot = m_tier.loot[random.randint(0,(arr_num - 1))]	
		self.H = self.H - m_tier.loot_val[loot]
		return(loot)
	
	def gen_horde(self):
		m = 1
		while m != 0:
			
			try:
				d = input("(Enter 0 to exit)Please enter the difficulty of the dungeon on a scale of 1-20: ")
				dif = int(d)
				m_tier = self.range_list[int(dif/4)]
				
				if m != 0:
					loot_amount = random.randint(1, 2)
					loot_total = ""
					self.gen_gold(dif)
						
					while(loot_amount != 0):
						loot = self.gen_loot(dif)
						loot_total += loot + ", "
						loot_amount = loot_amount - 1
						
						
					print(str(self.H) + " Gold pieces")
					print(loot_total)
					
				else:
					print("Thank you for using my Horde Generator Program! ")
					
			except ValueError:
				print("You entered an Invalid Character. Enter an integer between 1-20. ")
				
			except IndexError:
				print("The number you entered was too large. Enter an integer between 1-20. ")
				
				
	class Power():
		def __init__(self, bpower, loot = [], loot_val = {}):
			self.bpower = bpower
			self.loot = loot
			self.loot_val = loot_val
		def print_bp(self):
			print(str(self.bpower))

horde1 = Horde_Maker()
horde1.gen_bpower()
horde1.print_bpower()
horde1.gen_horde()
