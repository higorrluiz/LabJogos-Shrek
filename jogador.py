from PPlay.window import*
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.collision import *
from PPlay.keyboard import *
import globais
class Jogador(object):
    def __init__(self,window):
        self.window = window
        self.teclado = Keyboard()
        self.fiona = [Sprite("./Imagens/Fiona/FionaR.png", 6),Sprite("./Imagens/Fiona/FionaL.png", 6)]
        self.fiona[0].set_position(globais.BORDER,30)
        self.fiona[0].set_total_duration(1000)
        self.vet_tiro= []
        self.reload_cron = 0
        self.drag = Dragao(self.fiona[0].y, 0, True)
        self.primeira = True
        self.tempo_especial = 5
        self.direcao = 0
       

    def update(self):

        i = self.direcao

        if self.primeira:
            self.fiona[1].set_total_duration(1000)
            self.fiona[1].x=self.fiona[0].x
            self.fiona[1].y=self.fiona[0].y
            self.primeira = False
        

        if (self.teclado.key_pressed("w")==True
            and self.teclado.key_pressed("s")==False
        ):
            self.fiona[i-1].y -= 1
            self.fiona[i].y -= 1
        
        if (self.teclado.key_pressed("w")==False
            and self.teclado.key_pressed("s")==True
        ):       
            self.fiona[i-1].y +=1
            self.fiona[i].y += 1
        
        if (self.teclado.key_pressed("a")==True
            and self.teclado.key_pressed("d")==False
        ):
            i=1
            self.fiona[i-1].x -=1
            self.fiona[i].x -= 1

        if (self.teclado.key_pressed("a")==False
            and self.teclado.key_pressed("d")==True
        ):      
            i=0  
            self.fiona[-1].x += 1
            self.fiona[i].x += 1
        
        self.direcao = i
        
        
        #IFs para limitar espaço de locomoção da fiona
        if self.fiona[i].x >= self.window.width-self.fiona[i].width or self.fiona[i-1].x >= self.window.width-self.fiona[i-1].width:
            self.fiona[i].x = self.window.width-self.fiona[i].width
            self.fiona[i-1].x = self.window.width-self.fiona[i-1].width
        
        if self.fiona[i].x <=0 or self.fiona[i-1].x <=0 :
            self.fiona[i].x=0
            self.fiona[i-1].x=0
        
        if self.fiona[i].y <= 0 or self.fiona[i-1].y <= 0:
            self.fiona[i].y=1
            self.fiona[i-1].y=1


        if self.fiona[i].y>= self.window.height- self.fiona[i].height or self.fiona[i-1].y>= self.window.height- self.fiona[i-1].height:
            self.fiona[i].y = self.window.height- self.fiona[i].height
            self.fiona[i-1].y = self.window.height- self.fiona[i-1].height

        vely = 0
        velx = 0
        
        if (self.teclado.key_pressed("left")==False #Tiro para diagonal direita-cima
            and self.teclado.key_pressed("right")==True
            and self.teclado.key_pressed("up")==True
            and self.teclado.key_pressed("down")==False
            and self.reload_cron == 0
        ):
            velx = 1
            vely = -1    
            bala = Tiro(self.fiona[i].x+(self.fiona[i].width/2), self.fiona[i].y+(self.fiona[i].height/2), velx, vely)
            self.vet_tiro.append(bala)
            self.reload_cron = 100

        if (self.teclado.key_pressed("left")==False #Tiro para diagonal direita-baixo
            and self.teclado.key_pressed("right")==True
            and self.teclado.key_pressed("up")==False
            and self.teclado.key_pressed("down")==True
            and self.reload_cron == 0
        ):
            velx = 1
            vely = 1    
            bala = Tiro(self.fiona[i].x+(self.fiona[i].width/2), self.fiona[i].y+(self.fiona[i].height/2), velx, vely)
            self.vet_tiro.append(bala)
            self.reload_cron = 100   

        if (self.teclado.key_pressed("left")==True #Tiro para diagonal esquerda-cima
            and self.teclado.key_pressed("right")==False
            and self.teclado.key_pressed("up")==True
            and self.teclado.key_pressed("down")==False
            and self.reload_cron == 0
        ):
            velx = -1
            vely = -1    
            bala = Tiro(self.fiona[i].x+(self.fiona[i].width/2), self.fiona[i].y+(self.fiona[i].height/2), velx, vely)
            self.vet_tiro.append(bala)
            self.reload_cron = 100

        if (self.teclado.key_pressed("left")==True #Tiro para diagonal esquerda-baixo
            and self.teclado.key_pressed("right")==False
            and self.teclado.key_pressed("up")==False
            and self.teclado.key_pressed("down")==True
            and self.reload_cron == 0
        ):
            velx = -1
            vely = 1    
            bala = Tiro(self.fiona[i].x+(self.fiona[i].width/2), self.fiona[i].y+(self.fiona[i].height/2), velx, vely)
            self.vet_tiro.append(bala)
            self.reload_cron = 100
        
        if (self.teclado.key_pressed("up")==True #Tiro para cima
            and self.teclado.key_pressed("down")==False
            and self.reload_cron == 0
        ):
            vely = -1
            bala = Tiro(self.fiona[i].x+(self.fiona[i].width/2), self.fiona[i].y+(self.fiona[i].height/2), velx, vely)
            self.vet_tiro.append(bala)
            self.reload_cron = 100

        if (self.teclado.key_pressed("up")==False #Tiro para baixo
            and self.teclado.key_pressed("down")==True
            and self.reload_cron == 0
        ):        
            vely = 1
            bala = Tiro(self.fiona[i].x+(self.fiona[i].width/2), self.fiona[i].y+(self.fiona[i].height/2), velx, vely)
            self.vet_tiro.append(bala)
            self.reload_cron = 100

        if (self.teclado.key_pressed("left")==True #Tiro para esquerda
            and self.teclado.key_pressed("right")==False
            and self.reload_cron == 0
        ):
            velx = -1
            bala = Tiro(self.fiona[i].x+(self.fiona[i].width/2), self.fiona[i].y+(self.fiona[i].height/2), velx, vely)
            self.vet_tiro.append(bala)
            self.reload_cron = 100

        if (self.teclado.key_pressed("left")==False #Tiro para direita
            and self.teclado.key_pressed("right")==True
            and self.reload_cron == 0
        ):
            velx = 1   
            bala = Tiro(self.fiona[i].x+(self.fiona[i].width/2), self.fiona[i].y+(self.fiona[i].height/2), velx, vely)
            self.vet_tiro.append(bala)
            self.reload_cron = 100

        if self.reload_cron > 0:
            self.reload_cron -= 1
        
        
        self.fiona[i].update()
        self.fiona[i].draw()
        
        if len(self.vet_tiro)>0:
            for bala in self.vet_tiro:
                if (
                    bala.bullet.x < 0
                    or bala.bullet.x + bala.bullet.width > self.window.width
                    or bala.bullet.y < 0
                    or bala.bullet.y+bala.bullet.height > self.window.height
                ):
                    self.vet_tiro.remove(bala)
                else:    
                    bala.bullet.x += bala.vel_x*self.window.delta_time()
                    bala.bullet.y += bala.vel_y*self.window.delta_time()
                    bala.bullet.update()
                    bala.bullet.draw()

        if self.tempo_especial >= 1:
                self.tempo_especial -= self.window.delta_time()

        if self.tempo_especial <=1  and self.teclado.key_pressed("space"):
            self.drag = Dragao(self.fiona[i].y-self.fiona[i].height, 1)
            self.tempo_especial = 11
           
        
        if self.drag.Dcount > 0:
            self.drag.dragoneza.update()
            self.drag.dragoneza.draw()
            self.drag.Dcount -= self.window.delta_time()

        if self.drag.fireBall.x > self.window.width:
            self.drag.fireOut = True
        
        if self.drag.Dcount <= 0.5:
            if self.drag.fireOut == False:
                self.drag.fireBall.x +=250*self.window.delta_time() #movimenta a bola de fogo
                self.drag.fireBall.update()
                self.drag.fireBall.draw()

                    
class Tiro(object):
    def __init__(self, x_inicial, y_inicial, vel_x, vel_y):
        self.speed = 300
        self.bullet = Sprite("./Imagens/Fiona/bullet.png",8)
        self.bullet.set_total_duration(1)
        self.bullet.set_position(x_inicial, y_inicial)
        self.vel_x = vel_x *self.speed
        self.vel_y = vel_y *self.speed

class Dragao(object):
    def __init__(self, pos_y, count, fire = False):
        self.dragoneza = Sprite("./Imagens/Fiona/Dragao_mov.png", 18)
        self.fireBall = Sprite("./Imagens/Fiona/fireBall.png", 4)
        self.fireBall.set_total_duration(500)
        self.dragoneza.set_total_duration(1000)
        self.dragoneza.set_position(0, pos_y)
        self.fireBall.set_position(self.dragoneza.width,self.dragoneza.y+(self.dragoneza.height/2))
        self.Dcount = count
        self.fireOut = fire
