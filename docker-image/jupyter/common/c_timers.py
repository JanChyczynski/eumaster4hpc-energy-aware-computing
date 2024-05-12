# ------------------------------------------------------------------------------
# 
# The original NPB 3.4.1 version was written in Fortran and belongs to: 
# 	http://www.nas.nasa.gov/Software/NPB/
# 
# ------------------------------------------------------------------------------
# 
# The serial C++ version is a translation of the original NPB 3.4.1
# Serial C++ version: https://github.com/GMAP/NPB-CPP/tree/master/NPB-SER
# 
# Authors of the C++ code: 
# 	Dalvan Griebler <dalvangriebler@gmail.com>
# 	Gabriell Araujo <hexenoften@gmail.com>
# 	Júnior Löff <loffjh@gmail.com>
#
# ------------------------------------------------------------------------------
#
# The serial Python version is a translation of the NPB serial C++ version
# Serial Python version: https://github.com/PYTHON
# 
# Authors of the Python code:
#	LUPS (Laboratory of Ubiquitous and Parallel Systems)
#	UFPEL (Federal University of Pelotas)
#	Pelotas, Rio Grande do Sul, Brazil
#
# ------------------------------------------------------------------------------

import time
import numpy

# Global variables
start = numpy.repeat(0.0, 64)
elapsed = numpy.repeat(0.0, 64)

energy_start = numpy.repeat(0.0, 64)
energy_used = numpy.repeat(0.0, 64)


################################# -- D -- ###################################

from random import randrange
cpu_zone = '/sys/devices/virtual/powercap/intel-rapl/intel-rapl:0'


def energy_uj():
	# return randrange(300)
	# TODO verify
	with open(f"{cpu_zone}/energy_uj") as energy_file:
		return int(energy_file.readline())


def max_energy():
	# return 300
	# TODO verify
	with open(f"{cpu_zone}/max_energy_range_uj") as file:
		return int(file.readline())

def energy_consumption(energy_uj_start, energy_uj_end):
	# TODO verify
	# return randrange(300)
	return energy_uj_end - energy_uj_start if energy_uj_end > energy_uj_start else max_energy() - energy_uj_start + energy_uj_end

################################# -- D -- ###################################




#*****************************************************************
#******            T  I  M  E  R  _  C  L  E  A  R          ******
#*****************************************************************
def timer_clear(n):
	global elapsed
	global energy_used
	elapsed[n] = 0.0
	energy_used[n] = 0.0

#*****************************************************************
#******            T  I  M  E  R  _  S  T  A  R  T          ******
#*****************************************************************
def timer_start(n):
	global start
	global energy_start
	start[n] = time.time()
	energy_start[n] = energy_uj()

#*****************************************************************
#******            T  I  M  E  R  _  S  T  O  P             ******
#*****************************************************************
def timer_stop(n):
	global elapsed
	global energy_used
	t = (time.time() - start[n])
	elapsed[n] += t
	e = energy_consumption(energy_start[n], energy_uj())
	energy_used[n] += e

#*****************************************************************
#******            T  I  M  E  R  _  R  E  A  D             ******
#*****************************************************************
def timer_read(n):
	return elapsed[n]


def energy_read(n):
	return energy_used[n]

