#------------------------------------------------------------------------------
#  Makefile for www.github.com/runyanjake/summersim/
#  @author Jake Runyan
#
#  ***Directives***
#  all: does nothing. Python is interpretive lang so no need to compile.
#  run: runs the program with test parameters.
#  clean: hides all generated files nonessential for running.
#  spotless: cleans down to source level.
#  
#------------------------------------------------------------------------------


EXEBIN	= summergame 
CLASSES	= $(%.py)

all:
	@echo Nothing to do here. Python is an interpretive language so no need to compile.

run: $(EXEBIN)

$(EXEBIN):$(CLASSES)
	@echo runyanjake-$(EXEBIN): running $(EXEBIN). . .
	@echo
	python3 ./src/main.py
	@echo
	@echo runyanjake-$(EXEBIN): done.
