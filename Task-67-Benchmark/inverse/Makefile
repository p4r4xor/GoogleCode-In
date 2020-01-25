COMP=g++
FLAG=-O1 -larmadillo

.PHONY: all
all: cpp

.PHONY: clean
clean: rm -rf cpp

cpp: inverse.cpp
	$(COMP) -o cpp inverse.cpp $(FLAG)
