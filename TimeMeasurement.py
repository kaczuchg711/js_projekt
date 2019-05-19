


class TimeMeasurement:
    def __init__(self):
        self.time_N_all = 0
        self.time_N_A_issue = 0
        self.time_N_B_issue = 0
        self.time_N_1_window = 0
        self.time_N_2_window = 0
        self.time_N_3_window = 0


        self.time_VIP_all = 0
        self.time_VIP_A_issue = 0
        self.time_VIP_B_issue = 0
        self.time_VIP_1_window = 0
        self.time_VIP_2_window = 0
        self.time_VIP_3_window = 0

    def __call__(self,time_of_one_client,kind,NV,w_nr):
        if NV == "N":
            self.time_N_all += time_of_one_client

