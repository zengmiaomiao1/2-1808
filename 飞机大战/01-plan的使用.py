import pygame
pygame.init()
screen = pygame.display.set_mode((480,700))#创建游戏窗口
bg = pygame.image.load('./images/background.png')#加载壁纸
hero = pygame.image.load('./images/hero.gif')#加载飞机图片
time = pygame.time.Clock()#游戏时钟
rect = pygame.Rect(200,200,100,126)

while True:
	time.tick(100)#每秒刷新100次
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("退出游戏")
			pygame.quit()
			exit()
	rect.y -= 20
	if rect.y+rect.height <= 0:
		rect.y = 700
	screen.blit(bg,(0,0))#贴
	screen.blit(hero,rect)
	pygame.display.update()#更新
pygame.quit()

