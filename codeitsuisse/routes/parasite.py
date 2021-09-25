import logging
import json
import copy

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

class Parasite_A():
    def __init__(self, room, grid, interestedIndividuals):
        self.room_no = room
        self.grid = copy.deepcopy(grid)
        self.grid_c = [[False for _ in self.grid[0]] for _ in self.grid]
        
        self.interestedIndividuals_loc = {}
        self.p1 = {}
        self.p2 = 0
        
        self.time = 0
        self.max_time = max(len(grid), len(grid[0]))
        
        self.infect_time = [[-1 for _ in self.grid[0]] for _ in self.grid]
        
        for locs in interestedIndividuals:
            loc = locs.split(",")
            # print(loc)
            self.interestedIndividuals_loc[locs] = (int(loc[0]), int(loc[1])) # x, y, time
            self.p1[locs] = -1
        
    def tick(self):
        self.time += 1
    
    def spread(self):
        for x in range(self.max_time + 1):
            # print(self.p1)
            self.tick()
            
            # reset grid_change
            self.grid_c = [[False for _ in self.grid[0]] for _ in self.grid]
            
            for row_idx, row in enumerate(self.grid):
                for col_idx, col in enumerate(row):
                    # if this person is invected
                    if col == 3 and not self.grid_c[row_idx][col_idx]:
                        try: # up
                            cur_row = row_idx - 1
                            cur_col = col_idx
                            if self.grid[cur_row][cur_col] == 1 and not self.grid_c[cur_row][cur_col]:
                                self.grid[cur_row][cur_col] = 3
                                self.infect_time[cur_row][cur_col] = self.time
                                self.grid_c[cur_row][cur_col] = True
                                if str(cur_row)+','+str(cur_col) in self.p1:
                                    self.p1[str(cur_row)+','+str(cur_col)] = self.time
                        except IndexError:
                            pass
                        
                        try: # down
                            cur_row = row_idx + 1
                            cur_col = col_idx
                            if self.grid[cur_row][cur_col] == 1:
                                self.grid[cur_row][cur_col] = 3
                                self.infect_time[cur_row][cur_col] = self.time
                                # print(self.time)
                                self.grid_c[cur_row][cur_col] = True
                                if str(cur_row)+','+str(cur_col) in self.p1:
                                    self.p1[str(cur_row)+','+str(cur_col)] = self.time
                        except IndexError:
                            pass
                        
                        try: #left
                            cur_row = row_idx
                            cur_col = col_idx - 1
                            if self.grid[cur_row][cur_col] == 1:
                                self.grid[cur_row][cur_col] = 3
                                self.infect_time[cur_row][cur_col] = self.time
                                self.grid_c[cur_row][cur_col]
                                if str(cur_row)+','+str(cur_col) in self.p1:
                                    self.p1[str(cur_row)+','+str(cur_col)] = self.time
                        except IndexError:
                            pass
                        
                        try: # right
                            cur_row = row_idx
                            cur_col = col_idx + 1
                            if self.grid[cur_row][cur_col] == 1:
                                self.grid[cur_row][cur_col] = 3
                                self.infect_time[cur_row][cur_col] = self.time
                                self.grid_c[cur_row][cur_col] = True
                                if str(cur_row)+','+str(cur_col) in self.p1:
                                    self.p1[str(cur_row)+','+str(cur_col)] = self.time
                        except IndexError:
                            pass
                        
                        
        # min time to infect all healthy people
        min_time = -1
        for row in self.infect_time:
            for col in row:
                if col > min_time:
                    min_time = col
        self.p2 = min_time
        
        for row_idx, row in enumerate(self.grid):
            for col_idx, col in enumerate(row):
                if col == 1:
                    self.p2 = -1
                    break
                
class Parasite_B(Parasite_A):
    def __init__(self, room, grid, interestedIndividuals):
        super().__init__(room, grid, interestedIndividuals)
        self.p3 = -1
            
    def spread(self):
        for x in range(self.max_time + 1):
            # print(self.p1)
            self.tick()
            # print(self.grid)
            #print(self.grid_c, "\n")
            # reset grid_change
            self.grid_c = [[False for _ in self.grid[0]] for _ in self.grid]
            
            for row_idx, row in enumerate(self.grid):
                for col_idx, col in enumerate(row):
                    # if this person is infected
                    if col == 3 and not self.grid_c[row_idx][col_idx]:
                        try: # up
                            cur_row = row_idx - 1
                            cur_col = col_idx
                            if self.grid[cur_row][cur_col] == 1:
                                self.grid[cur_row][cur_col] = 3
                                self.infect_time[cur_row][cur_col] = self.time
                                self.grid_c[cur_row][cur_col] = True
                                if str(cur_row)+','+str(cur_col) in self.p1:
                                    self.p1[str(cur_row)+','+str(cur_col)] = self.time
                        except IndexError:
                            pass
                        
                        try: # down
                            cur_row = row_idx + 1
                            cur_col = col_idx
                            if self.grid[cur_row][cur_col] == 1:
                                self.grid[cur_row][cur_col] = 3
                                self.infect_time[cur_row][cur_col] = self.time
                                # print(self.time)
                                self.grid_c[cur_row][cur_col] = True
                                if str(cur_row)+','+str(cur_col) in self.p1:
                                    self.p1[str(cur_row)+','+str(cur_col)] = self.time
                        except IndexError:
                            pass
                        
                        try: #left
                            cur_row = row_idx
                            cur_col = col_idx - 1
                            if self.grid[cur_row][cur_col] == 1:
                                self.grid[cur_row][cur_col] = 3
                                self.infect_time[cur_row][cur_col] = self.time
                                self.grid_c[cur_row][cur_col] = True
                                if str(cur_row)+','+str(cur_col) in self.p1:
                                    self.p1[str(cur_row)+','+str(cur_col)] = self.time
                        except IndexError:
                            pass
                        
                        try: # right
                            cur_row = row_idx
                            cur_col = col_idx + 1
                            if self.grid[cur_row][cur_col] == 1:
                                self.grid[cur_row][cur_col] = 3
                                self.infect_time[cur_row][cur_col] = self.time
                                self.grid_c[cur_row][cur_col] = True
                                if str(cur_row)+','+str(cur_col) in self.p1:
                                    self.p1[str(cur_row)+','+str(cur_col)] = self.time
                        except IndexError:
                            pass
                        
                        # diagonal
                        try: # left-up
                            cur_row = row_idx - 1
                            cur_col = col_idx - 1
                            if self.grid[cur_row][cur_col] == 1:
                                self.grid[cur_row][cur_col] = 3
                                self.infect_time[cur_row][cur_col] = self.time
                                self.grid_c[cur_row][cur_col] = True
                                if str(cur_row)+','+str(cur_col) in self.p1:
                                    self.p1[str(cur_row)+','+str(cur_col)] = self.time
                        except IndexError:
                            pass
                        
                        try: # right-up
                            cur_row = row_idx - 1
                            cur_col = col_idx + 1
                            if self.grid[cur_row][cur_col] == 1:
                                self.grid[cur_row][cur_col] = 3
                                self.infect_time[cur_row][cur_col] = self.time
                                self.grid_c[cur_row][cur_col] = True
                                if str(cur_row)+','+str(cur_col) in self.p1:
                                    self.p1[str(cur_row)+','+str(cur_row)] = self.time
                        except IndexError:
                            pass
                        
                        try: # left-down
                            cur_row = row_idx + 1
                            cur_col = col_idx - 1
                            if self.grid[cur_row][cur_col] == 1:
                                self.grid[cur_row][cur_col] = 3
                                self.infect_time[cur_row][cur_col] = self.time
                                self.grid_c[cur_row][cur_col] = True
                                if str(cur_row)+','+str(cur_col) in self.p1:
                                    self.p1[str(cur_row)+','+str(cur_row)] = self.time
                        except IndexError:
                            pass                        
                        
                        try: # right-down
                            cur_row = row_idx + 1
                            cur_col = col_idx - 1
                            if self.grid[cur_row][cur_col] == 1:
                                self.grid[cur_row][cur_col] = 3
                                self.infect_time[cur_row][cur_col] = self.time
                                self.grid_c[cur_row][cur_col] = True
                                if str(cur_row)+','+str(cur_col) in self.p1:
                                    self.p1[str(cur_row)+','+str(cur_row)] = self.time
                        except IndexError:
                            pass
                        
                        
        # min time to infect all healthy people
        min_time = -1
        for row in self.infect_time:
            for col in row:
                if col > min_time:
                    min_time = col
        self.p3 = min_time
        
        for row_idx, row in enumerate(self.grid):
            for col_idx, col in enumerate(row):
                if col == 1:
                    self.p3 = -1
                    break
        
class Parasite_X(Parasite_A):
    def __init__(self, room, grid, interestedIndividuals):
        super().__init__(room, grid, interestedIndividuals)
        self.parasite_exist = [[False for _ in self.grid[0]] for _ in self.grid]
        self.p4 = 0
    
    def infected(self, row, col):
        if self.grid[row][col] == 1:
            self.grid[row][col] = 3
            # if str(row)+','+str(col) in self.p1:
            #     self.p1[str(row)+','+str(col)] = self.time
    
    def all_infected(self):
        no_1 = True
        for row in self.grid:
            for col in row:
                if col == 1:
                    no_1 = False
        
        return no_1
    
    def spread(self):
        for x in range(self.max_time + 1):
            # print(self.p1)
            
            for row_idx, row in enumerate(self.grid):
                for col_idx, col in enumerate(row):
                    if self.parasite_exist[row_idx][col_idx] == True:
                        self.infected(row_idx, col_idx)
                        
            if self.all_infected():
                return
            
            self.tick()
            
            
                    
            
            # reset grid_change
            # self.grid_c = [[False for _ in self.grid[0]] for _ in self.grid]
            
            for row_idx, row in enumerate(self.grid):
                for col_idx, col in enumerate(row):
                    # if this person is invected
                    if col == 3:
                        try: # up
                            cur_row = row_idx - 1
                            cur_col = col_idx
                            
                            self.parasite_exist[cur_row][cur_col] = True
                            if (self.grid[cur_row][cur_col] == 0) or (self.grid[cur_row][cur_col] == 2):
                                self.p4 += 1
                            # if self.grid[cur_row][cur_col] == 1:
                            #     self.parasite_exist[cur_row][cur_col] = True
                            #     self.infect_time[cur_row][cur_col] = self.time
                            #     # self.grid_c[cur_row][cur_col] = True
                            #     if str(cur_row)+','+str(cur_col) in self.p1:
                            #         self.p1[str(cur_row)+','+str(cur_col)] = self.time
                        except IndexError:
                            pass
                        
                        try: # down
                            cur_row = row_idx + 1
                            cur_col = col_idx
                            
                            self.parasite_exist[cur_row][cur_col] = True
                            if (self.grid[cur_row][cur_col] == 0) or (self.grid[cur_row][cur_col] == 2):
                                self.p4 += 1
                            # if self.grid[cur_row][cur_col] == 1:
                            #     self.parasite_exist[cur_row][cur_col] = True
                            #     self.infect_time[cur_row][cur_col] = self.time
                            #     # print(self.time)
                            #     # self.grid_c[cur_row][cur_col] = True
                            #     if str(cur_row)+','+str(cur_col) in self.p1:
                            #         self.p1[str(cur_row)+','+str(cur_col)] = self.time
                        except IndexError:
                            pass
                        
                        try: #left
                            cur_row = row_idx
                            cur_col = col_idx - 1
                            
                            self.parasite_exist[cur_row][cur_col] = True
                            if (self.grid[cur_row][cur_col] == 0) or (self.grid[cur_row][cur_col] == 2):
                                self.p4 += 1
                            # if self.grid[cur_row][cur_col] == 1:
                            #     self.parasite_exist[cur_row][cur_col] = True
                            #     self.infect_time[cur_row][cur_col] = self.time
                            #     # self.grid_c[cur_row][cur_col]
                            #     if str(cur_row)+','+str(cur_col) in self.p1:
                            #         self.p1[str(cur_row)+','+str(cur_col)] = self.time
                        except IndexError:
                            pass
                        
                        try: # right
                            cur_row = row_idx
                            cur_col = col_idx + 1
                            
                            self.parasite_exist[cur_row][cur_col] = True
                            if (self.grid[cur_row][cur_col] == 0) or (self.grid[cur_row][cur_col] == 2):
                                self.p4 += 1
                            # if self.grid[cur_row][cur_col] == 1:
                            #     self.parasite_exist[cur_row][cur_col] = True
                            #     self.infect_time[cur_row][cur_col] = self.time
                            #     self.grid_c[cur_row][cur_col] = True
                            #     if str(cur_row)+','+str(cur_col) in self.p1:
                            #         self.p1[str(cur_row)+','+str(cur_col)] = self.time
                        except IndexError:
                            pass
                        
    
    
        
# Number	Representation
#   0	         Vacant
#   1	         Healthy
#   2	       Vaccinated
#   3	        Infected
@app.route('/parasite', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = []
    for room in data:
        #print(room["grid"])
        A = Parasite_A(room["room"], room["grid"], room["interestedIndividuals"])
        A.spread()
        #print(room["grid"], "\n") 
        
        B = Parasite_B(room["room"], room["grid"], room["interestedIndividuals"])
        B.spread()
        #print(B.grid)
        print(B.infect_time, "\n")
        X = Parasite_X(room["room"], room["grid"], room["interestedIndividuals"])
        X.spread()
        result.append( {
            "room": room["room"],
            "p1": A.p1, 
            "p2": A.p2,
            "p3": B.p3,
            "p4": X.p4} )
    
    logging.info("My result :{}".format(result))
    return json.dumps(result)



