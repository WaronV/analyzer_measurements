from time import sleep
from random import randint
from datetime import datetime
import statistics

class Probka():
	def __init__(self, pomiar=[], wynik=0):
		self._pomiar=pomiar
		self._wynik=wynik

	def dodaj_pomiar(self, newPomiar):
		self._pomiar.append(newPomiar)
		return self._pomiar

	def usun_pomiar(self):
		nrPomiar=len(self._pomiar)+1
		while True:
			if len(self._pomiar)==0:
				print("Nie ma pomiarow")
				break
			if nrPomiar>=0 and nrPomiar<len(self._pomiar):
				self._pomiar.pop(nrPomiar)
				break
			else:
				nrPomiar=int(input("Pomiar do usuniecia: "))-1
		return self._pomiar

	def drukowanie_pomiarow(self):
		hist2=[str(x) for x in self._pomiar]
		print("Historia wynikow: "+", ".join(hist2))

	def wynik(self, w):
		if z=="a":
			w= statistics.mean(self._pomiar)
		elif z=="b":
			w=statistics.geometric_mean(self._pomiar)
		elif z=="c":
			w=statistics.harmonic_mean(self._pomiar)
		print(w)
		return w

	@property
	def wyniki (self):
		return self._wynik

	@wyniki.getter
	def wyniki (self):
		hist2=[str(x) for x in self._wynik]
		return "Historia wynikow: "+", ".join(hist2)

	@wyniki.setter
	def wyniki (self, value):
		return self._wynik.append(value)



def dekoracja(func):
	def wrapper(*args, **kwargs):
		print(" ")
		print("-------------------------------------")
		z=func(*args, **kwargs)
		print("-------------------------------------")
		print(" ")
		return z
	return wrapper


def unknow(v, v1, v2, v3=False, v4=False):
	while True:
		if v==v1 or v==v2 or v==v3 or v==v4:
			break
		else:
			v=input("Niewlasciwy znak! Podaj wlasciwy znak: ").lower()
	return v

@dekoracja
def question (v1,v2,v3,v4=" ",v5=" "):
	print(v1)
	print(v2)
	print(v3)
	print(v4)
	print(v5)
	return input("Podaj odpowiedz: ")


while True:
	table=[]
	pomiar=Probka()
	table.append(pomiar)

	while True:
		x=input("podaj liczbe x lub wpisz LOS aby wygenerowalo liczbe z przedzialu <1,100>: ")
		y=input("podaj liczbe y lub wpisz LOS aby wygenerowalo liczbe z przedzialu <1,100>: ")
		if x=="los":
			x=randint(1,100)
			print("wylosowana liczba x to", x)

		if y=="los":
			y=randint(1,100)
			print("wylosowana liczba y to", y)

		x=float(x)
		y=float(y)

		z=question("Rownania : ","a)x+y","b)x-y","c)x*y","d)x/y")
		z=unknow(z.lower(), "a", "b", "c", "d")

		if z=="a":
			k=x+y
		elif z=="b":
			k=x-y
		elif z=="c":
			k=x*y
		elif z=="d":
			try:
				k=x/y
			except:
				while True:
					if y!=0:
						break
					else:
						y=input("Nie mozna dzielic przez 0! Wprowadz inna wartosc: ")
						y=float(y)
				k=x/y

		#-------------------------------------------------------------------------------------
		
		print("Wynik: ", k)
		hist=pomiar.dodaj_pomiar(k)

		pomiar.drukowanie_pomiarow()
		z=question("Nowe rownanie?","y) Tak","n) nie")
		z=unknow(z.lower(), "n", "y")
		if z=="n":
			break
		elif z=="y":
			continue
	while True:
		z=question("Usunac pomiar?","y) Tak","n) nie")
		z=unknow(z.lower(), "n", "y")
	
		if z=="y":
			hist=pomiar.usun_pomiar()
		elif z=="n":
			break

		pomiar.drukowanie_pomiarow()
	#-------------------------------------------------------------------------------------

	if all([i%2==0 for i in hist]):
		print("\n"+"WOW! wszystkie parzyste!"+"\n")
	if any([i<0 for i in hist]):
		print("\n"+"Uwaga! Wystepują wartosci ujemne!"+"\n")

	#-------------------------------------------------------------------------------------
	z=question("Jaki wyniki?","a)srednia arytmetyczna","b)srednia geometryczna","c)srednia harmoniczna")
	z=unknow(z.lower(), "a", "b","c","d")
	k=pomiar.wynik(z)
	#-------------------------------------------------------------------------------------


	z=question("Czy rozpoczac nowa serie?","y)tak ","n)zamknij plik")
	z=unknow(z.lower(), "y", "n",)
	if z=="n":
		break
	elif z=="y":
		continue

	Probka.wyniki=k
	print(Probka.wyniki)

z=question("Zapisac pomiary do txt?","y)tak ","n)zamknij plik")
z=unknow(z.lower(), "y", "n",)
#if z=="y":
	#z=input("Nazwij plik: ")
	#plikHist=open(z, "a")

	#plikHist.close()
del y,x,z,hist, k

	