from datetime import datetime

class Block:
    def __init__(self, index, timestamp, data, hash, previousHash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.previousHash = previousHash
    

def toString(block):
		finalString = "{\n"
		finalString += "\tIndex: " +str(block.index)+"\n"
		finalString += "\tTimestamp: " +str(block.timestamp)+"\n"
		finalString += "\tData: " +str(block.data)+"\n"
		finalString += "\tHash: " +str(block.hash)+"\n"
		finalString += "\tPrevious Hash: " +str(block.previousHash)+"\n"
		finalString += "}\n"
		return finalString


blockchain = []
members = ['Elton','Harwinder','Shaun', 'Zames']

def createBlocks(members):
#check if blockchain is null
	for x in range(0, len(members)):
		dateTimeObj = datetime.now()
		timestamp = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
		if not blockchain:
			previousHash = None;
		else:
			previousHash = blockchain[x-1].hash
		node = Block(x, timestamp, members[x], (hash(str(x)+str(timestamp)+str(members[x]))), previousHash)
		blockchain.append(node);

createBlocks(members)
print("First iteration of blockchain")
for y in blockchain:
	print(toString(y))
#simulation of blockchain update

#onboard to blockchain





print("=============After Update============")
for y in blockchain:
	print(toString(y))



