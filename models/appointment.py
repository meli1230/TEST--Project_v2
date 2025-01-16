class Appointment:
    def __init__(self, user, consultant, customer_time, mentor_time):
        '''
        Initializes an appointment object with the following parameters:
        :param user: the user who booked the appointment
        :param consultant: the consultant assigned for this appointment
        :param customer_time: the date and time of the appointment in the customer's timezone
        :param mentor_time: the date and time of the appointment in the mentor's timezone
        '''
        self.user = user  #store the user who booked the appointment
        self.consultant = consultant  #store the consultant assigned for this appointment
        self.customer_time = customer_time  #store the date and time in customer's timezone
        self.mentor_time = mentor_time  #store the date and time in mentor's timezone

    def __repr__(self):
        '''
        Defines a string representation of the appointment object
        :return: user name, consultant, customer time, and mentor time
        '''
        return (f"Appointment(User: {self.user.name}, Consultant: {self.consultant}, "  #return formatted string showing user name and consultant
                f"Customer Time: {self.customer_time}, Mentor Time: {self.mentor_time})")  #include both customer and mentor times