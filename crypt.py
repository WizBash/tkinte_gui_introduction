def encode():
	string='abcdefghijklmnopqrstuvwxyz0123456789'
	key='q0wer1tyu2iopa3sdfg4hj5k9lz6xcv7bn8m'

	msg='1234'

	enc =  str.maketrans(dict(zip(string,key)))





	s=msg.translate(enc)
	t=s.translate(enc)
	v=t.translate(enc)

	print(v)

	

def decode():
	string='abcdefghijklmnopqrstuvwxyz0123456789'
	key='q0wer1tyu2iopa3sdfg4hj5k9lz6xcv7bn8m'

	msg='l9j694io0i'


	dec =  str.maketrans(dict(zip(key,string)))




	s=msg.translate(dec)
	t=s.translate(dec)
	v=t.translate(dec)
	print(v)


encode()
decode()