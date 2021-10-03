LDFLAGS = -lX11   
CFLAGS = -g
CPP = g++
LINKER = g++

xtest:entry.o linux/main.o x11/display.o x11/enter_instance_display.o
	$(LINKER) -o $@ $^ $(LDFLAGS) 

entry.o:entry.cpp display.h
	$(CPP) -c $(CFLAGS) $^

linux/main.o:linux/main.cpp
	$(CPP) -c $(CFLAGS) $^ -o $@

x11/display.o:x11/display.cpp
	$(CPP) -c $(CFLAGS) $^ -o $@

x11/enter_instance_display.o:x11/enter_instance_display.cpp
	$(CPP) -c $(CFLAGS) $^ -o $@

clear:
	rm *.o
