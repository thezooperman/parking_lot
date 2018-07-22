#!/bin/sh

if [ "$#" -eq 0 ]
then
	python src/main/python/command_parser.py
else
	python src/main/python/command_parser.py $1 
fi
