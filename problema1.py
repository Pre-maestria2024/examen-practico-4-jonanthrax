"""
import pathlib

def get_indexes_from_file(file_lines):
	indexes = [] # indexes
	test_id = 1
	for i,line in enumerate(file_lines):
		if line.endswith(")"):
			indexes.append((test_id, i))
			test_id += 1
			pass
		pass
	
	extended_indexes = []
	# Iteramos sobre la lista de índices hasta el penúltimo elemento
	for i in range(len(indexes) - 1):
		# Obtenemos el elemento actual y el siguiente
		x_current, y_current = indexes[i]
		x_next, y_next = indexes[i + 1]
		# Generamos la tupla (x_current, y_current, x_next, y_next)
		extended_indexes.append(
			(x_current, y_current, x_next, y_next)
			)
		pass
	return extended_indexes
def read_inputs_from_file(folderpath, filename='p01_tests.txt'):
	input_folder = pathlib.Path(folderpath)
	input_file = input_folder / filename
	full_tests = {}

	with open(input_file.as_posix(), 'r') as InputFile:
		lines = [line.strip() for line in InputFile.readlines()]
		indexes = get_indexes_from_file(file_lines=lines)
		#print("indexes")
		#print(indexes)
		for (x_current, y_current, x_next, y_next
	   			) in indexes:
			current_test = {}
			test_lines = lines[y_current+1:y_next-1]
			output_line = lines[y_next-2]
			
			# inputs:
			for k,line in enumerate(test_lines):
				if line == "[i]":
					# Leer m y n
					m, n = map(int, test_lines[k + 1].split())
					# Leer H
					H = list(map(int, test_lines[k + 2].split()))
					# Leer D
					D = list(map(int, test_lines[k + 3].split()))

					current_test['m'] = m
					current_test['n'] = n
					current_test['H'] = H
					current_test['D'] = D
					pass
				pass
			# output:
			current_test['o'] = output_line.replace("[o] ", " ")

			full_tests[x_current] = current_test
			pass
		pass
	return full_tests
 	"""

def	solve_major_muffin(m, n, H, D):
	T = sum(D)

	# dp[k] = mínimo costo (pérdida en dólares) para alcanzar salud k.
	# Inicializamos dp[0] = 0 y dp[1..n] = infinito.
	INF = 10**9
	dp = [0] + [INF]*n
	# Para cada alimento (0-indexado)
	for i in range(m):
		h = H[i]
		d = D[i]
		# Actualizamos de atrás hacia adelante para usar cada alimento solo una vez.
		for k in range(n, -1, -1):
			if dp[k] != INF:
				newk = k + h
				if newk > n:
					newk = n
					pass
				dp[newk] = min(dp[newk], dp[k] + d)
				pass
			pass
		pass
	return 0 if (dp[n] == INF) else T - dp[n]
"""
input_folder = r"C://Users//jvq_8//Desktop//MCIES//03_PROGRA//repo_04//"
tests = read_inputs_from_file(folderpath=input_folder,)
for i,test in tests.items():
	m = test['m']
	n = test['n']
	H = test['H']
	D = test['D']
	O = test['o']	
	result = solve_major_muffin(m, n, H, D)
	print("Test: {} | m: {} | n: {}".format(i, m, n))
	print("Output: {} | Expected: {}".format(result, O))
	print("")
	pass
	"""
def main():
	m, n = map(int, input().split())
	H = list(map(int, input().split()))
	D = list(map(int, input().split()))
	result = solve_major_muffin(m, n, H, D)
	print("{}".format(result))
	pass
if __name__ == '__main__':
	main()
	pass

