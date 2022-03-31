import  math
import  json
# from fitness_tools.meals.meal_maker import MakeMeal
try:
    with open("urfit_data.json") as f:
        data = json.load(f)
except:data={}
class  Player:
    def __init__(self,name,age,waight,hieght,gender,nick,waist,num_train_per_weak,player_target,player_activ,num_of_meals_per_day):
        self.name = name
        self.age = age
        self.waight=waight
        self.hieght=hieght
        self.gender = gender
        self.nick = nick
        self.waist=waist
        self.num_train_per_weak=num_train_per_weak
        self.player_target=player_target
        self.player_activ=player_activ
        self.num_of_meals_per_day=num_of_meals_per_day
    def cals(self):
        if self.gender == "male":
            cals=(10*int(self.waight))+(6.25*int(self.hieght))-(5*int(self.age))+5
        elif self.gender =="fmale":
            cals=(10*int(self.waight))+(6.25*int(self.hieght))-(5*int(self.age))-161
        return cals
    def fats(self):
        if self.gender == "male":
            fats=((495)/(1.0324-0.19077*math.log10(int(self.waist)-int(self.nick))+0.15456*math.log10(int(self.hieght))))-450
        elif self.gender =="fmale":
            fats=((495)/(1.29579-0.35004*math.log10(int(self.waist)-int(self.nick))+0.22100*math.log10(int(self.hieght))))-450
        return fats
    def fats_discription(self):
        if self.gender == "male":
            if 5>self.fats()>2:
                fat_description="Essential fat"
            elif 13>self.fats()>6:
                fat_description="Athelets"
            elif 17>self.fats()>14:
                fat_description="fitness"
            elif 24>self.fats()>18:
                fat_description="Normally"
            elif self.fats()>25:
                fat_description="Obese"
        elif self.gender =="fmale":
            if 13>=self.fats()>=10:
                fat_description="Essential fat"
            elif 20>=self.fats()>=14:
                fat_description="Athelets"
            elif 24>=self.fats()>=21:
                fat_description="fitness"
            elif 31>=self.fats()>=25:
                fat_description="Normally"
            elif self.fats()>=32:
                fat_description="Obese"
        return fat_description
    def ideal_fat(self):
        if self.gender == "male":
            if 10<=int(self.age)<=20:
                ideal_fat="8.5%"
            elif 21<=int(self.age)<=25:
                ideal_fat="10.5%"
            elif 26<=int(self.age)<=30:
                ideal_fat="12.7%"
            elif 31<=int(self.age)<=35:
                ideal_fat="13.7%"
            elif 36<=int(self.age)<=40:
                ideal_fat="15.3%"
            elif 41<=int(self.age)<=45:
                ideal_fat="16.4%"
            elif 46<=int(self.age)<=50:
                ideal_fat="18.9%"
            elif 51<=int(self.age)<=55:
                ideal_fat="20.9%"
        elif self.gender =="fmale":
            if 10<=int(self.age)<=20:
                ideal_fat="8.5%"
            elif 21<=int(self.age)<=25:
                ideal_fat="10.5%"
            elif 26<=int(self.age)<=30:
                ideal_fat="12.7%"
            elif 31<=int(self.age)<=35:
                ideal_fat="13.7%"
            elif 36<=int(self.age)<=40:
                ideal_fat="15.3%"
            elif 41<=int(self.age)<=45:
                ideal_fat="16.4%"
            elif 46<=int(self.age)<=50:
                ideal_fat="18.9%"
            elif 51<=int(self.age)<=55:
                ideal_fat="20.9%"
        return ideal_fat
    def get_cals_for_launch(self):
        cals=self.target_cals()
        num_of_meals_per_day=int(self.num_of_meals_per_day)
        if num_of_meals_per_day ==2:
            launch_cals=cals/2
        elif 5>num_of_meals_per_day >=3:
            launch_cals=cals*0.35
        elif 5>num_of_meals_per_day ==4:
            launch_cals=cals*0.30
        elif 6>num_of_meals_per_day==5:
            launch_cals=cals*0.27
        elif 7>num_of_meals_per_day==6:
            launch_cals=cals*0.28
        else:
            launch_cals="you have to visite doctor"
        return int(launch_cals)
    def get_cals_for_dinner(self):
        cals=self.target_cals()
        num_of_meals_per_day=int(self.num_of_meals_per_day)
        if num_of_meals_per_day ==2:
            dinner_cals=0
        elif 4>num_of_meals_per_day ==3:
            dinner_cals=cals*0.30
        elif 5>num_of_meals_per_day ==4:
            dinner_cals=cals*0.25
        elif 6>num_of_meals_per_day==5:
            dinner_cals=cals*0.20
        elif 7>num_of_meals_per_day==6:
            dinner_cals=cals*0.17
        else:
            dinner_cals="you have to visite doctor"
        return int(dinner_cals)
    def get_cals_for_additional(self):
        cals=self.target_cals()
        num_of_meals_per_day=int(self.num_of_meals_per_day)
        if num_of_meals_per_day ==2:
            additional_cals=0
        elif 4>num_of_meals_per_day ==3:
            additional_cals=0
        elif 5>num_of_meals_per_day ==4:
            additional_cals=cals*0.15
        elif 6>num_of_meals_per_day==5:
            additional_cals=cals*0.26/2
        elif 7>num_of_meals_per_day==6:
            additional_cals=cals*0.30/3
        else:
            additional_cals="you have to visite doctor"
        return int(additional_cals)
    def get_cals_for_breakfast(self):
        cals=self.target_cals()
        num_of_meals_per_day=int(self.num_of_meals_per_day)
        if num_of_meals_per_day ==2:
            breakfast_cals=cals/2
        elif 4>num_of_meals_per_day ==3:
            breakfast_cals=cals*0.35
        elif 5>num_of_meals_per_day ==4:
                breakfast_cals=cals*0.30
        elif 6>num_of_meals_per_day==5:
            breakfast_cals=cals*0.27
        elif 7>num_of_meals_per_day==6:
            breakfast_cals=cals*0.25
        else:
            breakfast_cals="you have to visite doctor"
        return int(breakfast_cals)
    
    def get_max_protien(self):
        if 3>=int(self.age)>1:
            stand_protien=13
        elif 8>=int(self.age)>3:
            stand_protien=19
        elif 13>=int(self.age)>8:
            stand_protien=34
        elif 18>=int(self.age)>13 and self.gender=="fmale":
            stand_protien=46
        elif 18>=int(self.age)>13 and self.gender=="male":
            stand_protien=52
        elif int(self.age)>18 and self.gender=="male":
            stand_protien=56
        elif 18>=int(self.age)>13 and self.gender=="fmale":
            stand_protien=46
        protien_from_waight=(int(self.waight))*1.9
        protien_per_Day=protien_from_waight+stand_protien
        return protien_per_Day
    def get_min_protien(self):
        if 3>=int(self.age)>1:
            stand_protien=13
        elif 8>=int(self.age)>3:
            stand_protien=19
        elif 13>=int(self.age)>8:
            stand_protien=34
        elif 18>=int(self.age)>13 and self.gender=="fmale":
            stand_protien=46
        elif 18>=int(self.age)>13 and self.gender=="male":
            stand_protien=52
        elif int(self.age)>18 and self.gender=="male":
            stand_protien=56
        elif 18>=int(self.age)>13 and self.gender=="fmale":
            stand_protien=46
        protien_from_waight=(int(self.waight))*1.02
        protien_per_Day=protien_from_waight
        return protien_per_Day

    def target_carbs(self):
        if self.player_activ == "1":
            carbs= int(self.cals()) * 0.30
        elif self.player_activ=="2":
            carbs= int(self.cals()) * 0.31
        elif self.player_activ=="3":
            carbs= int(self.cals()) * 0.33
        elif self.player_activ=="4":
            carbs= int(self.cals()) * 0.34
        elif self.player_activ=="5":
            carbs= int(self.cals()) * 0.35
        if self.player_target =="weight_loss":
            carbs= carbs * 0.85
        elif self.player_target =="gain_muscles":
            carbs=carbs*95
        carbs=carbs/4
        return carbs
    def body_mass(self):
        bmi=int(self.waight)/((int(self.hieght)/100)**2)
        return bmi


# payer= Player("ahmed","25","86","183","male","41","99","15","weight_loss","2","4")
payer= Player(age="34",waight="76",hieght="175",gender="male",nick="39",waist="93",player_activ="5",player_target="weight_loss",num_train_per_weak="6",num_of_meals_per_day="3")
print("fats",payer.fats())
print("fats discriptions",payer.fats_discription())
# print("target cals",payer.target_cals())
print("cals",payer.cals())
print("target breakfast",payer.get_cals_for_breakfast())
print("target dinner",payer.get_cals_for_dinner())
print("additional",payer.get_cals_for_launch())
print("ideal fats",payer.ideal_fat())
print("protien",payer.get_min_protien())
print("carvs",payer.target_carbs())
#name,age,waight,hieght,gender,nick,waist,num_train_per_weak,player_target,player_activ,num_of_meals_per_day
# payer1= Player("mohammed","25","86","183","male","41","99","15","weight_loss","3","3")
# payer2= Player("esraa","25","86","183","male","41","99","15","weight_loss","4","4")
# payer3= Player("mohammedy","25","86","183","male","41","99","15","weight_loss","5","5")
# payer4= Player("magdi","25","86","183","male","41","99","15","weight_loss","6","6")
# payer.add_name_data()
# payer1.add_name_data()
# payer2.add_name_data()
# payer3.add_name_data()
# payer4.add_name_data()
# print(payer.fats(),payer.fats_discription())
# print(payer.get_cals_for_breakfast(),"cals for break fast","prtin up",payer.get_max_protien()," min ",int(payer.get_min_protien()))
# print(payer.target_cals(),"target cals")
# print(payer.get_max_protien(),"protiens")
# print(payer.fats())
# print(payer.target_carbs())
# print(payer.)
# #to lose 0.5kg / weak 69% of cals
#90% .25kg
#61% 1kk