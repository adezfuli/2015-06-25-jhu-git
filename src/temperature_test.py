import temperature

def f_to_k_test():
	assert temperature.f_to_k(32) == 273.15
	assert temperature.f_to_k(212) == 373.15
