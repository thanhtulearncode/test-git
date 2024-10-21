import pygame as pg

class MapResource:
    def __init__(self, resource_manager, resource_type, amount):
        def __init__(self, resource_manager, resource_type, amount):
        self.resource_manager = resource_manager
        self.resource_type = resource_type
        self.the_rest = amount
        self.resource_cooldown = pg.time.get_ticks()
        self.available = True
    
    #Reduire les ressources
    def mine(self, team=""):
        if self.the_rest > 0 and self.available:
            now = pg.time.get_ticks()
            if now - self.resource_cooldown > 2000:  # Delay entre la collecte
                self.the_rest -= 1  
                self.resource_cooldown = now
                
                # Ajouter ressources à l'equipe appropriee
                if team == "Blue":
                    self.resource_manager.starting_resources[self.resource_type] += 1
                elif team == "Red":
                    self.resource_manager.starting_resources_AI[self.resource_type] += 1
                return 1
        else:
            self.available = False  # Resource is depleted
            return 0
                                    
class Map_Tree(MapResource):
    def __init__(self, resource_manager):
        super().__init__(resource_manager, "Wood", 100)

class Map_Gold(MapResource):
    def __init__(self, resource_manager):
        super().__init__(resource_manager, "Gold", 800)
