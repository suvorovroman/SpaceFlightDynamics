LDFLAGS = -lX11   
CFLAGS = -g 

xtest:entry.o main.o
	cc -o $@ $^ $(LDFLAGS) 

entry.o:entry.cpp
	cc -c $(CFLAGS) $^

main.o:linux/main.cpp
	cc -c $(CFLAGS) $^

clear:
	rm *.o
