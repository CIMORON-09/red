import wrap, random

wrap.add_sprite_dir("mayspraite")
wrap.world.create_world(1190, 804)
spisoktochhek = []
spisokkustov = []
spicok_sedeneh = []
schet = 0
prividenie = None
teleport_1 = wrap.sprite.add("battle_city_tanks", 52, 742, "tank_enemy_size1_purple1")
teleport_2 = wrap.sprite.add("battle_city_tanks",54,51, "tank_enemy_size1_purple1")
teleport_3 = wrap.sprite.add("battle_city_tanks",1138,55 ,"tank_enemy_size1_purple1")
teleport_4 = wrap.sprite.add("battle_city_tanks",1138,754 ,"tank_enemy_size1_purple1")


def postroy_stena_x(otkuda, dokuda, y):
    t = range(otkuda, dokuda, 1)
    u = [*t]
    for did in u:
        stroem_kust_po_kvadratnomu_kardenata(did, y)


def postroy_tochke(otkuda, dokuda, y):
    t = range(otkuda, dokuda, 1)
    u = [*t]
    for did in u:
        ppop = random.randint(1,100)
        if ppop <50:
            ctroem_tochku_po_kvadratnom_kaardenatam(did, y)


def postroy_stena_y(otkuda, dokuda, x):
    t = range(otkuda, dokuda, 1)
    u = [*t]
    for did in u:
        stroem_kust_po_kvadratnomu_kardenata(x, did)


def sosdaemkuste(x, y):
    kust1 = wrap.sprite.add("battle_city_items", x, y, "block_brick")

    wrap.sprite.set_size(kust1, 35, 35)

    spisokkustov.append(kust1)


def tochke(x, y):
    tochka = wrap.sprite.add("pppp", x, y, "krug")
    wrap.sprite.set_size(tochka, 15, 15)
    spisoktochhek.append(tochka)

    for did in spisokkustov:
        what = wrap.sprite.is_collide_sprite(did, tochka)
        if what == True:
            spisoktochhek.remove(tochka)
            wrap.sprite.remove(tochka)
            break


def edim_tochke(nomertocke):
    what = wrap.sprite.is_collide_sprite(pucman, nomertocke)

    if what == True:
        wrap.sprite.remove(nomertocke)
        spisoktochhek.remove(nomertocke)


def delaem_schetchik():
    global schet, prividenie

    for did in spisoktochhek:

        what = wrap.sprite.is_collide_sprite(pucman, did)
        if what == True:
            schet += 1

            wrap.sprite_text.set_text(id_scheta, str(schet))
            edim_tochke(did)

        if schet == 10 and prividenie == None:
            prividenie = wrap.sprite.add("pacman", 500, 400, "enemy_red_right1")

        # ???????? ????????????????????  ????????


@wrap.always(delay=10)
def siiuuuuu_seeeeeeeee():
    if prividenie != None:
        pacman_x = wrap.sprite.get_centerx(pucman)
        pacman_y = wrap.sprite.get_centery(pucman)
        wrap.sprite.move_at_angle_point(prividenie, pacman_x, pacman_y, 2)
        oo=wrap.sprite.is_collide_sprite(pucman,prividenie)
        if oo == True:
            wrap.sprite.add_text("GAME OVER",500,500, text_color=(0, 255, 6))
    eee=len(spisoktochhek)
    if eee==0 :
        wrap.sprite.add_text("YOU ARE WINER!",500,500, text_color=(0, 255, 6))





def teleporteruem_pucman ():


    teleport1=wrap.sprite.is_collide_sprite(pucman,teleport_1)
    teleport2=wrap.sprite.is_collide_sprite(pucman,teleport_2)
    teleport3=wrap.sprite.is_collide_sprite(pucman,teleport_3)
    teleport4=wrap.sprite.is_collide_sprite(pucman,teleport_4)





    mesto1=[51, 646]
    mesto2=[54,127]
    mesto3=[1135, 121]
    mesto4=[1137, 651]
    if  teleport1==True :
        choice_x = random.choice([mesto2,mesto3,mesto4])

        wrap.sprite.move_to(pucman,choice_x[0],choice_x[1])


    if   teleport2==True :

        choice_x=random.choice([mesto1,mesto3,mesto4])
        print(choice_x)


        wrap.sprite.move_to(pucman,choice_x[0],choice_x[1])


    if   teleport3==True :

        choice_x=random.choice([mesto1,mesto2,mesto4])
        print(choice_x)


        wrap.sprite.move_to(pucman,choice_x[0],choice_x[1])



    if   teleport4==True :

        choice_x=random.choice([mesto1,mesto2,mesto3])
        print(choice_x)


        wrap.sprite.move_to(pucman,choice_x[0],choice_x[1])



@wrap.on_mouse_move
def prrp(pos_x,pos_y):
    wrap.world.set_title(str(pos_x)+" "+str(pos_y))


def zactraevaem_pole_tochke(y):
    t = range(0, 35, 1)
    u = [*t]
    for did in u:
        ctroem_tochku_po_kvadratnom_kaardenatam(did, y)


def ctroem_tochku_po_kvadratnom_kaardenatam(x, y):
    tochke(17 + 35 * x, 17 + 35 * y)


def stroem_kust_po_kvadratnomu_kardenata(x, y):
    sosdaemkuste(17 + 35 * x, 17 + 35 * y)


def levl_1():
    # ??????????
    postroy_stena_x(0, 35, 0)
    postroy_stena_x(0, 35, 22)
    postroy_stena_y(0, 22, 0)
    postroy_stena_y(0, 22, 33)

    # ?????????????????? ?????????????????? ??????????
    postroy_stena_x(26, 32, 21)
    postroy_stena_x(26, 32, 1)
    postroy_stena_x(2, 8, 21)
    postroy_stena_x(2, 8, 1)

    # ?????????????? ???????????????? ???????? ?? ????????????
    postroy_stena_x(10, 22, 20)
    postroy_stena_x(10, 22, 2)

    # ???????????? ?????????????? ?????????? ?? ????????????

    postroy_stena_y(4, 18, 29.5)

    postroy_stena_y(4, 18, 3.5)

    postroy_stena_y(4, 18, 32)

    postroy_stena_y(4, 18, 1)
    # ?????? ???????????????????? ????!!!!

    postroy_stena_y(8, 14, 11.5)

    postroy_stena_y(8, 14, 19.5)

    postroy_stena_x(12, 15, 8)
    postroy_stena_x(17, 20, 8)
    postroy_stena_x(12, 20, 13)

    t = range(0, 23, 1)
    tyr = [*t]

    for did in tyr:
        postroy_tochke(1, 35, did)

    # ctroem_tochku_po_kvadratnom_kaardenatam(1,1)
    # zactraevaem_pole_tochke()


levl_1()
id_scheta = wrap.sprite.add_text("0", 275, 15, text_color=(0, 255, 6))

wrap.sprite.add_text("???????????????? ??????????", 150, 15, text_color=(0, 255, 6))

print(spisokkustov)

pucman = wrap.sprite.add("pacman", 450, 400, "player2")


@wrap.on_key_always(wrap.K_w, wrap.K_s, wrap.K_a, wrap.K_d)
def dvizhenie(keys):
    if wrap.K_w in keys:
        wrap.sprite.move(pucman, 0, -15)
        wrap.sprite.set_angle(pucman, 0)


    elif wrap.K_s in keys:
        wrap.sprite.move(pucman, 0, 15)

        wrap.sprite.set_angle(pucman, 180)

    elif wrap.K_a in keys:
        wrap.sprite.move(pucman, -15, 0)

        wrap.sprite.set_angle(pucman, 270)

    elif wrap.K_d in keys:
        wrap.sprite.move(pucman, 15, 0)

        wrap.sprite.set_angle(pucman, 90)

    for did in spisokkustov:
        dvizhenie_kist(did)

    delaem_schetchik()
    teleporteruem_pucman()

def dvizhenie_kist(nomerkusta):
    what = wrap.sprite.is_collide_sprite(pucman, nomerkusta)
    gradus = wrap.sprite.get_angle(pucman)

    if what == True and gradus == -90:
        pop = wrap.sprite.get_right(nomerkusta)

        wrap.sprite.move_left_to(pucman, pop + 1)

    if what == True and gradus == 90:
        pop = wrap.sprite.get_left(nomerkusta)

        wrap.sprite.move_right_to(pucman, pop - 1)

    if what == True and gradus == 0:
        pop = wrap.sprite.get_bottom(nomerkusta)

        wrap.sprite.move_top_to(pucman, pop + 1)

    if what == True and gradus == 180:
        pop = wrap.sprite.get_top(nomerkusta)

        wrap.sprite.move_bottom_to(pucman, pop - 1)


import wrap_py

wrap_py.app.start()
