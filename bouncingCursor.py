import time, math, win32api

# environment parameters
## cf, https://msdn.microsoft.com/en-us/library/windows/desktop/ms724385(v=vs.85).aspx
SM_CXCURSOR, SM_CYCURSOR = 13, 14

## Don't know why, but seems not having 1/1 scale... 
cursorWidth = int(win32api.GetSystemMetrics(SM_CXCURSOR)/4)
cursorHeight = int(win32api.GetSystemMetrics(SM_CYCURSOR)/2)

width, height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
mouseX, mouseY = win32api.GetCursorPos()[0], win32api.GetCursorPos()[1]

# physical parameters
m = 10
g = 9.8*0.2

# setup
vY = vX = 0
bounceCount = 0
loop = True

while loop == True:
    aX = (win32api.GetCursorPos()[0] - mouseX)/m
    aY = (win32api.GetCursorPos()[1] - mouseY)/m
    
    vX, vY = vX + aX, vY + g + aY
    dX, dY = int(vX), int(vY)
    
    if mouseY + dY > height - cursorHeight:
        mouseY = int(height - cursorHeight)
        vY = -0.85 * vY
        vX = 0.8 * vX
        bounceCount+=1
        if (bounceCount > 1 and abs(vY) < cursorHeight/4) or bounceCount > 50:
                mouseY = int(height-cursorHeight)
                loop = False 
    else:
        mouseY = mouseY + dY
    mouseX += dX
    
    win32api.SetCursorPos((mouseX,mouseY))
    time.sleep(0.01)