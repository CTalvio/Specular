import pygame, PyIgnition, sys


screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

effect = PyIgnition.ParticleEffect(screen)
gravity = effect.CreateVortexGravity(pos = (400, 300), strength = -3.0, strengthrandrange = 0.0)
source = effect.CreateSource(initspeed = 12.0, initspeedrandrange = 6, initdirectionrandrange = 3.3
, particlesperframe = 0, particlelife = 400, drawtype = PyIgnition.DRAWTYPE_LINE, length = 10.0, radius = 5.0)


def Draw():
    screen.fill((255, 255, 255))

    effect.Update()
    effect.Redraw()

    mpos = pygame.mouse.get_pos()
    #f = gravity.GetForce(mpos)
    #endpos = [mpos[0] + f[0], mpos[1] + f[1]]

    #pygame.draw.aaline(screen, (0, 0, 0), mpos, endpos)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
			source.CreateKeyframe(source.curframe + 1, pos = pygame.mouse.get_pos(), particlesperframe = 30)
			source.CreateKeyframe(source.curframe + 2, pos = pygame.mouse.get_pos(), particlesperframe = 0)

    Draw()
    pygame.display.update()
    clock.tick(30)
