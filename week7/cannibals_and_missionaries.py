

class State():
	def __init__(self, cannibalLeft, missionaryLeft, boat, cannibalRight, missionaryRight):
		self.cannibalLeft = cannibalLeft
		self.missionaryLeft = missionaryLeft
		self.boat = boat
		self.cannibalRight = cannibalRight
		self.missionaryRight = missionaryRight
		self.parent = None

	def winCheck(self):
		if self.cannibalLeft == 0 and self.missionaryLeft == 0:
			return True
		else:
			return False

	def isValid(self):
		if self.missionaryLeft >= 0 and self.missionaryRight >= 0 \
                   and self.cannibalLeft >= 0 and self.cannibalRight >= 0 \
                   and (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) \
                   and (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight):
			return True
		else:
			return False

	def __eq__(self, other):
		return self.cannibalLeft == other.cannibalLeft and self.missionaryLeft == other.missionaryLeft \
                   and self.boat == other.boat and self.cannibalRight == other.cannibalRight \
                   and self.missionaryRight == other.missionaryRight

	def __hash__(self):
		return hash((self.cannibalLeft, self.missionaryLeft, self.boat, self.cannibalRight, self.missionaryRight))

def successors(currentState):
	children = [];
	#boat on left side
	#Hector Alvarez - MU Data Structures
	if currentState.boat == 'left':
		newState = State(currentState.cannibalLeft, currentState.missionaryLeft - 2, 'right',
                                  currentState.cannibalRight, currentState.missionaryRight + 2)
		## Two missionaries cross left to right.
		if newState.isValid():
			newState.parent = currentState
			children.append(newState)
		newState = State(currentState.cannibalLeft - 2, currentState.missionaryLeft, 'right',
                                  currentState.cannibalRight + 2, currentState.missionaryRight)
		## Two cannibals cross left to right.
		if newState.isValid():
			newState.parent = currentState
			children.append(newState)
		newState = State(currentState.cannibalLeft - 1, currentState.missionaryLeft - 1, 'right',
                                  currentState.cannibalRight + 1, currentState.missionaryRight + 1)
		## One missionary and one cannibal cross left to right.
		if newState.isValid():
			newState.parent = currentState
			children.append(newState)
		newState = State(currentState.cannibalLeft, currentState.missionaryLeft - 1, 'right',
                                  currentState.cannibalRight, currentState.missionaryRight + 1)
		## One missionary crosses left to right.
		if newState.isValid():
			newState.parent = currentState
			children.append(newState)
		newState = State(currentState.cannibalLeft - 1, currentState.missionaryLeft, 'right',
                                  currentState.cannibalRight + 1, currentState.missionaryRight)
		## One cannibal crosses left to right.
		if newState.isValid():
			newState.parent = currentState
			children.append(newState)
	else:
		newState = State(currentState.cannibalLeft, currentState.missionaryLeft + 2, 'left',
                                  currentState.cannibalRight, currentState.missionaryRight - 2)
		## Two missionaries cross right to left.
		if newState.isValid():
			newState.parent = currentState
			children.append(newState)
		newState = State(currentState.cannibalLeft + 2, currentState.missionaryLeft, 'left',
                                  currentState.cannibalRight - 2, currentState.missionaryRight)
		## Two cannibals cross right to left.
		if newState.isValid():
			newState.parent = currentState
			children.append(newState)
		newState = State(currentState.cannibalLeft + 1, currentState.missionaryLeft + 1, 'left',
                                  currentState.cannibalRight - 1, currentState.missionaryRight - 1)
		## One missionary and one cannibal cross right to left.
		if newState.isValid():
			newState.parent = currentState
			children.append(newState)
		newState = State(currentState.cannibalLeft, currentState.missionaryLeft + 1, 'left',
                                  currentState.cannibalRight, currentState.missionaryRight - 1)
		## One missionary crosses right to left.
		if newState.isValid():
			newState.parent = currentState
			children.append(newState)
		newState = State(currentState.cannibalLeft + 1, currentState.missionaryLeft, 'left',
                                  currentState.cannibalRight - 1, currentState.missionaryRight)
		## One cannibal crosses right to left.
		if newState.isValid():
			newState.parent = currentState
			children.append(newState)
	return children

def breadthFirstSearch():
	initialState = State(3,3,'left',0,0)
	if initialState.winCheck():
		return initialState
	frontier = list()
	explored = set()
	frontier.append(initialState)
	
	while frontier:
		state = frontier.pop(0)
		if state.winCheck():
			return state
		explored.add(state)
		children = successors(state)
		for child in children:
			if (child not in explored) or (child not in frontier):
				frontier.append(child)
	return None

def printSolution(solution):
		path = []
		path.append(solution)
		parent = solution.parent
		while parent:
			path.append(parent)
			parent = parent.parent

		for t in range(len(path)):
			state = path[len(path) - t - 1]
			print ("canibal left: " + str(state.cannibalLeft) + " missionary left : " + str(state.missionaryLeft) \
                              + " ----boat ----- " + "Canibal right :" + str(state.cannibalRight)  + " Missionaries right : " \
                             + str(state.missionaryRight) )

def main():
	solution = breadthFirstSearch()
	print ("Missionaries and Cannibals solution:")

	printSolution(solution)

# if called from the command line, call main()
if __name__ == "__main__":
    main()