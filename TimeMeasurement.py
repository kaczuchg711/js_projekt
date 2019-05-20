class TimeMeasurement:
    def __init__(self):
        self.time_N_A_issue_for_counter = [0, 0, 0]
        self.time_N_B_issue_for_counter = [0, 0, 0]

        self.time_V_A_issue_for_counter = [0, 0, 0]
        self.time_V_B_issue_for_counter = [0, 0, 0]

    def __call__(self, time_of_one_client, kind, NV, counter_nr):
        if NV == "N":
            if kind == "A":
                self.time_N_A_issue_for_counter[counter_nr] += time_of_one_client
            elif kind == "B":
                self.time_N_B_issue_for_counter[counter_nr] += time_of_one_client

        elif NV == "VIP":
            if kind == "A":
                self.time_V_A_issue_for_counter[counter_nr] += time_of_one_client
            elif kind == "B":
                self.time_V_B_issue_for_counter[counter_nr] += time_of_one_client

    def __str__(self) -> str:
        a = ""
        for x in (self.time_N_A_issue_for_counter + self.time_N_B_issue_for_counter +\
                 self.time_V_A_issue_for_counter + self.time_V_B_issue_for_counter):
            a += str(x) + " "

        return a
