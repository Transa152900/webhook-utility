import dhooks

from dhooks import Webhook, Embed

torty = (input("Спамить (S) Или просто написать,(M)? "))

if torty == ("S"):
	webhook = (input("Введите URL вебхука: "))
	text_spam = (input("Введите текст спама: "))
	kolvo = (input("Введите количество спама: "))
	embedorno = (input("Хотите ли вы чтобы сообщение отправлялось панелью (e) или простым текстом (t): "))

	hook = Webhook(webhook)
	if embedorno == ("t"):
		for i in range(int(kolvo)):
			hook.send(text_spam)
		
	if embedorno == ("e"):
		for i in range(int(kolvo)):
			embed = Embed(
    description=text_spam,
    timestamp='now'  # sets the timestamp to current time
    )
			hook.send(embed=embed)
if torty == ("M"):
	webhook1 = (input("Введите URL вебхука: "))
	hook1 = Webhook(webhook1)
	text = (input("Введите текст: "))
	embedornon = (input("Хотите ли вы чтобы сообщение отправлялось панелью (e) или простым текстом (t): "))

	if embedornon == ("t"):
		hook1.send(text)
	if embedornon == ("e"):
		embed = Embed(
    description=text,
    timestamp='now'  # sets the timestamp to current time
    )
		hook1.send(embed=embed)
