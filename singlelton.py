# Singleton
class FileHandler():
	#Singleton
	_instance = None
	
	def __init__(self):
		self.path = "text.txt"
	
	def __new__(cls):
		if cls._instance:
			return cls._instance
		else:
			cls._instance = super().__new__(cls)
		return cls._instance
	
	def append_text(self, text):
		f = open(self.path, "a")
		f.write(text)
		f.close()
	
	def read_file(self):
		f = open(self.path, "r")
		text = f.readlines()
		f.close()
		return text


class User:
	def __init__(self, position):
		self.file_descriptor = FileHandler()
		self.position = position

users_arr = list()
for i in range(10):
	users_arr.append(User(i))

for user in users_arr:
	user.file_descriptor.append_text(str(user.position) + "\n")

if __name__ == "__main__":
	a = FileHandler()
	b = FileHandler()
	print(a is b)
	print(a.read_file())
