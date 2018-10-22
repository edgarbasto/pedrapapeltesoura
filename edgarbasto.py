#elaborado por Edgar Basto n.2222
op = {
    'pedra': {'pedra': 'empate', 'papel':'papel', 'tesoura':'pedra'},
    'papel': {'pedra': 'papel', 'papel':'empate', 'tesoura':'tesoura'},
    'tesoura': {'pedra':'pedra', 'papel':'tesoura', 'tesoura':'empate'},
    }

def joga(a,b):
    print(a + ' vs ' + b + ' ganha:')
    print(op[a][b])

joga('pedra','tesoura')
joga('papel','pedra')

