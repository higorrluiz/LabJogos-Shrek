from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.collision import *
from PPlay.window import* 
import globais


direção = 0

class Mob(object):
    def __init__(self, sprite, frames, time, speed, vida, dano, sp, boss=False):
        self.sprite_mov = [Sprite(sprite+'.png',frames), Sprite(sprite+'_L'+'.png', frames) ]
        self.sprite_mov[0].set_total_duration(time)
        self.sprite_mov[1].set_total_duration(time)
        self.vel = globais.MOB_SPEED*speed #*self.multiplier
        self.vel_x = 0
        self.vel_y = 0
        self.vida = vida
        self.dano = dano
        self.sp = sp
        
        

class Inimigo(object):
    def __init__(self, window, fase, jogador,dragao):
        self.window = window
        self.teclado = Keyboard() 
        self.fase = fase
        self.inimigos = []
        self.__setup()
        self.jogador = jogador
        self.dragon = dragao
        self.j_pos_x = self.jogador.fiona[0].x
        self.j_pos_y = self.jogador.fiona[0].y
        self.posCD = 100
        self.lado= 34
       
      
        
    
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
                "./Imagens/Inimigos/Guarda/Guards",
                4,
                800,
                0.75,
                3,
                1,
                1
            )
        elif tipo == 2: #Bruxa
            mob = Mob(
                "./Imagens/Inimigos/Bruxa/witch",
                3,
                500,
                1.5,
                3,
                2,
                1
           )
        elif tipo==3: #Capitao
            mob = Mob(
                "./Imagens/Inimigos/Capitao/Guards_lance",
                3,
                800,
                1,
                6,
                2,
                1                
            )
        elif tipo==4: #Martelo
            mob = Mob(
                "./Imagens/Inimigos/Martelo/Guards_Hammer",
                3,
                1500,
                0.75,
                12,
                3,
                2
            )
        
        elif tipo==5: #Boss
            mob = Mob(
                "./Imagens/Inimigos/Boss/Warder",
                8,
                800,
                0.75,
                50,
                1,
                1,
                True
            )
        self.mob=mob.vel
        mob.sprite_mov[0].set_position(x,y)
        mob.sprite_mov[1].set_position(x,y)
        self.inimigos.append(mob.sprite_mov[0])
        self.inimigos.append(mob.sprite_mov[1])
    
    def update(self):
        
        if self.posCD <= 0:
            self.j_pos_x = self.jogador.fiona[0].x
            self.j_pos_y = self.jogador.fiona[0].y
            self.posCD = 75
        else:
            self.posCD -= 1
        
        for indice in range(0,len(self.inimigos),2):
            if self.j_pos_x+self.jogador.fiona[0].width/2 > self.inimigos[indice].x+self.inimigos[indice].width/2:
                #andando pra esquerda
                self.lado = 0
                self.inimigos[indice].vel_x = 1
                self.inimigos[indice+1].vel_x = 1

            if self.j_pos_x+self.jogador.fiona[0].width/2 < self.inimigos[indice].x + self.inimigos[indice].width/2:
                #andando pra direita
                self.lado = 1
                self.inimigos[indice].vel_x = -1
                self.inimigos[indice+1].vel_x = -1
                
            if self.j_pos_y+self.jogador.fiona[0].height/2 > self.inimigos[indice].y+self.inimigos[indice].height/2:
                #andando pra baixo
                self.inimigos[indice].vel_y = 1
                self.inimigos[indice+1].vel_y = 1
            if self.j_pos_y+self.jogador.fiona[0].height/2 < self.inimigos[indice].y+self.inimigos[indice].height/2:
                #andando pra cima
                self.inimigos[indice].vel_y = -1
                self.inimigos[indice+1].vel_y = -1

            self.inimigos[indice].x += self.mob * self.inimigos[indice].vel_x * self.window.delta_time()
            self.inimigos[indice].y += self.mob * self.inimigos[indice].vel_y * self.window.delta_time()
            self.inimigos[indice].x += self.mob * self.inimigos[indice].vel_x * self.window.delta_time()
            self.inimigos[indice].y += self.mob * self.inimigos[indice].vel_y * self.window.delta_time()

            self.inimigos[indice+1].x += self.mob * self.inimigos[indice].vel_x * self.window.delta_time()
            self.inimigos[indice+1].y += self.mob * self.inimigos[indice].vel_y * self.window.delta_time()
            self.inimigos[indice+1].x += self.mob * self.inimigos[indice].vel_x * self.window.delta_time()
            self.inimigos[indice+1].y += self.mob* self.inimigos[indice].vel_y * self.window.delta_time()
        
        for indice in range(0,len(self.inimigos),2):
            if self.jogador.drag.count > 0:        
                if self.jogador.drag.fireBall.collided(self.inimigos[indice]):
                    self.jogador.drag.fireBall.x= 1400
                    self.inimigos[indice].vida -=3
                    self.inimigos[indice+1].vida -=3
                if self.inimigos[indice].vida <= 0:
                    self.inimigos.pop(indice)
                    self.inimigos.pop(indice+1)
                    break


                    
            for tiro in self.jogador.vet_tiro:
                if tiro.bullet.collided(self.inimigos[indice]):
                    self.jogador.vet_tiro.remove(tiro)
                    self.inimigos[indice].vida -= 1
                    self.inimigos[indice+1].vida -= 1
                if self.inimigos[indice].vida <= 0:
                    self.inimigos.pop(indice)
                    self.inimigos.pop(indice+1)
                    break
               
            if self.lado == 1:
                i= indice+1
                
            if self.lado == 0:
                i = indice
                
            self.inimigos[i].update()
            self.inimigos[i].draw()
               
    

            
                
        
        
        
        
            