from hiroyuki import MarkovChain

with open("hiroyuki.txt", encoding="utf-8") as f:
    text = f.read()

mc = MarkovChain(n=2)
mc.train(text)

while True:
    i = input('あなた: ')
    if i == "exit":
        break
    print('ひろゆき: ' + mc.generate(30).replace('\n', ''))