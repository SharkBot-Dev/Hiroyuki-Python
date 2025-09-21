from hiroyuki import MarkovChain

with open("hiroyuki.txt", encoding="utf-8") as f:
    text = f.read()

mc = MarkovChain(n=2)
mc.train(text)

server_name = input('サーバー名: ')

while True:
    i = input('あなた: ')
    if i == "exit":
        break
    print('ひろゆき: ' + mc.generate(30, server_name).replace('\n', ''))