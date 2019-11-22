

class MaquinaDePilha():
	def __init__(self,file):
		self.file  = file
	
	def Backend(self):
		
		stack = []
		with open(self.file, 'r') as fp:
			for line in fp.readlines():
				#print(stack)
				if "PUSH" in line:
					stack.append(int(line.split(' ')[1]))
				if  line in "SUB\nMULT\nSUM\nDIV\n":
					#print("oi")
					a = stack.pop() 
					b = stack.pop()
					stack.append(self.operation(line.replace('\n', ''), a, b))
				if "PRINT" in line:
					a = stack.pop()
					stack.append(a)
					#print(a)
		
		#stack.reverse()
		#print(stack)

		"""
		while(True):
			operator1 = stack.pop()
			print(operator1)
			operator2 = stack.pop()
			print(operator2)
			op = stack.pop()
			print(op)
			outcome = self.operation(op.replace('\n',''),operator1.replace('PUSH',''),operator2.replace('PUSH',''))
			print(outcome)
			
			stack.append('PUSH ' +str(outcome))
			if len(stack) == 2:
				break
			
		"""			
			
		
		return stack[0]
	def operation(self, op, op1, op2):
		#print(int(op1), int(op2))
		if   op == 'MULT':
			return int(op1) * int(op2)
		elif op == 'DIV':
			return int(op1) / int(op2)		
		elif op == 'SUM':
			return int(op1) + int(op2)
		elif op == 'SUB':
			return int(op1) - int(op2)
		
def main():
	file_name = 'teste.txt'
	stackMachine = MaquinaDePilha(file_name)
	print(stackMachine.Backend())
if __name__ == '__main__':
	main()