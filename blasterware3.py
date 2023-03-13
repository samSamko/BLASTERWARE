from graphics import *
tela=GraphWin("BLASTERWARE",1280,720)
fundo_0=Image(Point(640,360),"fundo_0.gif")
fundo_0.draw(tela)
fundo_1=Image(Point(640,360),"fundo_1.gif")
fundo_2=Image(Point(640,360),"fundo_2.gif")
fundo_3=Image(Point(640,360),"fundo_3.gif")
fundo_4=Image(Point(640,360),"fundo_4.gif")
fundo_5=Image(Point(640,360),"fundo_5.gif")
secret=Image(Point(640,360),"secret.gif")
secret_2=Image(Point(640,360),"secret_2.gif")
atual=3
instru_m=Text(Point(200,150),"Movimentos: Setas")
instru_m.setTextColor("white")
instru_m.setSize(26)
instru_m.setStyle("bold")
instru_t=Text(Point(200,200),"Atirar: Shift Direito")
instru_t.setTextColor("white")
instru_t.setSize(26)
instru_t.setStyle("bold")
bola=Circle(Point(200,100),30)
bola.setFill("purple")
vida_4=Text(Point(200,100),"4")
vida_4.setTextColor("white")
vida_4.setSize(36)
vida_3=Text(Point(200,100),"3")
vida_3.setTextColor("white")
vida_3.setSize(36)
vida_2=Text(Point(200,100),"2")
vida_2.setTextColor("white")
vida_2.setSize(36)
vida_1=Text(Point(200,100),"1")
vida_1.setTextColor("white")
vida_1.setSize(36)
atual_2=3
instru_m_2=Text(Point(1080,150),"Movimentos: A-W-D")
instru_m_2.setTextColor("white")
instru_m_2.setSize(26)
instru_m_2.setStyle("bold")
instru_t_2=Text(Point(1080,200),"Atirar: Espaco")
instru_t_2.setTextColor("white")
instru_t_2.setSize(26)
instru_t_2.setStyle("bold")
bola_2=Circle(Point(1080,100),30)
bola_2.setFill("red")
vida_10_2=Text(Point(1080,100),"10")
vida_10_2.setTextColor("white")
vida_10_2.setSize(36)
vida_9_2=Text(Point(1080,100),"9")
vida_9_2.setTextColor("white")
vida_9_2.setSize(36)
vida_8_2=Text(Point(1080,100),"8")
vida_8_2.setTextColor("white")
vida_8_2.setSize(36)
vida_7_2=Text(Point(1080,100),"7")
vida_7_2.setTextColor("white")
vida_7_2.setSize(36)
vida_6_2=Text(Point(1080,100),"6")
vida_6_2.setTextColor("white")
vida_6_2.setSize(36)
vida_5_2=Text(Point(1080,100),"5")
vida_5_2.setTextColor("white")
vida_5_2.setSize(36)
vida_4_2=Text(Point(1080,100),"4")
vida_4_2.setTextColor("white")
vida_4_2.setSize(36)
vida_3_2=Text(Point(1080,100),"3")
vida_3_2.setTextColor("black")
vida_3_2.setSize(36)
vida_2_2=Text(Point(1080,100),"2")
vida_2_2.setTextColor("black")
vida_2_2.setSize(36)
vida_1_2=Text(Point(1080,100),"1")
vida_1_2.setTextColor("black")
vida_1_2.setSize(36)
jogador=Rectangle(Point(30,600),Point(80,650))
jogador.setFill("purple")
pulo=0
lado=2
cont=0
cont_tiro=0
tiro_esq=0
tiro_dir=0
hp=3
jogador_2=Rectangle(Point(1210,200),Point(1260,250))
jogador_2.setFill("red")
pulo_2=0
lado_2=0
cont_2=0
cont_tiro_2=0
tiro_esq_2=0
tiro_dir_2=0
hp_2=3
cena=0
sprite=1
ciclo=0
boss_atir_esq=Image(Point(900,665),"boss_atir_esq.gif")
boss_esc_esq=Image(Point(900,665),"boss_esc_esq.gif")
boss_tiro_cont=0
cont_boss=0
boss_tiro=0
boss_hp=2
boss_esc_cont=0
boss_def=0
esc_cont=0
boss_atir_esq_2=Image(Point(930,465),"boss_atir_esq.gif")
boss_esc_esq_2=Image(Point(930,465),"boss_esc_esq.gif")
boss_tiro_cont_2=0
cont_boss_2=0
boss_tiro_2=0
boss_hp_2=2
boss_esc_cont_2=0
boss_def_2=0
esc_cont_2=0
dummy=Image(Point(250,625),"dummy.gif")
dummy_hp=1
tanque=Image(Point(800,665),"tanque.gif")
tanque_hp=2
tanque_cont_tiro=0
tanque_tiro=0
tanque_cont=0
tanque_2=Image(Point(1180,665),"tanque.gif")
tanque_hp_2=2
tanque_cont_tiro_2=0
tanque_tiro_2=0
tanque_cont_2=0
bateria=Image(Point(280,550),"bateria.gif")
bat=1
andador=Image(Point(1000,500),"andador.gif")
cont_tiro_inst_andador=0
cont_tiro_andador=0
cont_onda_andador=0
atira_andador=0
onda_andador=0
andador_hp=10
turret_dir=Image(Point(150,340),"turret_dir.gif")
turret_dir_hp=2
cont_tiro_inst_turret_dir=0
cont_tiro_turret_dir=0
atira_turret_dir=0
turret_esq=Image(Point(1180,490),"turret_esq.gif")
turret_esq_hp=2
cont_tiro_inst_turret_esq=0
cont_tiro_turret_esq=0
atira_turret_esq=0
def atirar_andador():
	posi=andador.getAnchor()
	posx=posi.getX()
	posy=posi.getY()
	tiro_andador=Circle(Point(posx-180,posy-70),150)
	tiro_andador.setFill("red")
	return tiro_andador
def atirar_turret_dir():
	posi=turret_dir.getAnchor()
	posx=posi.getX()
	posy=posi.getY()
	tiro_turret_dir_im=Image(Point(posx,posy),"turret_tiro.gif")
	return tiro_turret_dir_im
def atirar_turret_esq():
	posi=turret_esq.getAnchor()
	posx=posi.getX()
	posy=posi.getY()
	tiro_turret_esq_im=Image(Point(posx,posy),"turret_tiro.gif")
	return tiro_turret_esq_im
def atirar_tanque():
	posi=tanque.getAnchor()
	posx=posi.getX()
	posy=posi.getY()
	tiro_tanque_im=Circle(Point(posx,posy),20)
	tiro_tanque_im.setFill("orange")
	return tiro_tanque_im
def atirar_tanque_2():
	posi=tanque_2.getAnchor()
	posx=posi.getX()
	posy=posi.getY()
	tiro_tanque_im=Circle(Point(posx,posy),10)
	tiro_tanque_im.setFill("red")
	return tiro_tanque_im
def atirar_boss():
	posi=boss_atir_esq.getAnchor()
	posx=posi.getX()
	posy=posi.getY()
	tiro_boss=Image(Point(posx,posy),"boss_tiro.gif")
	return tiro_boss
def atirar_boss_2():
	posi=boss_atir_esq_2.getAnchor()
	posx=posi.getX()
	posy=posi.getY()
	tiro_boss_2=Image(Point(posx,posy),"boss_tiro.gif")
	return tiro_boss_2
def atirar_jogador_2():
	posi_2=jogador_2.getCenter()
	posx_2=posi_2.getX()
	posy_2=posi_2.getY()
	tiro_2=Circle(Point(posx_2,posy_2),10)
	tiro_2.setFill("red")
	return tiro_2
def atirar_jogador():
	posi=jogador.getCenter()
	posx=posi.getX()
	posy=posi.getY()
	tiro=Circle(Point(posx,posy),10)
	tiro.setFill("purple")
	return tiro
tela.ligar_Buffer()
while (True):
	teclado=tela.checkKey_Buffer()
	if cena==0:
		boss_tiro_cont_2=0
		cont_boss_2=0
		boss_tiro_2=0
		boss_hp_2=2
		boss_esc_cont_2=0
		boss_def_2=0
		esc_cont_2=0
		tanque_hp_2=2
		tanque_cont_tiro_2=0
		tanque_tiro_2=0
		tanque_cont_2=0
		turret_esq_hp=2
		cont_tiro_inst_turret_esq=0
		cont_tiro_turret_esq=0
		atira_turret_esq=0
		turret_dir_hp=2
		cont_tiro_inst_turret_dir=0
		cont_tiro_turret_dir=0
		atira_turret_dir=0
		cont_tiro_inst_andador=0
		cont_tiro_andador=0
		cont_onda_andador=0
		atira_andador=0
		onda_andador=0
		andador_hp=10
		bat=1
		dummy_hp=1
		tanque_hp=2
		tanque_cont_tiro=0
		tanque_tiro=0
		tanque_cont=0
		pulo_2=0
		lado_2=0
		cont_2=0
		cont_tiro_2=0
		tiro_esq_2=0
		tiro_dir_2=0
		hp_2=3
		atual_2=3
		cena=0
		pulo=0
		lado=0
		cont=0
		cont_tiro=0
		tiro_esq=0
		tiro_dir=0
		hp=3
		atual=3
		boss_tiro_cont=0
		cont_boss=0
		boss_tiro=0
		boss_hp=2
		boss_esc_cont=0
		boss_def=0
		esc_cont=0
		jogador=Rectangle(Point(30,600),Point(80,650))
		jogador.setFill("Purple")
		jogador_2=Rectangle(Point(1210,200),Point(1260,250))
		jogador_2.setFill("red")
		print(teclado)
		if len(teclado)>0 and "Return" in teclado:
			fundo_1.draw(tela)
			fundo_0.undraw()
			jogador.draw(tela)
			cena=1
		if len(teclado)>0 and "space" in teclado:
			fundo_3.draw(tela)
			jogador.draw(tela)
			bola.draw(tela)
			vida_3.draw(tela)
			instru_m.draw(tela)
			instru_t.draw(tela)
			instru_m_2.draw(tela)
			instru_t_2.draw(tela)
			jogador_2.draw(tela)
			bola_2.draw(tela)
			cena=6
		if len(teclado)>0 and "p" in teclado:
			secret.draw(tela)
			time.sleep(5)
			secret.undraw()
		if len(teclado)>0 and "l" in teclado:
			secret_2.draw(tela)
			time.sleep(5)
			secret_2.undraw()
	if cena==1:
		posi=jogador.getCenter()
		posx=posi.getX()
		posy=posi.getY()
		print(teclado)
		print(posx,posy)
		if len(teclado)>0 and "Left" in teclado and posx>10:
			if "Shift_L" in teclado:
				jogador.move(-10,0)
				lado=1
			else:
				jogador.move(-5,0)
				lado=1
		if len(teclado)>0 and "Right" in teclado:
			if "Shift_L" in teclado:
				jogador.move(10,0)
				lado=2
			else:
				jogador.move(5,0)
				lado=2
		if len(teclado)>0 and "Up" in teclado and posy>660 and pulo==0:
			pulo=1
		if len(teclado)>0 and "space" in teclado and lado==1 and tiro_esq==0 and tiro_dir==0:
			tiro_esq=1
			tiro=atirar_jogador()
			tiro.draw(tela)
		if tiro_esq==1:
			tiro.move(-8,0)
			cont_tiro+=1
			if cont_tiro==75:
				cont_tiro=0
				tiro_esq=0
				tiro.undraw()
		if len(teclado)>0 and "space" in teclado and lado==2 and tiro_dir==0 and tiro_esq==0:
			tiro_dir=1
			tiro=atirar_jogador()
			tiro.draw(tela)
		if tiro_dir==1:
			tiro.move(8,0)
			cont_tiro+=1
			if cont_tiro==75:
				cont_tiro=0
				tiro_dir=0
				tiro.undraw()
		if pulo==1:
			jogador.move(0,-4)
			cont+=1
			if cont==40:
				cont=0
				pulo=0
		elif posy<670:
			jogador.move(0,5)
		if posx>1280:
			jogador.undraw()
			fundo_2.draw(tela)
			fundo_1.undraw()
			jogador.draw(tela)
			bola.draw(tela)
			dummy.draw(tela)
			tanque.draw(tela)
			tanque_2.draw(tela)
			jogador.move(-1270,0)
			cena=2
	if cena==2:
		posi=jogador.getCenter()
		posx=posi.getX()
		posy=posi.getY()
		print(teclado)
		print(posx,posy)
		if hp==3 and atual==3:
			vida_3.draw(tela)
			atual=2
		if hp==2 and atual==2:
			vida_3.undraw()
			vida_2.draw(tela)
			atual=1
		if hp==1 and atual==1:
			vida_2.undraw()
			vida_1.draw(tela)
			atual=0
		if len(teclado)>0 and "Left" in teclado and posx>10:
			if "Shift_L" in teclado:
				jogador.move(-10,0)
				lado=1
			else:
				jogador.move(-5,0)
				lado=1
		if len(teclado)>0 and "Right" in teclado:
			if "Shift_L" in teclado:
				jogador.move(10,0)
				lado=2
			elif posx>1270 and dummy_hp>0 or posx>1270 and tanque_hp>0 or posx>1270 and tanque_hp_2>0:
				jogador.move(0,0)
				lado=2
			else:
				jogador.move(5,0)
				lado=2
		if tanque_cont==100:
			tanque_tiro=1
			tanque_tiro_im=atirar_tanque()
			tanque_tiro_im.draw(tela)
		if tanque_tiro==1:
			tanque_cont=0
			tanque_tiro_im.move(-6,0)
			tanque_cont_tiro+=1
			tiro_pos_tanque=tanque_tiro_im.getCenter()
			tiro_posx_tanque=tiro_pos_tanque.getX()
			tiro_posy_tanque=tiro_pos_tanque.getY()
			if tanque_cont_tiro==50:
				tanque_tiro=0
				tanque_cont=0
				tanque_tiro_im.undraw()
				tanque_cont_tiro=0
			elif tiro_posy_tanque>=posy-30 and tiro_posy_tanque<posy+30 and tiro_posx_tanque>posx-30 and tiro_posx_tanque<posx+30:
				hp-=1
				tanque_tiro=0
				tanque_cont=0
				tanque_tiro_im.undraw()
				tanque_cont=0
		if tanque_cont_2==100:
			tanque_tiro_2=1
			tanque_tiro_im_2=atirar_tanque_2()
			tanque_tiro_im_2.draw(tela)
		if tanque_tiro_2==1:
			tanque_cont_2=0
			tanque_tiro_im_2.move(-10,0)
			tanque_cont_tiro_2+=1
			tiro_pos_tanque_2=tanque_tiro_im_2.getCenter()
			tiro_posx_tanque_2=tiro_pos_tanque_2.getX()
			tiro_posy_tanque_2=tiro_pos_tanque_2.getY()
			if tanque_cont_tiro_2==50:
				tanque_tiro_2=0
				tanque_cont_2=0
				tanque_tiro_im_2.undraw()
				tanque_cont_tiro_2=0
			elif tiro_posy_tanque_2>=posy-30 and tiro_posy_tanque_2<posy+30 and tiro_posx_tanque_2>posx-30 and tiro_posx_tanque_2<posx+30:
				hp-=1
				tanque_tiro_2=0
				tanque_cont_2=0
				tanque_tiro_im_2.undraw()
				tanque_cont_2=0
		if len(teclado)>0 and "Up" in teclado and posy>660 and posy<700 and pulo==0:
			pulo=1
		if len(teclado)>0 and "space" in teclado and lado==1 and tiro_esq==0 and tiro_dir==0:
			tiro_esq=1
			tiro=atirar_jogador()
			tiro.draw(tela)
		if tiro_esq==1:
			tiro.move(-8,0)
			cont_tiro+=1
			tiro_pos=tiro.getCenter()
			tiro_posx=tiro_pos.getX()
			tiro_posy=tiro_pos.getY()
			if cont_tiro==75:
				cont_tiro=0
				tiro_esq=0
				tiro.undraw()
			elif tiro_posy>=625-35 and tiro_posy<625+55 and tiro_posx>250-35 and tiro_posx<250+35 and dummy_hp>0:
				dummy_hp-=1
				dummy.undraw()
				cont_tiro=0
				tiro_esq=0
				tiro.undraw()
			elif tiro_posy>=625-35 and tiro_posy<625+55 and tiro_posx>800-35 and tiro_posx<800+35 and tanque_hp>0:
				tanque_hp-=1
				cont_tiro=0
				tiro_esq=0
				tiro.undraw()
			elif tiro_posy>=625-35 and tiro_posy<625+55 and tiro_posx>1180-35 and tiro_posx<1180+35 and tanque_hp_2>0:
				tanque_hp_2-=1
				cont_tiro=0
				tiro_esq=0
				tiro.undraw()
		if len(teclado)>0 and "space" in teclado and lado==2 and tiro_dir==0 and tiro_esq==0:
			tiro_dir=1
			tiro=atirar_jogador()
			tiro.draw(tela)
		if tiro_dir==1:
			tiro.move(8,0)
			cont_tiro+=1
			tiro_pos=tiro.getCenter()
			tiro_posx=tiro_pos.getX()
			tiro_posy=tiro_pos.getY()
			if cont_tiro==75:
				cont_tiro=0
				tiro_dir=0
				tiro.undraw()
			elif tiro_posy>=625-35 and tiro_posy<625+55 and tiro_posx>250-35 and tiro_posx<250+35 and dummy_hp>0:
				dummy_hp-=1
				dummy.undraw()
				cont_tiro=0
				tiro_dir=0
				tiro.undraw()
			elif tiro_posy>=625-35 and tiro_posy<625+55 and tiro_posx>800-35 and tiro_posx<800+35 and tanque_hp>0:
				tanque_hp-=1
				cont_tiro=0
				tiro_dir=0
				tiro.undraw()
			elif tiro_posy>=625-35 and tiro_posy<625+55 and tiro_posx>1180-35 and tiro_posx<1180+35 and tanque_hp_2>0:
				tanque_hp_2-=1
				cont_tiro=0
				tiro_dir=0
				tiro.undraw()
		if pulo==1:
			jogador.move(0,-4)
			cont+=1
			if cont==40:
				cont=0
				pulo=0
		elif posy<670:
			jogador.move(0,5)
		if posx>320 and posx<400 and posy>660:
			jogador.move(0,5)
		if posx>630 and posx<700 and posy>660:
			jogador.move(0,5)
		if posx>990 and posx<1090 and posy>660:
			jogador.move(0,5)
		if tanque_hp>0:
			tanque_cont+=1
		if tanque_hp<1:
			tanque.undraw()
		if tanque_hp_2>0:
			tanque_cont_2+=2
		if tanque_hp_2<1:
			tanque_2.undraw()
		if posx>220 and posx<250 and posy>580 and dummy_hp>0:
			hp-=3
			vida_3.undraw()
		elif posy>720 or hp<1:
			vida_1.undraw()
			jogador.undraw()
			fim=Text(Point(640,400),"GAME OVER")
			fim.setSize(36)
			fim.setTextColor("red")
			fim.setStyle("bold italic")
			menu=Text(Point(640,300),"Clique aqui para voltar ao menu")
			menu.setSize(30)
			menu.setTextColor("white")
			menu.setStyle("bold")
			fim.draw(tela)
			menu.draw(tela)
			if hp==3:
				vida_3.undraw()
			if hp==2:
				vida_2.undraw()
			if hp==1:
				vida_1.undraw()
			tela.getMouse()
			bola.undraw()
			dummy.undraw()
			tanque.undraw()
			tanque_2.undraw()
			fundo_2.undraw()
			fundo_0.draw(tela)
			fim.undraw()
			menu.undraw()
			cena=0
		if posx>1280 and dummy_hp<1 and tanque_hp<1 and tanque_hp_2<1:
			jogador.undraw()
			fundo_3.draw(tela)
			fundo_2.undraw()
			jogador.draw(tela)
			boss_atir_esq.draw(tela)
			boss_atir_esq_2.draw(tela)
			bola.undraw()
			bola.draw(tela)
			if hp==3:
				vida_3.undraw()
				vida_3.draw(tela)
			if hp==2:
				vida_2.undraw()
				vida_2.draw(tela)
			if hp==1:
				vida_1.undraw()
				vida_1.draw(tela)
			jogador.move(-1270,0)
			cena=3
	if cena==3:
		posi=jogador.getCenter()
		posx=posi.getX()
		posy=posi.getY()
		boss_posi=boss_atir_esq.getAnchor()
		boss_posx=boss_posi.getX()
		boss_posy=boss_posi.getY()
		boss_posi_2=boss_atir_esq_2.getAnchor()
		boss_posx_2=boss_posi_2.getX()
		boss_posy_2=boss_posi_2.getY()
		if boss_esc_cont==150 and boss_hp>0:
			boss_atir_esq.undraw()
			boss_esc_esq.draw(tela)
			boss_def=1
		if boss_def==1:
			boss_tiro_cont=0
			esc_cont+=1
			if esc_cont==150:
				boss_esc_esq.undraw()
				boss_atir_esq.draw(tela)
				boss_esc_cont=0
				boss_def=0
				esc_cont=0
		if boss_tiro_cont==50 and boss_hp>0:
			boss_tiro=1
			tiro_boss=atirar_boss()
			tiro_boss.draw(tela)
		if boss_tiro==1:
			tiro_boss.move(-10,0)
			cont_boss+=1
			tiro_pos_boss=tiro_boss.getAnchor()
			tiro_posx_boss=tiro_pos_boss.getX()
			tiro_posy_boss=tiro_pos_boss.getY()
			if cont_boss==75:
				cont_boss=0
				boss_tiro=0
				tiro_boss.undraw()
				boss_tiro_cont=0
			elif tiro_posy_boss>=posy-30 and tiro_posy_boss<posy+30 and tiro_posx_boss>posx-30 and tiro_posx_boss<posx+30:
				hp-=1
				cont_boss=0
				boss_tiro=0
				tiro_boss.undraw()
				boss_tiro_cont=0
		if boss_esc_cont_2==150 and boss_hp_2>0:
			boss_atir_esq_2.undraw()
			boss_esc_esq_2.draw(tela)
			boss_def_2=1
		if boss_def_2==1:
			boss_tiro_cont_2=0
			esc_cont_2+=1
			if esc_cont_2==150:
				boss_esc_esq_2.undraw()
				boss_atir_esq_2.draw(tela)
				boss_esc_cont_2=0
				boss_def_2=0
				esc_cont_2=0
		if boss_tiro_cont_2==100 and boss_hp_2>0:
			boss_tiro_2=1
			tiro_boss_2=atirar_boss_2()
			tiro_boss_2.draw(tela)
		if boss_tiro_2==1:
			tiro_boss_2.move(-10,0)
			cont_boss_2+=1
			tiro_pos_boss_2=tiro_boss_2.getAnchor()
			tiro_posx_boss_2=tiro_pos_boss_2.getX()
			tiro_posy_boss_2=tiro_pos_boss_2.getY()
			if cont_boss_2==75:
				cont_boss_2=0
				boss_tiro_2=0
				tiro_boss_2.undraw()
				boss_tiro_cont_2=0
			elif tiro_posy_boss_2>=posy-30 and tiro_posy_boss_2<posy+30 and tiro_posx_boss_2>posx-30 and tiro_posx_boss_2<posx+30:
				hp-=1
				cont_boss_2=0
				boss_tiro_2=0
				tiro_boss_2.undraw()
				boss_tiro_cont_2=0
		print(teclado)
		print(posx,posy)
		if len(teclado)>0 and "Left" in teclado and posx>0:
			if posx>990	and posx<1000 and posy>470 and posy<540:
				jogador.move(0,0)
			elif posx>730 and posx<740 and posy<620 and posy>550:
				jogador.move(0,0)
			elif "Shift_L" in teclado:
				jogador.move(-10,0)
			else:
				jogador.move(-5,0)
			lado=1
		if len(teclado)>0 and "Right" in teclado:
			if posx>1120 and posx<1180 and posy>310 and posy<370:
				jogador.move(0,0)
			elif posx>1000 and posx<1010 and posy>380 and posy<450:
				jogador.move(0,0)
			elif posx>775 and posx<785 and posy>470 and posy<540:
				jogador.move(0,0)
			elif posx>420 and posx<450 and posy<620 and posy>550:
				jogador.move(0,0)
			elif posx>1180 and posy>255:
				jogador.move(0,0)
			elif "Shift_L" in teclado:
				jogador.move(10,0)
			elif posx<1290:
				jogador.move(5,0)
			lado=2
		if len(teclado)>0 and "Up" in teclado and pulo==0:
			if posx>1200 and posy<260 and posy>250:
				pulo=1
			elif posx>1140 and posx<1190 and posy>300 and posy<310:
				pulo=1
			elif posx>780 and posx<995 and posy<475 and posy>465:
				pulo=1
			elif posx>1020 and posx<1130 and posy<385 and posy>375:
				pulo=1
			elif posx>430 and posx<730 and posy>540 and posy<550:
				pulo=1
			elif posy>660:
				pulo=1
		if len(teclado)>0 and "space" in teclado and lado==1 and tiro_esq==0 and tiro_dir==0:
			tiro_esq=1
			tiro=atirar_jogador()
			tiro.draw(tela)
		if tiro_esq==1:
			tiro.move(-8,0)
			cont_tiro+=1
			tiro_pos=tiro.getCenter()
			tiro_posx=tiro_pos.getX()
			tiro_posy=tiro_pos.getY()
			if cont_tiro==75:
				cont_tiro=0
				tiro_esq=0
				tiro.undraw()
			elif tiro_posy>=boss_posy-30 and tiro_posy<boss_posy+30 and tiro_posx>boss_posx-30 and tiro_posx<boss_posx+30 and boss_def==0:
				boss_hp-=1
				cont_tiro=0
				tiro_esq=0
				tiro.undraw()
			elif tiro_posy>=boss_posy_2-30 and tiro_posy<boss_posy_2+30 and tiro_posx>boss_posx_2-30 and tiro_posx<boss_posx_2+30 and boss_def_2==0:
				boss_hp_2-=1
				cont_tiro=0
				tiro_esq=0
				tiro.undraw()
		if len(teclado)>0 and "space" in teclado and lado==2 and tiro_dir==0 and tiro_esq==0:
			tiro_dir=1
			tiro=atirar_jogador()
			tiro.draw(tela)
		if tiro_dir==1:
			tiro.move(8,0)
			cont_tiro+=1
			tiro_pos=tiro.getCenter()
			tiro_posx=tiro_pos.getX()
			tiro_posy=tiro_pos.getY()
			if cont_tiro==75:
				cont_tiro=0
				tiro_dir=0
				tiro.undraw()
			elif tiro_posy>=boss_posy-30 and tiro_posy<boss_posy+30 and tiro_posx>boss_posx-30 and tiro_posx<boss_posx+30 and boss_def==0:
				boss_hp-=1
				cont_tiro=0
				tiro_dir=0
				tiro.undraw()
			elif tiro_posy>=boss_posy_2-30 and tiro_posy<boss_posy_2+30 and tiro_posx>boss_posx_2-30 and tiro_posx<boss_posx_2+30 and boss_def_2==0:
				boss_hp_2-=1
				cont_tiro=0
				tiro_esq=0
				tiro.undraw()
		if pulo==1:
			if cont>40:
				cont=0
				pulo=0
			elif posx>780 and posx<995 and posy>560 and posy<565:
				jogador.move(0,0)
				cont+=2
			elif posx>430 and posx<730 and posy<620 and posy>615:
				jogador.move(0,0)
				cont+=3
			else:
				jogador.move(0,-4)
			cont+=1
		elif posy<670:
			if posx>1180 and posy<260 and posy>250:
				jogador.move(0,0)
			elif posx>1140 and posx<1190 and posy>300 and posy<310:
				jogador.move(0,0)
			elif posx>1020 and posy<385 and posy>375:
				jogador.move(0,0)
			elif posx>780 and posx<995 and posy<475 and posy>465:
				jogador.move(0,0)
			elif posx>430 and posx<730 and posy>540 and posy<560:
				jogador.move(0,0)
			else:
				jogador.move(0,5)
		if boss_hp!=0:
			boss_tiro_cont+=1
			boss_esc_cont+=2
		if boss_hp_2!=0:
			boss_tiro_cont_2+=2
			boss_esc_cont_2+=1
		if boss_hp==0:
			boss_atir_esq.undraw()
		if boss_hp_2==0:
			boss_atir_esq_2.undraw()
		if hp==3 and atual==3:
			vida_3.draw(tela)
			atual=2
		if hp==2 and atual==2:
			vida_3.undraw()
			vida_2.draw(tela)
			atual=1
		if hp==1 and atual==1:
			vida_2.undraw()
			vida_1.draw(tela)
			atual=0
		if hp<1:
			jogador.undraw()
			fim=Text(Point(640,400),"GAME OVER")
			fim.setSize(36)
			fim.setTextColor("red")
			fim.setStyle("bold italic")
			menu=Text(Point(640,300),"Clique aqui para voltar ao menu")
			menu.setSize(30)
			menu.setTextColor("white")
			menu.setStyle("bold")
			fim.draw(tela)
			menu.draw(tela)
			vida_1.undraw()
			tela.getMouse()
			bola.undraw()
			boss_atir_esq.undraw()
			boss_atir_esq_2.undraw()
			if boss_esc_cont==1:
				boss_esc_esq.undraw()
			if boss_esc_cont_2==1:
				boss_esc_esq_2.undraw()
			fundo_0.draw(tela)
			fundo_3.undraw()
			fim.undraw()
			menu.undraw()
			cena=0
		if posx>1280 and boss_hp<1:
			jogador.undraw()
			fundo_4.draw(tela)
			fundo_3.undraw()
			jogador.draw(tela)
			bola.undraw()
			bola.draw(tela)
			if hp==3:
				vida_3.undraw()
				vida_3.draw(tela)
			if hp==2:
				vida_2.undraw()
				vida_2.draw(tela)
			if hp==1:
				vida_1.undraw()
				vida_1.draw(tela)
			bateria.draw(tela)
			turret_dir.draw(tela)
			turret_esq.draw(tela)
			jogador.move(-1280,0)
			cena=4
		if hp==3 and atual==3:
			vida_3.undraw()
			vida_3.draw(tela)
			atual=2
		if hp==2 and atual==2:
			vida_3.undraw()
			vida_2.draw(tela)
			atual=1
		if hp==1 and atual==1:
			vida_2.undraw()
			vida_1.draw(tela)
			atual=0
	if cena==4:
		posi=jogador.getCenter()
		posx=posi.getX()
		posy=posi.getY()
		print(teclado)
		print(posx,posy)
		if cont_tiro_turret_dir==40:
			atira_turret_dir=1
			tiro_turret_dir_im=atirar_turret_dir()
			tiro_turret_dir_im.draw(tela)
		if atira_turret_dir==1:
			cont_tiro_turret_dir=0
			tiro_turret_dir_im.move(10,0)
			cont_tiro_inst_turret_dir+=1
			tiro_pos_turret_dir=tiro_turret_dir_im.getAnchor()
			tiro_posx_turret_dir=tiro_pos_turret_dir.getX()
			tiro_posy_turret_dir=tiro_pos_turret_dir.getY()
			if cont_tiro_inst_turret_dir==75:
				cont_tiro_inst_turret_dir=0
				atira_turret_dir=0
				tiro_turret_dir_im.undraw()
			elif tiro_posy_turret_dir>posy-25 and tiro_posy_turret_dir<posy+25 and tiro_posx_turret_dir>posx-25 and tiro_posx_turret_dir<posx+25:
				hp-=1
				cont_tiro_inst_turret_dir=0
				atira_turret_dir=0
				tiro_turret_dir_im.undraw()
		if cont_tiro_turret_esq==40:
			atira_turret_esq=1
			tiro_turret_esq_im=atirar_turret_esq()
			tiro_turret_esq_im.draw(tela)
		if atira_turret_esq==1:
			cont_tiro_turret_esq=0
			tiro_turret_esq_im.move(-10,0)
			cont_tiro_inst_turret_esq+=1
			tiro_pos_turret_esq=tiro_turret_esq_im.getAnchor()
			tiro_posx_turret_esq=tiro_pos_turret_esq.getX()
			tiro_posy_turret_esq=tiro_pos_turret_esq.getY()
			if cont_tiro_inst_turret_esq==75:
				cont_tiro_inst_turret_esq=0
				atira_turret_esq=0
				tiro_turret_esq_im.undraw()
			elif tiro_posy_turret_esq>posy-25 and tiro_posy_turret_esq<posy+25 and tiro_posx_turret_esq>posx-25 and tiro_posx_turret_esq<posx+25:
				hp-=1
				cont_tiro_inst_turret_esq=0
				atira_turret_esq=0
				tiro_turret_esq_im.undraw()
		if posx>270 and posx<320 and posy>520 and posy<640 and bat==1:
			bateria.undraw()
			bat=0
			if hp!=3:
				if hp==2:
					vida_2.undraw()
				if hp==1:
					vida_1.undraw()
				vida_3.draw(tela)
				hp=3
				atual=2
		if hp==3 and atual==3:
			vida_3.draw(tela)
			atual=2
		if hp==2 and atual==2:
			vida_3.undraw()
			vida_2.draw(tela)
			atual=1
		if hp==1 and atual==1:
			vida_2.undraw()
			vida_1.draw(tela)
			atual=0
		if len(teclado)>0 and "Left" in teclado and posx>0:
			if posx<880 and posx>870 and posy<415 and posy>340:
				jogador.move(0,0)
			elif posx>145 and posx<155 and posy<350 and posy>270:
				jogador.move(0,0)
			elif "Shift_L" in teclado:
				jogador.move(-10,0)
			else:
				jogador.move(-5,0)
			lado=1
		if len(teclado)>0 and "Right" in teclado:
			if posx>595 and posx<605 and posy<565 and posy>460:
				jogador.move(0,0)
			elif posx>1180 and posy<560:
				jogador.move(0,0)
			elif "Shift_L" in teclado:
				jogador.move(10,0)
			else:
				jogador.move(5,0)
			lado=2
		if len(teclado)>0 and "Up" in teclado and pulo==0:
			if posx>600 and posy<500 and posy>490:
				pulo=1
			elif posx>-5 and posx<150 and posy<260 and posy>250:
				pulo=1
			elif posx>-5 and posx<865 and posy<350 and posy>340:
				pulo=1
			elif posy>660 and posx>440:
				pulo=1
			else:
				pulo=0
		if len(teclado)>0 and "space" in teclado and lado==1 and tiro_esq==0 and tiro_dir==0:
			tiro_esq=1
			tiro=atirar_jogador()
			tiro.draw(tela)
		if tiro_esq==1:
			tiro.move(-8,0)
			cont_tiro+=1
			if cont_tiro==75:
				cont_tiro=0
				tiro_esq=0
				tiro.undraw()
		if len(teclado)>0 and "space" in teclado and lado==2 and tiro_dir==0 and tiro_esq==0:
			tiro_dir=1
			tiro=atirar_jogador()
			tiro.draw(tela)
		if tiro_dir==1:
			tiro.move(8,0)
			cont_tiro+=1
			if cont_tiro==75:
				cont_tiro=0
				tiro_dir=0
				tiro.undraw()
		if pulo==1:
			if cont>40:
				cont=0
				pulo=0
			elif posx<865 and posy>405 and posy<415:
				jogador.move(0,0)
				cont+=2
			elif posx>600 and posy>560 and posy<565:
				jogador.move(0,0)
				cont+=2
			else:
				jogador.move(0,-4)
			cont+=1
		if posy<670 and pulo!=1:
			if posx>600 and posy<500 and posy>490:
				jogador.move(0,0)
			elif posx>-5 and posx<150 and posy<260 and posy>250:
				jogador.move(0,0)
			elif posx>-5 and posx<865 and posy<350 and posy>340:
				jogador.move(0,0)
			else:
				jogador.move(0,5)
		elif posy>660 and posx<450 and pulo!=1:
			jogador.move(0,5)
		cont_tiro_turret_dir+=1
		cont_tiro_turret_esq+=1
		if posy>720 or hp<1:
			jogador.undraw()
			fim=Text(Point(640,400),"GAME OVER")
			fim.setSize(36)
			fim.setTextColor("red")
			fim.setStyle("bold italic")
			menu=Text(Point(640,300),"Clique aqui para voltar ao menu")
			menu.setSize(30)
			menu.setTextColor("white")
			menu.setStyle("bold")
			fim.draw(tela)
			menu.draw(tela)
			if hp==3:
				vida_3.undraw()
			if hp==2:
				vida_2.undraw()
			if hp==1 or hp==0:
				vida_1.undraw()
			tela.getMouse()
			bola.undraw()
			fundo_0.draw(tela)
			if bat==1:
				bateria.undraw()
			turret_esq.undraw()
			turret_dir.undraw()
			fim.undraw()
			menu.undraw()
			fundo_4.undraw()
			cena=0
		if posx>1280:
			jogador.undraw()
			turret_esq.undraw()
			turret_dir.undraw()
			fundo_5.draw(tela)
			fundo_4.undraw()
			jogador.draw(tela)
			jogador.move(-1270,0)
			bola.undraw()
			bola.draw(tela)
			if hp==4:
				vida_4.undraw()
				vida_4.draw(tela)
			if hp==3:
				vida_3.undraw()
				vida_3.draw(tela)
			if hp==2:
				vida_2.undraw()
				vida_2.draw(tela)
			if hp==1:
				vida_1.undraw()
				vida_1.draw(tela)
			andador.draw(tela)
			bola_2.draw(tela)
			vida_10_2.draw(tela)
			cena=5
	if cena==5:
		posi=jogador.getCenter()
		posx=posi.getX()
		posy=posi.getY()
		print(teclado)
		print(posx,posy)
		if len(teclado)>0 and "Left" in teclado and posx>10:
			if posx>235 and posx<465 and posy>555 and posy<625:
				jogador.move(0,0)
			elif "Shift_L" in teclado:
				jogador.move(-10,0)
				lado=1
			else:
				jogador.move(-5,0)
				lado=1
		if len(teclado)>0 and "Right" in teclado:
			if posx>235 and posx<465 and posy>555 and posy<625:
				jogador.move(0,0)
			elif "Shift_L" in teclado:
				jogador.move(10,0)
				lado=2
			else:
				jogador.move(5,0)
				lado=2
		if len(teclado)>0 and "Up" in teclado and pulo==0:
			if posx>235 and posx<465 and posy>550 and posy<560:
				pulo=1
			elif posy>660:
				pulo=1
			print(pulo)
		if len(teclado)>0 and "space" in teclado and lado==1 and tiro_esq==0 and tiro_dir==0:
			tiro_esq=1
			tiro=atirar_jogador()
			tiro.draw(tela)
		if tiro_esq==1:
			tiro.move(-8,0)
			cont_tiro+=1
			if cont_tiro==75:
				cont_tiro=0
				tiro_esq=0
				tiro.undraw()
		if len(teclado)>0 and "space" in teclado and lado==2 and tiro_dir==0 and tiro_esq==0:
			tiro_dir=1
			tiro=atirar_jogador()
			tiro.draw(tela)
		if tiro_dir==1:
			tiro.move(8,0)
			cont_tiro+=1
			tiro_pos=tiro.getCenter()
			tiro_posx=tiro_pos.getX()
			tiro_posy=tiro_pos.getY()
			if cont_tiro==75:
				cont_tiro=0
				tiro_dir=0
				tiro.undraw()
			elif tiro_posy>400 and tiro_posy<500 and tiro_posx>800 and tiro_posx<1280:
				andador_hp-=1
				if andador_hp==0:
					vida_1_2.undraw()
				if andador_hp==1:
					vida_2_2.undraw()
					vida_1_2.draw(tela)
				if andador_hp==2:
					vida_3_2.undraw()
					vida_2_2.draw(tela)
				if andador_hp==3:
					vida_4_2.undraw()
					vida_3_2.draw(tela)
				if andador_hp==4:
					vida_5_2.undraw()
					vida_4_2.draw(tela)
				if andador_hp==5:
					vida_6_2.undraw()
					vida_5_2.draw(tela)
				if andador_hp==6:
					vida_7_2.undraw()
					vida_6_2.draw(tela)
				if andador_hp==7:
					vida_8_2.undraw()
					vida_7_2.draw(tela)
				if andador_hp==8:
					vida_9_2.undraw()
					vida_8_2.draw(tela)
				if andador_hp==9:
					vida_10_2.undraw()
					vida_9_2.draw(tela)
				cont_tiro=0
				tiro_dir=0
				tiro.undraw()
		if pulo==1:
			if cont>40:
				cont=0
				pulo=0
			elif posx>235 and posx<465 and posy>620 and posy<630:
				jogador.move(0,0)
				cont+=3
			else:
				jogador.move(0,-4)
			cont+=1
		elif posy<670:
			if posx>235 and posx<465 and posy>550 and posy<560:
				jogador.move(0,0)
			else:
				jogador.move(0,5)
		if andador_hp>0:
			cont_tiro_andador+=1
			cont_onda_andador+=1
		if cont_tiro_andador==150:
			atira_andador=1
			tiro_andador=atirar_andador()
			tiro_andador.draw(tela)
		if atira_andador==1:
			cont_tiro_andador=0
			tiro_andador.move(-7,0)
			cont_tiro_inst_andador+=1
			tiro_pos_andador=tiro_andador.getCenter()
			tiro_posx_andador=tiro_pos_andador.getX()
			tiro_posy_andador=tiro_pos_andador.getY()
			if cont_tiro_inst_andador==100:
				cont_tiro_andador=0
				atira_andador=0
				cont_tiro_inst_andador=0
				tiro_andador.undraw()
			elif tiro_posy_andador>posy-150 and tiro_posy_andador<posy+150 and tiro_posx_andador>posx-100 and tiro_posx_andador<posx+100:
				if hp==1:
					hp=0
					vida_1.undraw()
				if hp==2:
					hp=1
					vida_2.undraw()
					vida_1.draw(tela)
					tiro_andador.undraw()
				if hp==3:
					hp=2
					vida_3.undraw()
					vida_2.draw(tela)
					tiro_andador.undraw()
				if hp==4:
					hp=3
					vida_4.undraw()
					vida_3.draw(tela)
					tiro_andador.undraw()
				cont_tiro_andador=0
				atira_andador=0
				cont_tiro_inst_andador=0
		if hp<1:
			jogador.undraw()
			fim=Text(Point(640,400),"GAME OVER")
			fim.setSize(36)
			fim.setTextColor("black")
			fim.setStyle("bold italic")
			menu=Text(Point(640,300),"Clique aqui para voltar ao menu")
			menu.setSize(30)
			menu.setTextColor("white")
			menu.setStyle("bold")
			fim.draw(tela)
			menu.draw(tela)
			vida_1.undraw()
			tela.getMouse()
			if andador_hp==10:
				vida_10_2.undraw()
			if andador_hp==9:
				vida_9_2.undraw()
			if andador_hp==8:
				vida_8_2.undraw()
			if andador_hp==7:
				vida_7_2.undraw()
			if andador_hp==6:
				vida_6_2.undraw()
			if andador_hp==5:
				vida_5_2.undraw()
			if andador_hp==4:
				vida_4_2.undraw()
			if andador_hp==3:
				vida_3_2.undraw()
			if andador_hp==2:
				vida_2_2.undraw()
			if andador_hp==1:
				vida_1_2.undraw()
			tiro_andador.undraw()
			fundo_0.draw(tela)
			andador.undraw()
			fim.undraw()
			menu.undraw()
			fundo_5.undraw()
			cena=0
		if andador_hp<1:
			andador.undraw()
			fim=Text(Point(640,400),"MESTRE ROBO DERROTADO, PARABENS!")
			fim.setSize(36)
			fim.setTextColor("yellow")
			fim.setStyle("bold italic")
			menu=Text(Point(640,300),"Clique aqui para voltar ao menu")
			menu.setSize(30)
			menu.setTextColor("grey")
			menu.setStyle("bold")
			fim.draw(tela)
			menu.draw(tela)
			tela.getMouse()
			bola.undraw()
			bola_2.undraw()
			if hp==4:
				vida_4.undraw()
			if hp==3:
				vida_3.undraw()
			if hp==2:
				vida_2.undraw()
			if hp==1:
				vida_1.undraw()
			tiro_andador.undraw()
			fundo_0.draw(tela)
			andador.undraw()
			fim.undraw()
			menu.undraw()
			fundo_5.undraw()
			cena=0
	if cena==6:
		posi=jogador.getCenter()
		posx=posi.getX()
		posy=posi.getY()
		print(teclado)
		print(posx,posy)
		if len(teclado)>0 and "Left" in teclado and posx>0:
			if posx>990	and posx<1000 and posy>470 and posy<540:
				jogador.move(0,0)
			elif posx>730 and posx<740 and posy<620 and posy>550:
				jogador.move(0,0)
			elif "Shift_L" in teclado:
				jogador.move(-10,0)
			else:
				jogador.move(-5,0)
			lado=1
		if len(teclado)>0 and "Right" in teclado and posx<1280:
			if posx>1120 and posx<1180 and posy>310 and posy<370:
				jogador.move(0,0)
			elif posx>1000 and posx<1010 and posy>380 and posy<450:
				jogador.move(0,0)
			elif posx>775 and posx<785 and posy>470 and posy<540:
				jogador.move(0,0)
			elif posx>420 and posx<450 and posy<620 and posy>550:
				jogador.move(0,0)
			elif posx>1180 and posy>255:
				jogador.move(0,0)
			elif "Shift_L" in teclado:
				jogador.move(10,0)
			else:
				jogador.move(5,0)
			lado=2
		if len(teclado)>0 and "Up" in teclado and pulo==0:
			if posx>1200 and posy<260 and posy>250:
				pulo=1
			elif posx>1140 and posx<1190 and posy>300 and posy<310:
				pulo=1
			elif posx>780 and posx<995 and posy<475 and posy>465:
				pulo=1
			elif posx>1020 and posx<1130 and posy<385 and posy>375:
				pulo=1
			elif posx>430 and posx<730 and posy>540 and posy<550:
				pulo=1
			elif posy>660:
				pulo=1
		if len(teclado)>0 and "Shift_R" in teclado and lado==1 and tiro_esq==0 and tiro_dir==0:
			tiro_esq=1
			tiro=atirar_jogador()
			tiro.draw(tela)
		if tiro_esq==1:
			tiro.move(-8,0)
			cont_tiro+=1
			tiro_pos=tiro.getCenter()
			tiro_posx=tiro_pos.getX()
			tiro_posy=tiro_pos.getY()
			if cont_tiro==75:
				cont_tiro=0
				tiro_esq=0
				tiro.undraw()
			elif tiro_posy>=posy_2-35 and tiro_posy<posy_2+35 and tiro_posx>posx_2-35 and tiro_posx<posx_2+35:
				hp_2-=1
				tiro_esq=0
				cont_tiro=0
				tiro.undraw()
		if len(teclado)>0 and "Shift_R" in teclado and lado==2 and tiro_dir==0 and tiro_esq==0:
			tiro_dir=1
			tiro=atirar_jogador()
			tiro.draw(tela)
		if tiro_dir==1:
			tiro.move(8,0)
			cont_tiro+=1
			tiro_pos=tiro.getCenter()
			tiro_posx=tiro_pos.getX()
			tiro_posy=tiro_pos.getY()
			if cont_tiro==75:
				cont_tiro=0
				tiro_dir=0
				tiro.undraw()
			elif tiro_posy>=posy_2-35 and tiro_posy<posy_2+35 and tiro_posx>posx_2-35 and tiro_posx<posx_2+35:
				hp_2-=1
				tiro_dir=0
				cont_tiro=0
				tiro.undraw()
		if pulo==1:
			if cont>40:
				cont=0
				pulo=0
			elif posx>780 and posx<995 and posy>560 and posy<565:
				jogador.move(0,0)
				cont+=2
			elif posx>430 and posx<730 and posy<620 and posy>615:
				jogador.move(0,0)
				cont+=3
			else:
				jogador.move(0,-4)
			cont+=1
		elif posy<670:
			if posx>1180 and posy<260 and posy>250:
				jogador.move(0,0)
			elif posx>1140 and posx<1190 and posy>300 and posy<310:
				jogador.move(0,0)
			elif posx>1020 and posy<385 and posy>375:
				jogador.move(0,0)
			elif posx>780 and posx<995 and posy<475 and posy>465:
				jogador.move(0,0)
			elif posx>430 and posx<730 and posy>540 and posy<560:
				jogador.move(0,0)
			else:
				jogador.move(0,5)
		if hp==3 and atual==3:
			atual=2
		if hp==2 and atual==2:
			vida_3.undraw()
			vida_2.draw(tela)
			atual=1
		if hp==1 and atual==1:
			vida_2.undraw()
			vida_1.draw(tela)
			atual=0
		if hp==0:
			bola.undraw()
			vida_1.undraw()
			jogador.undraw()
			instru_m.undraw()
			instru_t.undraw()
			instru_m_2.undraw()
			instru_t_2.undraw()
			fim=Text(Point(640,100),">VERMELHO VENCEU<")
			fim.setSize(36)
			fim.setTextColor("red")
			menu=Text(Point(640,300),"Clique aqui para voltar ao menu")
			menu.setSize(30)
			menu.setTextColor("white")
			menu.setStyle("bold")
			fim.draw(tela)
			menu.draw(tela)
			tela.getMouse()
			jogador_2.undraw()
			bola_2.undraw()
			if hp_2==3:
				vida_3_2.undraw()
			if hp_2==2:
				vida_2_2.undraw()
			if hp_2==1:
				vida_1_2.undraw()
			fundo_3.undraw()
			fim.undraw()
			menu.undraw()
			if tiro_esq!=0 or tiro_dir!=0:
				tiro.undraw()
			cena=0
		############JOGADOR_2############
		posi_2=jogador_2.getCenter()
		posx_2=posi_2.getX()
		posy_2=posi_2.getY()
		if len(teclado)>0 and "a" in teclado and posx_2>0:
			if posx_2>990	and posx_2<1000 and posy_2>470 and posy_2<540:
				jogador_2.move(0,0)
			elif posx_2>730 and posx_2<740 and posy_2<620 and posy_2>550:
				jogador_2.move(0,0)
			elif "Shift_L" in teclado:
				jogador_2.move(-10,0)
			else:
				jogador_2.move(-5,0)
			lado_2=1
		if len(teclado)>0 and "d" in teclado and posx_2<1280:
			if posx_2>1120 and posx_2<1180 and posy_2>310 and posy_2<370:
				jogador_2.move(0,0)
			elif posx_2>1000 and posx_2<1010 and posy_2>380 and posy_2<450:
				jogador_2.move(0,0)
			elif posx_2>775 and posx_2<785 and posy_2>470 and posy_2<540:
				jogador_2.move(0,0)
			elif posx_2>420 and posx_2<450 and posy_2<620 and posy_2>550:
				jogador_2.move(0,0)
			elif posx_2>1180 and posy_2>255:
				jogador_2.move(0,0)
			elif "Shift_L" in teclado:
				jogador_2.move(10,0)
			else:
				jogador_2.move(5,0)
			lado_2=2
		if len(teclado)>0 and "w" in teclado and pulo_2==0:
			if posx_2>1200 and posy_2<260 and posy_2>250:
				pulo_2=1
			elif posx_2>1140 and posx_2<1190 and posy_2>300 and posy_2<310:
				pulo_2=1
			elif posx_2>780 and posx_2<995 and posy_2<475 and posy_2>465:
				pulo_2=1
			elif posx_2>1020 and posx_2<1130 and posy_2<385 and posy_2>375:
				pulo_2=1
			elif posx_2>430 and posx_2<730 and posy_2>540 and posy_2<550:
				pulo_2=1
			elif posy_2>660:
				pulo_2=1
		if len(teclado)>0 and "space" in teclado and lado_2==1 and tiro_esq_2==0 and tiro_dir_2==0:
			tiro_esq_2=1
			tiro_2=atirar_jogador_2()
			tiro_2.draw(tela)
		if tiro_esq_2==1:
			tiro_2.move(-8,0)
			cont_tiro_2+=1
			tiro_pos_2=tiro_2.getCenter()
			tiro_posx_2=tiro_pos_2.getX()
			tiro_posy_2=tiro_pos_2.getY()
			if cont_tiro_2==75:
				cont_tiro_2=0
				tiro_esq_2=0
				tiro_2.undraw()
			elif tiro_posy_2>=posy-35 and tiro_posy_2<posy+35 and tiro_posx_2>posx-35 and tiro_posx_2<posx+35:
				hp-=1
				tiro_esq_2=0
				cont_tiro_2=0
				tiro_2.undraw()
		if len(teclado)>0 and "space" in teclado and lado_2==2 and tiro_dir_2==0 and tiro_esq_2==0:
			tiro_dir_2=1
			tiro_2=atirar_jogador_2()
			tiro_2.draw(tela)
		if tiro_dir_2==1:
			tiro_2.move(8,0)
			cont_tiro_2+=1
			tiro_pos_2=tiro_2.getCenter()
			tiro_posx_2=tiro_pos_2.getX()
			tiro_posy_2=tiro_pos_2.getY()
			if cont_tiro_2==75:
				cont_tiro_2=0
				tiro_dir_2=0
				tiro_2.undraw()
			elif tiro_posy_2>=posy-35 and tiro_posy_2<posy+35 and tiro_posx_2>posx-35 and tiro_posx_2<posx+35:
				hp-=1
				tiro_dir_2=0
				cont_tiro_2=0
				tiro_2.undraw()
		if pulo_2==1:
			if cont_2>40:
				cont_2=0
				pulo_2=0
			elif posx_2>780 and posx_2<995 and posy_2>560 and posy_2<565:
				jogador_2.move(0,0)
				cont_2+=2
			elif posx_2>430 and posx_2<730 and posy_2<620 and posy_2>615:
				jogador_2.move(0,0)
				cont_2+=3
			else:
				jogador_2.move(0,-4)
			cont_2+=1
		elif posy_2<670:
			if posx_2>1180 and posy_2<260 and posy_2>250:
				jogador_2.move(0,0)
			elif posx_2>1140 and posx_2<1190 and posy_2>300 and posy_2<310:
				jogador_2.move(0,0)
			elif posx_2>1020 and posy_2<385 and posy_2>375:
				jogador_2.move(0,0)
			elif posx_2>780 and posx_2<995 and posy_2<475 and posy_2>465:
				jogador_2.move(0,0)
			elif posx_2>430 and posx_2<730 and posy_2>540 and posy_2<560:
				jogador_2.move(0,0)
			else:
				jogador_2.move(0,5)
		if hp_2==3 and atual_2==3:
			vida_3_2.draw(tela)
			atual_2=2
		if hp_2==2 and atual_2==2:
			vida_3_2.undraw()
			vida_2_2.draw(tela)
			atual_2=1
		if hp_2==1 and atual_2==1:
			vida_2_2.undraw()
			vida_1_2.draw(tela)
			atual_2=0
		if hp_2==0:
			bola_2.undraw()
			vida_1_2.undraw()
			jogador_2.undraw()
			instru_m.undraw()
			instru_t.undraw()
			instru_m_2.undraw()
			instru_t_2.undraw()
			fim=Text(Point(640,100),">ROXO VENCEU<")
			fim.setSize(36)
			fim.setTextColor("purple")
			menu=Text(Point(640,300),"Clique aqui para voltar ao menu")
			menu.setSize(30)
			menu.setTextColor("white")
			menu.setStyle("bold")
			fim.draw(tela)
			menu.draw(tela)
			tela.getMouse()
			jogador.undraw()
			bola.undraw()
			if hp==3:
				vida_3.undraw()
			if hp==2:
				vida_2.undraw()
			if hp==1:
				vida_1.undraw()
			fundo_3.undraw()
			fim.undraw()
			menu.undraw()
			if tiro_esq_2!=0 or tiro_dir_2!=0:
				tiro_2.undraw()
			cena=0
	update()
	time.sleep(0.01)