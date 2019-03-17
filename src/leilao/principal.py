from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

gui = Usuario('Gui')
yuri = Usuario('Yuri')

lance_do_yuri = Lance(yuri, 100.0)
lance_do_gui = Lance(gui, 150.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_do_yuri)
leilao.lances.append(lance_do_gui)

print(leilao)
