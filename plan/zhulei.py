import pygame
from jingling import *
pygame.font.init()
font=pygame.font.SysFont(None,30)
class PlaneGame(object):
	def __init__(self):
		print('初始化窗口')
		# 1. 创建游戏的窗口
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		# 2. 创建游戏的时钟
		self.clock = pygame.time.Clock()
		# 3. 调用私有方法，精灵和精灵组的创建
		self.__create_sprites()

		#敌机出现的时间
		pygame.time.set_timer(CREATE_ENEMY_EVENT,500)#敌机时间
		pygame.time.set_timer(CREATE_BULLET_EVENT,250)#子弹时间越大越慢

		#敌机的精灵组
		self.enemy_group=pygame.sprite.Group()
		#敌机销毁精灵组
		self.enemy1_down_group=pygame.sprite.Group()
		self.count=0
		self.score=0#分数


	def start_game(self):
		print("开始游戏...")
		while True:
			self.count+=1
			# 1. 设置刷新帧率
			self.clock.tick(60)
			# 2. 事件监听
			self.__event_handler()
			# 3. 碰撞检测
			self.__check_collide()
			# 4. 更新精灵组
			self.__update_sprites()
			# 5. 更新屏幕显示
			pygame.display.update()


	def __create_sprites(self):
		'''创建精灵'''
		bg1=BackGroundSprite()
		bg2=BackGroundSprite(True)
		self.enemy_group=pygame.sprite.Group()#创建敌机精灵组		
		self.bg_group=pygame.sprite.Group(bg1,bg2)

		self.hero=Hero()#英雄组
		self.hero_group=pygame.sprite.Group(self.hero)

	def __event_handler(self):
		'''监听事件'''
		for event in pygame.event.get():
			#判断是否退出游戏
			if event.type==pygame.QUIT:
				planeGame.__game_over()
			elif event.type==CREATE_ENEMY_EVENT:#定时敌机出现
				print('敌机出场')
				self.enemy_group.add(EnemySprite())
			elif event.type==CREATE_BULLET_EVENT:#定时子弹
				self.hero.fire()

		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_RIGHT]:
			self.hero.speed = 12
		elif keys_pressed[pygame.K_LEFT]:
			self.hero.speed = -12
		elif keys_pressed[pygame.K_UP]:
			self.hero.speeds = -12
		elif keys_pressed[pygame.K_DOWN]:
			self.hero.speeds = 12
		else:
			self.hero.speed = 0
			self.hero.speeds=0

		if keys_pressed[pygame.K_SPACE]:
			self.hero.fire()

	def __check_collide(self):
		'''碰撞检测'''
		#1.子弹摧毁敌机,返回敌机的精灵
		enemy_down=pygame.sprite.groupcollide(self.hero.bullet_group,self.enemy_group,True,True)
		#加入销毁组
		enemy1_down_group.add(enemy_down)
		#2.敌机摧毁英雄
		enemies=pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
		
		#3判断列表有内容
		if len(enemies)>0:
			#让英雄牺牲
			self.hero.kill()
			#结束游戏
			PlaneGame.__game_over()

	def __update_sprites(self):
		#更新精灵组
		self.bg_group.update()
		self.bg_group.draw(self.screen)

		self.enemy_group.update()
		self.enemy_group.draw(self.screen)

		self.hero_group.update()
		self.hero_group.draw(self.screen)

		self.hero.bullet_group.update()
		self.hero.bullet_group.draw(self.screen)

		self.drawText(str(self.score),SCREEN_RECT.width-30,50)#绘制分数

		for enemy1_down in enemy1_down_group:
			self.screen.blit(enemy1_down_surface[enemy1_down.down_index],enemy1_down.rect)
			if self.count%10==0:#爆炸索引间隔时间
				enemy1_down.down_index+=1
				if enemy1_down.down_index==3:#4张爆炸效果 3个索引
					self.score+=5#一次次加5分
					enemy1_down_group.remove(enemy1_down)
					print(self.score)


	@staticmethod
	def __game_over():#游戏结束
		print('你已经挂了')
		pygame.quit()
		exit()

	def drawText(self,text,posx,posy,textHeight=48,fontColor=(0,0,0),backgroudColor=(255,255,255)):
			fontObj = pygame.font.Font(None,textHeight)  # 通过字体文件获得字体对象
			textSurfaceObj = fontObj.render(text, True,fontColor,backgroudColor)  # 配置要显示的文字
			textRectObj = textSurfaceObj.get_rect()  # 获得要显示的对象的rect
			textRectObj.center = (posx, posy)  # 设置显示对象的坐标
			self.screen.blit(textSurfaceObj, textRectObj)  # 绘制字	


if __name__=='__main__':
	#创建对象
	game=PlaneGame()
	#开始游戏
	game.start_game()

