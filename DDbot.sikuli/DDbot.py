import os
import time
import signal
myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)

import myLib

def main():
	size = 40
	setAutoWaitTimeout(1)
	Settings.MoveMouseDelay = 0
	rec = Screen(0).getBounds()
	maxh = rec.height
	maxw = rec.width
	print maxw,maxh
	xsize = maxw/size+1
	ysize = maxh/size+1
	notfound = 0
	a = [Pattern(i).similar(0.85) for i in ["red.png","blue.png","green.png","yellow.png","purple.png"]]
	b = ["continue.png","close.png","play1.png","play2.png","skip.png"]
	while True:
		print "While 1 loop"
		for i,d in enumerate(a):
			print "start find %s %d" % (d,i)
			arr = [[myLib.diamond(Location(0,0)) for j in range(xsize)] for i in range(ysize)]
			found1 = True
			try:
				matches = findAll(d)
			except FindFailed:
				print "except FindFailed"
				found1 = False
			if found1:
				for j in matches:
					# print j.getX(),j.getY()
					arr[j.getY()/size][j.getX()/size].set(i,j)

				matches.destroy()
				print "find ok"
				# for i in arr:
				# 	for j in i:
				# 		print j.n,
				# 	print

				earth = []
				print "cal"
				for i in range(ysize):
					for j in range(xsize):
						if arr[i][j].n==-1 or arr[i][j].s!=0:continue
						# print "%d at %d %d" % (len(earth),i,j)
						n = arr[i][j].n
						earth.append(myLib.counter(arr[i][j].l))
						stack = [[i,j]]
						while len(stack):
							ii,jj = stack.pop()
							# print ii,jj
							if arr[ii][jj].s==1:continue
							arr[ii][jj].s = 1
							earth[-1].n+=1
							if ii!=0 and n==arr[ii-1][jj].n and arr[ii-1][jj].s==0:
								stack.append([ii-1,jj])
							if jj!=0 and n==arr[ii][jj-1].n and arr[ii][jj-1].s==0:
								stack.append([ii,jj-1])
							if ii!=ysize-1 and n==arr[ii+1][jj].n and arr[ii+1][jj].s==0:
								stack.append([ii+1,jj])
							if jj!=xsize-1 and n==arr[ii][jj+1].n and arr[ii][jj+1].s==0:
								stack.append([ii,jj+1])
				print "cal ok"
				found2 = False
				if len(earth):
					toclick = max(earth,key=lambda x:x.n)
					if toclick.n >= 3:
						print "found"
						found2 = True
						click(toclick.l)
						print "diamond %d" % (toclick.n)
						notfound = 0
				if not found2:
					notfound+=1

			print "not found = %d" % notfound
			if not found1 or notfound==len(a):
				notfound = 0
				found1 = True
				print "Try to enter game"
				ok = False
				while not ok:
					print "Looping"
					ok = True
					for i in b:
						if exists(Pattern(i).similar(0.92)):
							print "found way",i
							click(Pattern(i).similar(0.92))
							# ok = False
							if i == "play2.png":
								print "BREAKKKKK"
								time.sleep(2)
								ok = True
								break
			# print "cooldown"
			# time.sleep(1)

if __name__ == '__main__':
	main()