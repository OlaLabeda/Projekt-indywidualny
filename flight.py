class Flight:
    def __init__(self, flight_id, go_from,
                 go_to, date_from, date_to,
                 hour_from, hour_to, gate_number,
                 boarding_till,
                 plane_id, plane_name):
        self._flight_id = flight_id
        self._go_from = go_from
        self._go_to = go_to
        self._date_from = date_from
        self._date_to  = date_to
        self._hour_from = hour_from
        self._hour_to = hour_to
        self._gate_number = gate_number
        self._boarding_till = boarding_till
        self._plane_id = plane_id
        self._plane_name = plane_name

    def flight_id(self):
        return self._flight_id

    def go_from(self):
        return self._go_from

    def go_to(self):
        return self._go_to

    def date_from(self):
        return self._date_from

    def date_to(self):
        return self._date_to

    def hour_from(self):
        return self._hour_from

    def hour_to(self):
        return self._hour_to

    def gate_number(self):
        return self._gate_number

    def boarding_till(self):
        return self._boarding_till

    def plane_id(self):
        return self._plane_id

    def plane_name(self):
        return self._plane_name