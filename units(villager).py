class Villager:
    def __init__(self, resource_manager):
        self.resource_manager = resource_manager
        self.collected_resources = 0
        self.resource_type = None
        self.collect_rate = 25 / 60  # 25 ressources/minute
        self.max_capacity = 20
        self.resource_cooldown = pg.time.get_ticks()

    def collect(self, resource_tile, team="Blue"):
        now = pg.time.get_ticks()
        if now - self.resource_cooldown >= 1000:  
            
            if not resource_tile.mine(team):   
                #print("Resource is depleted, turning into soil.")
                return
            
            collect_amount = min(self.collect_rate, resource_tile.the_rest)
            
            if self.collected_resources + collect_amount <= self.max_capacity and resource_tile.the_rest > 0:
                self.collected_resources += collect_amount
                self.resource_type = resource_tile.resource_type
                self.resource_cooldown = now
                #print(f"Villager is collecting {self.resource_type}: {self.collected_resources}/{self.max_capacity}")
            else:
                #print("Villager is full, must return to drop resources.")

    def drop_resources(self, town_center, team="Blue"):
        if self.collected_resources > 0:
            if team == "Blue":
                self.resource_manager.starting_resources[self.resource_type] += self.collected_resources
            elif team == "Red":
                self.resource_manager.starting_resources_AI[self.resource_type] += self.collected_resources

            #print(f"Villager dropped {self.collected_resources} {self.resource_type} at the Town Center.")
            self.collected_resources = 0
