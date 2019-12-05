from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.collision import *
from PPlay.window import* 
import globais



class Mob(object):
    def __init__(self, sprite, spriteL, frames, time, speed, vida, dano, sp, boss=False):
        self.sprite_mov = [Sprite(spriteL, frames), Sprite(sprite, frames)]
        self.sprite_mov[0].set_total_duration(time)
        self.sprite_mov[1].set_total_duration(time)
        self.vel = globais.MOB_SPEED*speed #*self.multiplier
        self.vel_x = 0
        self.vel_y = 0
        self.vida = vida
        self.dano = dano
        self.sp = sp
        self.direcao = True
        self.boss = boss
        self.stun = 0
        #self.dirChange = 5
        
        

class Inimigo(object):
    def __init__(self, window, fase, jogador):
        self.window = window
        self.teclado = Keyboard() 
        self.fase = fase
        self.inimigos = []
        self.__setup()
        self.jogador = jogador
        self.j_pos_x = self.jogador.fiona[0].x
        self.j_pos_y = self.jogador.fiona[0].y
        self.posCD = 100

    
    def __setup(self): #y<350 #x<650
        if self.fase == 1:
            self.spawn(1, self.window.width/2, self.window.height/2 -200)
            self.spawn(1, self.window.width/2+300, self.window.height/2 -275)
            self.spawn(1, self.window.width/2+150, self.window.height/2-50)
            self.spawn(1, self.window.width/2-150, self.window.height/2+50)
            self.spawn(1, self.window.width/2-350, self.window.height/2+250)
            self.spawn(1, self.window.width/2, self.window.height/2+300)
            self.spawn(3, self.window.width/2, self.window.height/2)
            self.spawn(2, self.window.width/2+550, self.window.height/2+200)
            self.spawn(2, self.window.width/2+450, self.window.height/2+250)

        if self.fase == 2:
            self.spawn(1, self.window.width/2, self.window.height/2-175)
            self.spawn(1, self.window.width/2+325, self.window.height/2-250)
            self.spawn(1, self.window.width/2-250, self.window.height/2-50)
            self.spawn(1, self.window.width/2-350, self.window.height/2+175)
            self.spawn(3, self.window.width/2, self.window.height/2)
            self.spawn(3, self.window.width/2+150, self.window.height/2-150)
            self.spawn(3, self.window.width/2-150, self.window.height/2+150)
            self.spawn(4, self.window.width/2+400, self.window.height/2+150)
            self.spawn(2, self.window.width/2+550, self.window.height/2+100)
            self.spawn(2, self.window.width/2+250, self.window.height/2+300)

        if self.fase == 3:
            self.spawn(3, self.window.width/2-200, self.window.height/2-100)
            self.spawn(3, self.window.width/2-50, self.window.height/2-300)
            self.spawn(3, self.window.width/2-400, self.window.height/2+50)
            self.spawn(3, self.window.width/2-600, self.window.height/2+250)
            self.spawn(2, self.window.width/2+550, self.window.height/2-300)
            self.spawn(2, self.window.width/2+450, self.window.height/2-300)
            self.spawn(2, self.window.width/2+350, self.window.height/2-300)
            self.spawn(2, self.window.width/2+550, self.window.height/2+300)
            self.spawn(2, self.window.width/2+450, self.window.height/2+300)
            self.spawn(2, self.window.width/2+350, self.window.height/2+300)
            self.spawn(4, self.window.width/2+50, self.window.height/2-50)
            self.spawn(4, self.window.width/2+325, self.window.height/2-115)
            self.spawn(4, self.window.width/2-115, self.window.height/2+175)

        if self.fase == 4:
            self.spawn(3, self.window.width/2+150, self.window.height/2-250)
            self.spawn(3, self.window.width/2+50, self.window.height/2-175)
            self.spawn(3, self.window.width/2-50, self.window.height/2-100)
            self.spawn(3, self.window.width/2-150, self.window.height/2-25)
            self.spawn(3, self.window.width/2-250, self.window.height/2+50)
            self.spawn(2, self.window.width/2+500, self.window.height/2-250)
            self.spawn(2, self.window.width/2+500, self.window.height/2-125)
            self.spawn(2, self.window.width/2+500, self.window.height/2)
            self.spawn(2, self.window.width/2+500, self.window.height/2+125)
            self.spawn(2, self.window.width/2+500, self.window.height/2+250)
            self.spawn(4, self.window.width/2+325, self.window.height/2-100)
            self.spawn(4, self.window.width/2+175, self.window.height/2)
            self.spawn(4, self.window.width/2+125, self.window.height/2+100)
            self.spawn(4, self.window.width/2+75, self.window.height/2+200)
            

        if self.fase == 5:
            self.spawn(5,self.window.width-300, self.window.height/2-75)
            self.spawn(2, self.window.width/2+500, self.window.height/2-250)
            self.spawn(2, self.window.width/2+500, self.window.height/2-125)
            self.spawn(2, self.window.width/2+500, self.window.height/2)
            self.spawn(2, self.window.width/2+500, self.window.height/2+125)
            self.spawn(2, self.window.width/2+500, self.window.height/2+250)

    def spawn(self,tipo, x, y):
        if tipo == 1:#Guarda
            mob = Mob(
                "./Imagens/Inimigos/Guarda/Guards.png",
                "./Imagens/Inimigos/Guarda/Guards_L.png",
                4,
                800,
                0.75,
                3,
                1,
                1
            )
        elif tipo == 2: #Bruxa
            mob = Mob(
                "./Imagens/Inimigos/Bruxa/witch.png",
                "./Imagens/Inimigos/Bruxa/witch_L.png",
                3,
                500,
                1.5,
                3,
                2,
                1
           )
        elif tipo==3: #Capitao
            mob = Mob(
                "./Imagens/Inimigos/Capitao/Guards_lance.png",
                "./Imagens/Inimigos/Capitao/Guards_lance_L.png",
                3,
                800,
                1,
                6,
                2,
                1                
            )
        elif tipo==4: #Martelo
            mob = Mob(
                "./Imagens/Inimigos/Martelo/Guards_Hammer.png",
                "./Imagens/Inimigos/Martelo/Guards_Hammer_L.png",
                3,
                1500,
                0.75,
                12,
                3,
                2
            )
        
        elif tipo==5: #Boss
            mob = Mob(
                "./Imagens/Inimigos/Boss/Warder.png",
                "./Imagens/Inimigos/Boss/Warder_L.png",
                8,
                800,
                0.75,
                50,
                1,
                1,
                True
            )

        mob.sprite_mov[0].set_position(x,y)
        mob.sprite_mov[1].set_position(x,y)
        self.inimigos.append(mob)
    
    def update(self):
        if self.posCD <= 0:
            self.j_pos_x = self.jogador.fiona[0].x+self.jogador.fiona[0].width/2
            self.j_pos_y = self.jogador.fiona[0].y+self.jogador.fiona[0].height/2
            self.posCD = 75
        else:
            self.posCD -= 1
        
        for mob in self.inimigos:
            if mob.stun <= 0:
                if self.j_pos_x > mob.sprite_mov[0].x+mob.sprite_mov[0].width/2:
                    mob.vel_x = 1
                    if self.jogador.fiona[0].x - mob.sprite_mov[0].x >20:
                    #if mob.dirChange <= 0:
                        mob.direcao = False
                if self.j_pos_x < mob.sprite_mov[0].x+mob.sprite_mov[0].width/2:
                    mob.vel_x = -1
                    if mob.sprite_mov[0].x-self.jogador.fiona[0].x > 20:
                    #if mob.dirChange <= 0:
                        mob.direcao = True
                if self.j_pos_y > mob.sprite_mov[0].y+mob.sprite_mov[0].height/2:
                    mob.vel_y = 1
                if self.j_pos_y < mob.sprite_mov[0].y+mob.sprite_mov[0].height/2:
                    mob.vel_y = -1

                #if mob.dirChange >0:
                #    mob.dirChange -= self.window.delta_time()

                mob.sprite_mov[0].x += mob.vel * mob.vel_x * self.window.delta_time()
                mob.sprite_mov[0].y += mob.vel * mob.vel_y * self.window.delta_time()
                mob.sprite_mov[1].set_position(mob.sprite_mov[0].x, mob.sprite_mov[0].y) #posicao do sprite[1] segue a do [0]
            
            elif mob.stun > 0:
                mob.stun -= self.window.delta_time()

        for mob in self.inimigos:
            if self.jogador.drag.fireOut == False:        
                if self.jogador.drag.fireBall.collided(mob.sprite_mov[0]):
                    self.jogador.drag.fireBall.x= 1400
                    mob.vida -= 5
                    if mob.boss:
                        mob.stun = 2
                
                if mob.vida <= 0:
                    self.jogador.tempo_especial -= mob.sp
                    self.inimigos.remove(mob)
                    break


                    
            for tiro in self.jogador.vet_tiro:
                if tiro.bullet.collided(mob.sprite_mov[0]):
                    self.jogador.vet_tiro.remove(tiro)
                    mob.vida -= 1
                if mob.vida <= 0:
                    self.inimigos.remove(mob)
                    break
                
        
        for mob in self.inimigos:
            mob.sprite_mov[0].update()
            mob.sprite_mov[1].update()
            if mob.direcao == True:
                mob.sprite_mov[0].draw()
            elif mob.direcao == False:
                mob.sprite_mov[1].draw()
        
        
        
            