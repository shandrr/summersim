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


EXEBIN	= summersim
CLASSES	= $(%.py)

all:
	@echo Python is an interpretive language so no need to compile.
	@make run

run: $(EXEBIN)

$(EXEBIN):$(CLASSES)
	@echo runyanjake-$(EXEBIN): running $(EXEBIN). . .
	@echo
	python3 ./src/$(EXEBIN).py
	@echo
	@echo runyanjake-$(EXEBIN): done.
