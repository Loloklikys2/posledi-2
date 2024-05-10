pravo = 0
vniz = 0
def setup():
    background(90,109,160)
    size(800,600)
    
def draw():
    global pravo
    global vniz
    background(90,109,160)
    textSize(25)
    text("proide labirint", 300, 550);
    fill(180,249,255)
    ellipse(mouseX,mouseY,20,20)
    if keyPressed ==True:
        if key == "d":
            pravo = pravo + 1
                
    
        if key == 's':
            vniz = vniz + 1
            
        if key == "a":
            pravo = pravo - 1
            

            
        if key == "w":
            vniz = vniz - 1
            
    strokeWeight(5)
    point(280,520)
    point(280,600)
    line(280,520,280,600)
    
    point(480,520)
    point(480,600)
    line(480,520,480,600)
    line(280,520,480,520)
    
    point(30,0)
    point(30,60)
    line(30,0,30,60)
    point(65,60)
    line(30,60,65,60)
    point(65,23)
    line(65,60,65,23)
    point(100,23)
    line(65,23,100,23)
    point(125,23)
    line(100,23,125,23)
    point(125,60)
    line(125,23,125,60)
    point(100,60)
    line(125,60,100,60)
    point(100,110)
    line(100,60,100,110)

    
    
    point(170,110)
    line(100,110,170,110)
    point(170,25)
    line(170,110,170,25)
    point(230,25)
    line(170,25,230,25)
    point(290,25)
    
    
    line(230,25,290,25)
    point(290,55)
    line(290,25,290,55)
        
