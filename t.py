class Horde_Maker():
	def __init__(self):
		self.B = 50
		self.C = 0
		self.B1 = 0
		self.B2 = 0
		self.B3 = 0
		self.B4 = 0
		self.range_list = []
		self.H = 0
		
	def gen_bpower(self, n):
		self.C = self.B/(n*2)
		self.B1 = self.B * (n*2)
		self.B2 = self.B * (n*8)
		self.B3 = self.B * (n*32)
		self.B4 = self.B * (n*256) 
		print(type(self.B4))
		self.range_list = [self.C, self.C, self.C, self.C, self.B, self.B, self.B, self.B, self.B1, self.B1, self.B1, self.B1, self.B2, self.B2, self.B2, self.B2, self.B3, self.B3, self.B3, self.B3, self.B4]
		
	def print_bpower(self):
		print(self.C)
		print(self.B)
		print(self.B1)
		print(self.B2)
		print(self.B3)
		print(self.B4)
		
	def gen_horde(self, m):
		i = m % 4
		w = self.range_list[m]
		print(i)
		print(w)
		self.H = w *(3.5 * (i + 1.5)) + 100
		h = int(self.H)
		print(h)
		
		

val = input("Please enter the wage disparity of your setting on a scale of 1-3 (1 is little disparity, 2 is moderate, 3 is extreme): ")
horde1 = Horde_Maker()
n = int(val)
horde1.gen_bpower(n)
horde1.print_bpower()
d = input("Please enter the difficulty of the dungeon on a scale of 1-20: ")
dif = int(d)
horde1.gen_horde(dif)
























