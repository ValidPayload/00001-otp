import os
import random


def gen_pin():
	return "{}".format(
		random.randint(1000, 9999)
	)


def gen_pin_v2(length):
	return ("{}") \
		.format(
			int.from_bytes(
				os.urandom(4),
				byteorder="big"
			) % (10**length),
		) \
		.zfill(length)


