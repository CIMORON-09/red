import wrap, random

wrap.add_sprite_dir("mayspraite")
wrap.world.create_world(1190, 804)
spisoktochhek = []
spisokkustov = []
spicok_sedeneh= []

def postroy_stena_x(otkuda, dokuda, y):
    t = range(otkuda, dokuda, 1)
    u = [*t]
    for did in u:
        stroem_kust_po_kvadratnomu_kardenata(did, y)


def postroy_tochke(otkuda, dokuda, y):
    t = range(otkuda, dokuda, 1)
    u = [*t]
    for did in u:
        ppop = random.randint(1, 100)
        if ppop > 50:
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
        what = wrap.sprite.is_collide_sprite(did,tochka)
        if what == True:
            spisoktochhek.remove(tochka)
            wrap.sprite.remove(tochka)
            break

def edim_tochke(nomertocke):

    what = wrap.sprite.is_collide_sprite(pucman,nomertocke)

    if what == True:
        wrap.sprite.remove(nomertocke)
        spisoktochhek.remove(nomertocke)



@wrap.always()
def delaem_schetchik():
    pop=0
    what = wrap.sprite.is_collide_sprite(pucman,spisoktochhek)
    if what == True  :
        pop+=1


    print(pop)

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
    postroy_stena_x(0, 35, 0)
    postroy_stena_x(0, 35, 22)
    postroy_stena_y(0, 22, 0)
    postroy_stena_y(0, 22, 33)
    postroy_stena_y(4, 18, 29.5)
    postroy_stena_y(4, 18, 3.5)
    postroy_stena_y(4, 18, 1)
    postroy_stena_y(4, 18, 32)
    postroy_stena_x(10, 22, 20)
    postroy_stena_x(10, 22, 2)
    postroy_stena_x(2, 8, 21)
    postroy_stena_x(2, 8, 1)
    postroy_stena_x(2, 8, 21)
    postroy_stena_x(26, 32, 21)
    postroy_stena_x(26, 32, 1)

    t = range(0, 23, 1)
    tyr = [*t]

    for did in tyr:
        postroy_tochke(1, 35, did)

    # ctroem_tochku_po_kvadratnom_kaardenatam(1,1)
    # zactraevaem_pole_tochke()


levl_1()
wrap.sprite.add_text("ПОЙМАНЫЕ ТОЧКИ", 100, 100, text_color=(0, 255, 6))

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

    for did in spisoktochhek:
        edim_tochke(did)


def dvizhenie_kist(nomerkusta):
    print("проветрка")
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
