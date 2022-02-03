class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []
        
    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)
            

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)


    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)


    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)


    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)
         
         
    def subscription_info(self, subscription_id):
        result = ''
        subs_info = [x for x in self.subscriptions if x.id == subscription_id][0]
        result += subs_info.__repr__() + '\n'
        customer_info  = [x for x in self.customers if x.id == subs_info.customer_id][0]
        result += customer_info.__repr__() + '\n'
        trainer_info  = [x for x in self.trainers if x.id == subs_info.trainer_id][0]
        result += trainer_info.__repr__() + '\n'
        equ_info = [x for x in self.equipment if x.id == subs_info.exercise_id][0]
        result += equ_info.__repr__() + '\n'
        plan_info = [x for x in self.plans][0]
        result += plan_info.__repr__() 
        return result

