import tkinter as tk
class Chessboard():
    def __init__(self):
        self.NOCHESS="d"
        self.NDCHESS=" "
        self.BLACK="●"
        self.WHITE="○"
        self.isalive_flag = 0
        self.chessboard_list=[]
        for i in range(19):
            self.chessboard_list.append([])
            for j in range(19):
                self.chessboard_list[i].append(self.NDCHESS)
        self.visitboard=[]
        for i in range(19):
            self.visitboard.append([])
            for j in range(19):
                self.visitboard[i].append(0)
    def chess_down(self,x:int,y:int,color):
        self.chessboard_list[x][y]=color
    def chess_up(self,x:int,y:int):
        self.chessboard_list[x][y]=self.NOCHESS
    def clean_visit(self):
        self.visitboard=[]
        for i in range(19):
            self.visitboard.append([])
            for j in range(19):
                self.visitboard[i].append(0)
        self.isalive_flag = 0
    def is_alive(self,x,y):
        isalive=1
        self.clean_visit()
        self.DFS(x,y)
        if self.isalive_flag == 0:
            isalive=0
        self.clean_visit()
        return isalive
    def upnochess(self):
        token_list = []
        suicide_flag = 0
        for i in range(19):
            for j in range(19):
                if self.chessboard_list[i][j] == self.NOCHESS or self.chessboard_list[i][j] == self.NDCHESS:
                    continue
                elif self.chessboard_list[i][j] == nowplayer and self.is_alive(i, j) == 0:
                    token_list.append([i, j])
        for x, y in token_list:
            self.chessboard_list[x][y] = self.NOCHESS
        for i in range(19):
            for j in range(19):
                if (self.chessboard_list[i][j] == self.BLACK and nowplayer == self.WHITE) or (self.chessboard_list[i][j] == self.WHITE and nowplayer == self.BLACK):
                    if self.is_alive(i,j) == 0:
                        surcide_flag = 1
                        break
    def DFS(self, x, y):
        self.visitboard[x][y] = 1
        directions = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
        for dx, dy in directions:
            if dx < 0 or dx > 18 or dy < 0 or dy > 18:
                continue
            elif self.visitboard[dx][dy] == 0:
                if self.chessboard_list[dx][dy] == self.NOCHESS or self.chessboard_list[dx][dy] == self.NDCHESS:
                    self.isalive_flag = 1
                    return
                elif (self.chessboard_list[dx][dy] == self.BLACK and self.chessboard_list[x][y] == self.WHITE) or (self.chessboard_list[dx][dy] == self.WHITE and self.chessboard_list[x][y] == self.BLACK):
                    continue
                elif self.chessboard_list[dx][dy] == self.chessboard_list[x][y]:
                    self.DFS(dx, dy)
        return
    def new_gui(self,x:int,y:int,color,name:str):
        exec("global c"+str(x)+"_"+str(y))
        exec(name+"=guichess.create_oval(25+40*"+str(x)+",25+40*"+str(y)+",55+40*"+str(x)+",55+40*"+str(y)+",fill='"+color+"',outline='"+color+"')")
def updatedfs():
    for i in range(19):
        for j in range(19):
            chess.upnochess()
def update_gui(chesslist):
    updatedfs()
    for i in range(19):
        for j in range(19):
            if chesslist[i][j] == chess.BLACK:
                chess.new_gui(i,j,"black","c"+str(i)+"_"+str(j))
                continue
            elif chesslist[i][j] == chess.WHITE:
                chess.new_gui(i,j,"white","c"+str(i)+"_"+str(j))
                continue
            elif chesslist[i][j] == chess.NOCHESS:
                chesslist[i][j] == chess.NDCHESS
                guichess.delete("all")
                for i in range(19):
                    guichess.create_line(40,40+(40*i),760,40+(40*i),fill="black")
                for j in range(19):
                    guichess.create_line(40+(40*j),40,40+(40*j),760,fill="black")
                guichess.create_oval(155,155,165,165,fill="black")
                guichess.create_oval(155,395,165,405,fill="black")
                guichess.create_oval(155,635,165,645,fill="black")
                guichess.create_oval(395,155,405,165,fill="black")
                guichess.create_oval(395,395,405,405,fill="black")
                guichess.create_oval(395,635,405,645,fill="black")
                guichess.create_oval(635,155,645,165,fill="black")
                guichess.create_oval(635,395,645,405,fill="black")
                guichess.create_oval(635,635,645,645,fill="black")
                updatedfs()
                for i in range(19):
                    for j in range(19):
                        if chesslist[i][j] == chess.BLACK:
                            chess.new_gui(i,j,"black","c"+str(i)+"_"+str(j))
                            continue
                        elif chesslist[i][j] == chess.WHITE:
                            chess.new_gui(i,j,"white","c"+str(i)+"_"+str(j))
                            continue
    '''for i in chess.chessboard_list:
        print(i)'''
def callback(event):
    global nowplayer
    mousex=event.x
    mousey=event.y
    for i in range(19):
        for j in range(19):
            if (mousex > nodemotion[i][j][0] - 10) and (mousex < nodemotion[i][j][0] + 10):
                if (mousey > nodemotion[i][j][1] - 10) and (mousey < nodemotion[i][j][1] + 10):
                    if nowplayer == chess.BLACK:
                        chess.chess_down(i,j,chess.BLACK)
                        nowplayer = chess.WHITE
                        update_gui(chess.chessboard_list)
                        updatedfs()
                        root.update()
                    elif nowplayer == chess.WHITE:
                        chess.chess_down(i,j,chess.WHITE)
                        nowplayer = chess.BLACK
                        update_gui(chess.chessboard_list)
                        updatedfs()
                        root.update()

def main():
    global guichess
    global chess
    global nodemotion
    global nowplayer
    global root
    root=tk.Tk()
    root.title("Go")
    root.geometry("800x800")
    root.resizable(width=False,height=False)
    chess=Chessboard()
    nowplayer = chess.BLACK
    guichess=tk.Canvas(root,width=800,height=800,background="#A0522D")
    guichess.pack()
    for i in range(19):
        guichess.create_line(40,40+(40*i),760,40+(40*i),fill="black")
    for j in range(19):
        guichess.create_line(40+(40*j),40,40+(40*j),760,fill="black")
    guichess.create_oval(155,155,165,165,fill="black")
    guichess.create_oval(155,395,165,405,fill="black")
    guichess.create_oval(155,635,165,645,fill="black")
    guichess.create_oval(395,155,405,165,fill="black")
    guichess.create_oval(395,395,405,405,fill="black")
    guichess.create_oval(395,635,405,645,fill="black")
    guichess.create_oval(635,155,645,165,fill="black")
    guichess.create_oval(635,395,645,405,fill="black")
    guichess.create_oval(635,635,645,645,fill="black")
    nodemotion=[]
    for i in range(19):
        nodemotion.append([])
        for j in range(19):
            nodemotion[i].append([])
            nodemotion[i][j].append(40+40*i)
            nodemotion[i][j].append(40+40*j)
    guichess.bind("<Button-1>",callback)
    root.mainloop()
if __name__ == "__main__":
    main()
