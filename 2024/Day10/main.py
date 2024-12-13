#!/usr/bin/python3

DATA = """5678970120787667809876787651450321789810165432234561012345
4301787431296556912765698540341410786728765501103676545434
3212896594365443213454501231232545695439154610898387656946
4307885785872337801653215432545694321089043781763296047877
5456934576901236998740126721694787899676112891054102137898
4327825676210365485035432830780146788765208982567873223703
1012010789301345304126701910567235623654367643432984012612
9887652105401253213239878323458945514545106543221265698543
6798943766798760560145569850179876408763215456100896787432
5212237854899621056776457763287654309854580367018701656501
4302108983014552345889308954390101218345691278929632540987
8921321212123467496973217654321010101210782987834541231236
7010450908765658787210106563898110567623458906543210340145
6524567849434349872323293478967223408988967217890107459054
5433008956721238721494782566554310510177654394345498768765
8942112349810101430585691057431214321287656783216321659056
9853523658901233549674541008120109450392345654307010123141
6765434567890312678234432219078218765431874309458927034230
1034323450765403510165498348569341016210967218567898985541
4125614321877654523276327653414452547893458967898769876632
3210701234988347678987014512103963458982105450745601896781
4678890215679298689898101105432878967821123301234312765890
5469810309100198776543239416001263456710054210126543454323
6954323458210789743987678327122452349821269329237632670110
7856542167345679812310565498214301265430178778748911789224
3067630018901256701423457012303210178923476565652100654343
2188921078872345690501298989452121089012383418983434334534
3298934569863418987632367898763011298234592307894521025676
0387650101678507876753456501014980347105681016765601210787
1456343212589216909865401432325671256501789823454782309898
2341067823410365419872316543234560787432328987123495434321
8932058934321474321891027652101765698543212656016596521030
7634149965430589890765438984989854321692303443067787676543
4543232876787672763210567823870143430781054512198971980612
4687601045298101454569498014561034231278766503456890121701
3894523432101212343278307601432120140389107652107765439890
2183410589043239852101212587347899655473298940998987610141
1012398679650126760120103496256978796554567831876898543234
0310487778743245679833210145107878987143278722365687650125
1223456899012632988744103230123217610012189013451232105676
8346543456598701279655654389874306526323076567600345694789
9857812347405654210346969210165435435414105458912256783238
6768901098312343981237878301456521056905912345863109890104
0345650101232107834369765412347678167876801056874223454323
1278761321943456125078098943678999101210760767985214567910
2109874430854534076165107834567783212323458898876307698876
3436543561763325689234256623478654323212789954343298714565
4567612675610118763240345510569823434101652765210134503443
5698203984323709454121245432234712345612501897898325612652
6782100112345890365039876101165601016780432101107210726761
6783078201076761276321276543036523239891569232216874835890
5894569345987457889430389236543210145652678740125965934701
6784578896590356996321298107012301276743245656734014821012
5693678787101243987654301058905434985890130543876523498763
4542109843262012276019012765676125673981021982923434549854
3432101257876540145328943894387089012832123671019323676345
4309210369901234239457654703298976326721034501208710789234
3218765478710123378765645612107845435434345212345621678101""".split("\n")

class Map:
	def __init__(self, data):
		self.map = self.gen_map(data)
		self.starts = self.find_starts(self.map)

	def gen_map(self, data):
		map = []
		for y, row in enumerate(data):
			map.append([])
			for x, height in enumerate(row):
				map[len(map)-1].append(self.Cell(y, x, height))
		return map

	def find_starts(self, map):
		starts = []
		for row in map:
			for cell in row:
				if(cell.h == 0):
					starts.append(cell)
		return starts
	
	def is_trail(self, map, start):
		queue = [start]
		rating = 0
		while(len(queue) >= 0):
			cC = queue.pop()
			if(map[cC[0]][cC[1]].h == 9):
				rating += 1
			else:
				nexts = cC.find_next_steps(map, cC)
				for nC in nexts:
					queue.append(nC)

	class Cell:
		def __init__(self, y, x, h):
			self.y = y
			self.x = x
			self.h = int(h)

		def find_next_steps(self, map):
			neighbors = [[-1,0], [0,1], [1,0], [0,-1]]
			nY = nX = 0
			queue = []
			height = map[self.y][self.x].h
			for neighbor in neighbors:
				nY, nX = self.y + neighbor[0], self.x + neighbor[1]
				if(nY >= 0 and nY < len(map) and nX >= 0 and nX < len(map[0])):
					if(map[nY][nX].h == (height + 1)):
						queue.append([nY, nX])
			return queue

def part_one(data):
	map = Map(data)
	print(map.starts[0].find_next_steps(map.map))

def part_two(data):
	pass

if __name__ == "__main__":
	part_one(DATA)