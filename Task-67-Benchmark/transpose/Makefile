COMP=g++
FLAG=-O1 -larmadillo

.PHONY: all
all: cpp

.PHONY: clean
clean: rm -rf cpp

cpp: transpose.cpp
	$(COMP) -o cpp transpose.cpp $(FLAG)
