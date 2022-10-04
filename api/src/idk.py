from datetime import datetime, timedelta

class Schedule:
    def __init__(self, reminder_offsets):
        self.current_time = datetime.now()
        self.reminder_offsets = list(self.sum_offsets(
            timedelta(**offset) for offset in reminder_offsets.items()
        ))

    def sum_offsets(self, reminder_offsets):
        """ Now each offset is a sum of all before it so that the returned values has each time
            measured since the previous reminder and not the beginning of the shedule (self.current_time)
        """
        curr_time = self.current_time
        for offset in reminder_offsets:
            curr_time += offset
            yield curr_time

def main():

    # [timedelta(minutes=5), timedelta(minutes=20),timedelta(hours=5),timedelta(minutes=5),timedelta(minutes=5),]
    reminder_offsets = {
        "minutes": 5,
        "minutes": 20,
        "hours": 5,
        "minutes": 5,
    }
    shedule = Schedule(reminder_offsets)

if __name__ == "__main__":
    main()

