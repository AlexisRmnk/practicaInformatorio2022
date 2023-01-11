import random
from def_tenis2 import *

class Player:
    def __init__(self, name:str):
        self.name = name
        self.score = 0
        self.games = 0
        self.sets = 0
        # self.deuce = False
        self.advantage = False # to use when DEUCE state
   
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getScore(self):
        return self.score
    def setScore(self, score):
        self.score = score
    def getGames(self):
        return self.games
    def setGames(self, games):
        self.games = games
    def getSets(self):
        return self.sets
    def setSets(self, sets):
        self.sets = sets
    def getAdvantage(self):
        return self.advantage
    def setAdvantage(self, advantage):
        self.advantage = advantage
    
    def reset_games_score_adv(self):
        self.score = 0
        self.games = 0
        self.advantage = False
        
class Match:
    status_tuple = ("Ongoing", "Deuce","Tie Brake", "Ended")
    def __init__(self):
        name_p1, name_p2 = self.__ask_players() 
        self.players = dict() #type: dict[int, Player]
        self.players[1] = Player(name_p1)
        self.players[2] = Player(name_p2)
        self.winner = Player("")
        self.status = self.status_tuple[0]      
    
    def getStatus(self):
        return self.status
    def getStatus_final_value(self):
        return self.status_tuple[-1]
    
    def __ask_players(self):
        while(True):
            print("Indicar el nombre del primer jugador:")
            name_p1 = input("\t").strip().title()
            print("Indicar el nombre del segundo jugador")
            name_p2 = input("\t").strip().title()
            
            print(f"Jugador 1: {name_p1}. Jugador 2: {name_p2}.")
            op = return_S_N()
            if op == "S":
                return (name_p1, name_p2)   
    
    def good_ball(self):
        print(f"Indicar que jugador anoto el punto:\n\t1) {self.players[1].getName()}."
              f"\n\t2) {self.players[2].getName()}.")
        player_n = return_1_2(input("\t\t"))
        self.__add_point(self.players[player_n])    
       
    def test_good_ball(self):
        '''function made for testing purposes'''
        player_n_test = random.randint(1,2)
        print(f"PUNTO DEL JUGADOR {player_n_test} "
              f"({self.players[player_n_test].getName()})")
        self.__add_point(self.players[player_n_test])
        if self.players[1].getSets() > 3:
            raise ValueError("Revisar linea de codigo. (No se pueden haber"
                            " registrado mas de 3 sets para el jugador 1)") 
        if self.players[2].getSets() > 3: 
            raise ValueError("Revisar linea de codigo. (No se pueden haber"
                            " registrado mas de 3 sets para el jugador 2)") 
    
    
    def __add_point(self, player:Player):
        other_player = self.__get_other_player(player)
        if self.status == self.status_tuple[0]:
            if player.getScore() == 0:
                player.setScore(15)
            elif player.getScore() == 15:
                player.setScore(30)
            elif player.getScore() == 30:
                player.setScore(40)
                if other_player.getScore() == 40:
                    self.status = self.status_tuple[1] #DEUCE STATUS alert
            elif player.getScore() == 40:
                if other_player.getScore() < 40:
                    self.__add_game(player)
                else:
                    raise ValueError("Revisar linea de codigo.")
        elif self.status == self.status_tuple[1]: #DEUCE STATUS 
            # inicio del deuce. A partir de aca dejamos de usar los
            # 'scores' y trabajamos con ventaja/deuce
            self.players[1].setScore(0)
            self.players[2].setScore(0)
            if player.getAdvantage():
                self.status = self.status_tuple[0]
                self.__add_game(player)
            else: # player.getAdvantage() == False:
                if other_player.getAdvantage():
                    other_player.setAdvantage(False)
                else: #other_player.getAdvantage == False
                    player.setAdvantage(True)
        elif self.status == self.status_tuple[2]: # TIE BRAKE STATUS
            player.setScore(player.getScore() + 1)
            diff_score = player.getScore() - other_player.getScore()
            if player.getScore() >= 7:
                if diff_score >= 2:
                    self.__add_set(player)
                    self.status = self.status_tuple[0] # ONGOING
        else: # ENDED STATUS
            print("No es posible agregar un punto. La partida ha finalizado.")
        
    def __add_game(self, player:Player):
        other_player = self.__get_other_player(player)
        player.setGames(player.getGames() + 1) # adds 1 game to the winner
        diff_g = player.getGames() - other_player.getGames()
        if player.getGames() >= 6:
            if other_player.getGames() == 6:
                self.status = self.status_tuple[2] # 6:6 TIE BRAKE
                self.__reset_games()
            elif diff_g >= 2: # 2  o mas puntos de ventaja
                self.__add_set(player)
            elif diff_g == 1: # un solo punto de ventaja (caso 6:5)
                pass
            else:
                raise ValueError("Revisar linea de codigo. (No se puede "
                                "dar un caso distinto a los 2 anteriores)")
        player.setScore(0)
        other_player.setScore(0)
        player.setAdvantage(False)
        other_player.setAdvantage(False)
        
    def __add_set(self, player:Player):
        player.setSets(player.getSets() + 1)
        self.__reset_games()
        if player.getSets() == 3:
            self.winner = player
            print(f"Jugador {self.winner.getName()} gana el juego con 3 sets.")
            self.status = self.status_tuple[-1] 
    
    def __get_other_player(self, player:Player) -> Player:
        '''if player1 its selected, then returns player2 and vice versa'''
        if player == self.players[1]:
            return self.players[2]
        else: # player == self.players[2]:
            return self.players[1]
                
    def __reset_games(self):
        self.players[1].reset_games_score_adv()
        self.players[2].reset_games_score_adv()
        
    def show_status(self):
        if self.status == self.status_tuple[0]: #ongoing
            print("La partida se encuentra en su curso normal.")
            print(f"Jugador 1 - {self.players[1].getName()}:")
            print(f"\tScore: {self.players[1].getScore()}\t"
                  f"Games:{self.players[1].getGames()}\t\t"
                  f"Sets:{self.players[1].getSets()}")
            print("")
            print(f"Jugador 2 - {self.players[2].getName()}:")
            print(f"\tScore: {self.players[2].getScore()}\t"
                  f"Games:{self.players[2].getGames()}\t\t"
                  f"Sets:{self.players[2].getSets()}")
        elif self.status == self.status_tuple[1]: #deuce
            print("La partida se encuentra en estado 'deuce'.")
            if (self.players[1].getAdvantage() and 
                not self.players[2].getAdvantage()):
                print(f"Jugador 1 - {self.players[1].getName()}")
                print("Tiene ventaja")
            elif (self.players[2].getAdvantage() and 
                not self.players[1].getAdvantage()):
                print(f"Jugador 2 - {self.players[2].getName()}")
                print("Tiene ventaja")
            elif (self.players[1].getAdvantage() == False and
                  self.players[2].getAdvantage() == False):
                print("Ningun jugador tiene ventaja.")
            else:
                raise ValueError("Revisar linea de codigo. (ambos jugadores "
                                 "no pueden tener ventaja simultaneamente)")
        elif self.status == self.status_tuple[2]: #Tie brake
            print("La partida se encuentra en 'Tie brake'")
            print(f"\tScore: {self.players[1].getScore()}\t"
                  f"Games:{self.players[1].getGames()}\t\t"
                  f"Sets:{self.players[1].getSets()}")
            print("")
            print(f"Jugador 2 - {self.players[2].getName()}:")
            print(f"\tScore: {self.players[2].getScore()}\t"
                  f"Games:{self.players[2].getGames()}\t\t"
                  f"Sets:{self.players[2].getSets()}")
        elif self.status == self.status_tuple[2]: #ended
            print(f"La partida finalizo. El ganador es "
                  f"{self.winner.getName()}") 